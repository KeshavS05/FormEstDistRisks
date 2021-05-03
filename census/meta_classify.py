import utils
import seaborn as sns
import pandas as pd

import numpy as np
from tqdm import tqdm
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from joblib import load
import os

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path1', type=str, default='',
                        help='path to first folder of models')
    parser.add_argument('--path2', type=str, default='',
                        help='path to second folder of models')
    parser.add_argument('--sample', type=int, default=0,
                        help='how many models to use for meta-classifier')
    parser.add_argument('--multimode', type=bool, default=False,
                        help='experiment for multiple samples?')
    parser.add_argument('--ntimes', type=int, default=5,
                        help='number of repetitions for multimode')
    parser.add_argument('--plot_title', type=str, default="",
                        help='desired title for plot, sep by _')
    args = parser.parse_args()
    utils.flash_utils(args)

    # Census Income dataset
    if (not args.multimode) and args.sample < 1:
        raise ValueError("At least one model must be used!")

    paths = [args.path1, args.path2]
    ci = utils.CensusIncome("./census_data/")

    w, b = [], []
    labels = []

    for i, path_seg in enumerate(paths):
        distr_x, distr_y = [], []
        models_in_folder = os.listdir(path_seg)
        np.random.shuffle(models_in_folder)
        if not args.multimode:
            models_in_folder = models_in_folder[:args.sample]
        for path in models_in_folder:
            clf = load(os.path.join(path_seg, path))

            # Look at weights linked to 'sex:Female' as well as 'sex:Male'
            _, _, cols = ci.load_data()
            f_weight = clf.coefs_[0][cols.get_loc("sex:Female")]
            m_weight = clf.coefs_[0][cols.get_loc("sex:Male")]
            distr_x.append(np.mean(f_weight))
            distr_y.append(np.mean(f_weight ** 2))

            # Look at initial layer weights, biases
            processed = clf.coefs_[0]

            processed = np.concatenate(
                (np.mean(processed, 1), np.mean(processed ** 2, 1)))
            w.append(processed)
            b.append(clf.intercepts_[0])
            labels.append(i)

        # plt.plot(distr_x, distr_y, 'o', label=str(i))
    # plt.legend()
    # plt.savefig("../visualize/quick_distr_look.png")
    # exit(0)

    w = np.array(w)
    b = np.array(w)
    labels = np.array(labels)

    if args.multimode:
        columns = [
            "Size of train-set for meta-classifier",
            "Accuracy on unseen models"
        ]
        data = []
        trainSetSizes = [
            4, 6, 10, 25, 50,
            100, 150, 200, 300,
            400, 450
        ]
        # Reserve 100 classifiers for testing
        X_train, X_test, y_train, y_test = train_test_split(
            w, labels, test_size=500)
        for tss in tqdm(trainSetSizes):
            x_tr, unused, y_tr, unused = train_test_split(
                X_train, y_train, train_size=tss)
            for j in range(args.ntimes):
                # Train meta-classifier
                clf = MLPClassifier(hidden_layer_sizes=(30, 30),
                                    max_iter=1000)
                clf.fit(x_tr, y_tr)
                data.append([tss, clf.score(X_test, y_test)])

        # Plot performance with size of training set
        # For meta-classifier
        df = pd.DataFrame(data, columns=columns)
        sns_plot = sns.boxplot(x="Size of train-set for meta-classifier",
                               y="Accuracy on unseen models",
                               data=df)
        plt.ylim(0.45, 1.0)
        # plt.title(" ".join(args.plot_title.split('_')))
        sns_plot.figure.savefig("../visualize/census_meta_scores.png")

    else:
        clf = MLPClassifier(hidden_layer_sizes=(30, 30), max_iter=500)
        X_train, X_test, y_train, y_test = train_test_split(
            w, labels, test_size=0.7)
        clf.fit(X_train, y_train)
        print("Meta-classifier performance on train data: %.2f" %
              clf.score(X_train, y_train))
        print("Meta-classifier performance on test data: %.2f" %
              clf.score(X_test, y_test))

        # Plot score distributions on test data
        labels = ['Trained on $D_0$', 'Trained on $D_1$']
        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        zeros = np.nonzero(y_test == 0)[0]
        ones = np.nonzero(y_test == 1)[0]

        score_distrs = clf.predict_proba(X_test)[:, 1]

        plt.hist(score_distrs[zeros], 20, label=labels[0], alpha=0.9)
        plt.hist(score_distrs[ones], 20, label=labels[1], alpha=0.9)

        plt.title("Metal-classifier score prediction distributions for unseen models")
        plt.xlabel("Meta-classifier $Pr$[trained on $D_1$]")
        plt.ylabel("Number of models")
        plt.legend()

    plt.savefig("../visualize/census_meta_scores.png")