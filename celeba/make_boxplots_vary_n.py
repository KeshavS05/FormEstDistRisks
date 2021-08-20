import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_utils import SUPPORTED_PROPERTIES
import argparse
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--darkplot', action="store_true",
                        help='Use dark background for plotting results')
    parser.add_argument('--legend', action="store_true",
                        help='Add legend to plots')
    parser.add_argument('--novtitle', action="store_true",
                        help='Remove Y-axis label')
    parser.add_argument('--filter', choices=SUPPORTED_PROPERTIES,
                        default="Male",
                        help='name for subfolder to save/load data from')
    args = parser.parse_args()

    first_cat = " 0.5"

    if args.darkplot:
        # Set dark background style
        plt.style.use('dark_background')

    # Set font size
    # plt.rcParams.update({'font.size': 18})
    plt.rcParams.update({'font.size': 14})

    data = []
    columns = [
        r'Male proportion of training data ($\alpha$)',
        "Accuracy (%)",
        r'$n$'
    ]

    categories = ["0.0", "0.1", "0.2", "0.3",
                  "0.4", "0.6", "0.7", "0.8", "0.9", "1.0"]
    if args.filter == "Young":
        columns[0] = r'Old proportion of training data ($\alpha$)'
        raw_data = {
            # Done
            "All": {
                1600: [
                    [61.11, 65.13, 66.50, 70.78, 79.44],
                    [59.25, 59.3, 55.54, 59.66, 59.66],
                    [50.93, 61.33, 52.91, 50.61, 51.40],
                    [50.83, 49.69, 50.29, 53.99, 47.94],
                    [50.26, 50.44, 50.10, 50.46, 49.74],
                    [49.99, 50.96, 49.86, 49.99, 50.29],
                    [52.43, 49.92, 50, 52.71, 51.51],
                    [54.32, 55.63, 48.89, 51.08, 49.1],
                    [63.24, 51.68, 69.19, 65.8, 65.98],
                    [74.9, 82.13, 82.44, 82.44, 86.23]
                ],
                100: [
                    [55.28, 50.95, 54.14, 52.94, 54.21],
                    [51.83, 50.56, 50.64, 52.04, 50.14],  # 0.1
                    [57.79, 52.75, 53.85, 58.02, 52.0], # 0.9
                    [50.09, 56.3, 65.99, 56.04, 53.00]
                ]
            },
            # Done
            "1": {
                1600: [
                    [65.05, 70.21, 68.58, 64.61, 70.49],
                    [52.25, 56.98, 57.56, 53.4, 51.1],
                    [53.59, 52.93, 52.20, 52.57, 50.82],
                    [50.5, 48.59, 51.07, 51.41, 48.88],
                    [49.71, 50.72, 50.18, 52.23, 49.05],
                    [50.11, 50.14, 49.88, 49.94, 50.14],
                    [51.28, 51.36, 50.46, 51.74, 51.33],
                    [52.52, 51.37, 51.97, 53.33, 51.61],
                    [52.41, 52.52, 50.87, 54.66, 53.17],
                    [56.91, 63.05, 62.0, 59.34, 54.61]
                ]
            },
            # Done
            "2": {
                1600: [
                    [58.78, 53.85, 60.85, 58.96, 59.66],
                    [53.48, 55.29, 55.44, 52.30, 52.81],
                    [51.11, 48.94, 52.28, 51.76, 52.39],
                    [50.21, 51.51, 51.67, 51.33, 51.64],
                    [50.46, 49.49, 50.41, 50.05, 50.03],
                    [51.34, 50.29, 49.70, 50.24, 49.35],
                    [54.83, 55.01, 54.58, 55.40, 54.09],
                    [60.27, 59.72, 59.78, 60.32, 59.28],
                    [68.54, 52.57, 51.08, 67.10, 67.34],
                    [79.02, 77.03, 75.19, 79.96]
                ]
            },
            # Donne
            "3": {
                1600: [
                    [49.62, 50.48, 49.39, 49.26, 50.14],
                    [50.87, 49.98, 49.85, 50.66, 49.97],
                    [50.17, 49.0, 49.73, 50.17, 50.72],
                    [49.97, 48.72, 48.85, 49.53, 51.07],
                    [49.85, 49.02, 49.44, 49.59, 49.85],
                    [50.52, 50.24, 49.04, 49.83, 50.37],
                    [49.97, 50.66, 49.49, 49.67, 49.16],
                    [49.20, 50.74, 51.34, 48.26, 48.89],
                    [48.81, 51.08, 49.36, 51.08, 51.08],
                    [54.46, 56.04, 51.75, 49.73, 50.58]
                ]
            },
            # Done
            "4": {
                1600: [
                        [49.49, 50.56, 49.08, 49.29, 50.19],
                        [50.0, 49.97, 49.97, 50.10, 50.41],
                        [51.06, 50.48, 48.92, 49.6, 51.18],
                        [51.43, 51.07, 51.38, 51.72, 48.93],
                        [50.0, 51.03, 49.33, 50.51, 50.10],
                        [50.86, 50.27, 50.68, 50.14, 50.27],
                        [50.08, 49.46, 49.74, 50.28, 50.13],
                        [50.54, 51.08, 51.11, 50.12, 50.82],
                        [48.91, 51.13, 50.69, 49.52, 49.18],
                        [50.32, 50.14, 50.60, 52.16, 51.11]
                ]
            },
            # Done
            "5": {
                1600: [
                        [51.10, 51.02, 52.01, 50.97, 51.93],
                        [49.80, 52.00, 52.22, 52.0, 50.54],
                        [50.09, 49.26, 48.94, 49.15, 49.28],
                        [48.90, 49.61, 50.89, 49.63, 50.26],
                        [51.08, 49.74, 50.33, 49.79, 50.31],
                        [50.78, 50.14, 50.17, 50.29, 49.71],
                        [50.67, 50.15, 50.51, 50.15, 49.64],
                        [50.07, 49.93, 50.43, 51.11, 48.94],
                        [49.20, 50.87, 49.96, 50.77, 51.42],
                        [50.45, 49.58, 49.19, 50.58, 50.45]
                ]
            },
            # Done
            "6": {
                1600: [
                        [66.27, 77.73, 76.43, 72.67, 78.04],
                        [69.62, 72.69, 73.15, 73.07, 68.52],
                        [63.96, 62.97, 64.25, 63.49, 63.55],
                        [54.10, 51.77, 53.70, 54.54, 54.28],
                        [49.74, 51.46, 52.82, 52.16, 52.18],
                        [51.27, 51.5, 50.81, 51.75, 50.32],
                        [56.85, 55.42, 56.42, 55.58, 53.63],
                        [59.88, 53.12, 60.14, 58.71, 59.75],
                        [63.19, 66.34, 62.74, 63.87, 66.32],
                        [67.54, 74.04, 70.18, 72.92, 68.44]
                ]
            },
            # Done
            "7": {
                1600: [
                        [50.09, 49.29, 47.94, 49.16, 50.76],
                        [49.54, 49.31, 50.74, 50.13, 49.46],
                        [49.23, 50.98, 51.24, 49.26, 51.06],
                        [50.39, 49.06, 49.97, 48.54, 49.82],
                        [50.08, 50.08, 49.31, 49.79, 50.05],
                        [48.99, 48.76, 48.55, 49.32, 50.22],
                        [51.41, 49.26, 49.57, 50.0, 51.0],
                        [49.75, 49.73, 49.75, 50.98, 49.88],
                        [51.27, 50.69, 51.08, 49.57, 51.03],
                        [49.99, 50.01, 49.14, 51.65, 49.96]
                ]
            },
            # Done
            "8": {
                1600: [
                        [50.76, 49.24, 49.24, 50.76, 50.76],
                        [50.03, 50.03, 50.03, 49.97, 49.97],
                        [51.06, 48.94, 48.94, 51.06, 51.06],
                        [51.07, 48.93, 48.93, 51.07, 51.07],
                        [50.26, 50.26, 50.26, 50.26, 49.74],
                        [50.14, 50.14, 49.86, 50.14, 50.14],
                        [49.92, 49.92, 49.92, 49.92, 49.92],
                        [48.89, 48.89, 51.11, 48.89, 51.11],
                        [48.92, 48.92, 51.08, 51.08, 48.92],
                        [49.96, 50.04, 49.96, 50.04, 50.04]
                ]
            },
            # "sc3_fnc4_c": {
            #     1600: [
            #             [71.64, 50.76, 78.92, 50.76],
            #             [68.4, 50.03, 50.03, 50.03],
            #             [57.47, 54.34, 50.9, 50.56, 51.08],
            #             [51.07, 51.07, 53.86, 48.93, 50.31],
            #             [50.26, 50.36, 50.26],
            #             [50.14, 50.65, 50.22, 50.63],
            #             [50.08, 50.08, 49.92],
            #             [50.98, 51.11, 51.11],
            #             [48.87, 48.92, 51.08, 62.77],
            #             [50.19, 50.04, 50.04, 50.81, 59.80]
            #     ]
            # },
            # "5_6" : {
            #     100: [
            #             [51.69, 50.31, 50.18, 50.79, 51.46],
            #             [49.67, 51.15, 50.82, 49.97, 50.89],  # 0.1
            #             [50.48, 47.98, 51.21, 51.08, 49.57],  # 0.9
            #             [50.1, 50.01, 49.68, 51.14, 49.99],
            #     ]
            # },
            "all_fc": {
                100: [
                        [63.86, 58.75, 62.09, 55.87, 65.62], # 0.0
                        [58.38, 53.17, 57.36, 58.02, 57.05],
                        [52.36, 52.31, 55.41, 54.71, 54.60], # 0.9
                        [56.58, 57.25, 56.43, 59.62, 57.94]
                ]
            }
        }
    else:
        raw_data = {
            # Done
            "All": {
                10: [
                        [49.95, 54.25, 52.35, 53.1, 48.30],
                        [50.02, 50.92, 50.67, 50.87, 50.07],
                        [54.1, 46.63, 56.22, 53.04, 46.24],
                        [49.18, 50.58, 50.33, 48.98, 49.23],
                        [50.64, 51.71, 49.26, 50.64, 50.79],
                        [51.28, 49.24, 53.0, 49.98, 51.38],
                        [50.03, 50.37, 49.83, 50.27, 50.72],
                        [72.5, 61.33, 42.53, 75.94, 80.3],
                        [51.22, 51.27, 50.18, 50.32, 51.62],
                        [50.43, 50.67, 49.83, 48.43, 51.87]
                    ],
                20: [
                        [51.3, 51.75, 51.15, 55.04, 48.95],
                        [49.03, 50.08, 51.12, 49.93, 51.62],
                        [56.61, 46.51, 51.65, 50.03, 52.70],
                        [49.68, 50.83, 49.88, 50.67, 51.67],
                        [52.48, 52.42, 49.67, 49.00, 49.567],
                        [52.11, 50.39, 52.06, 47.79, 52.01],
                        [49.68, 49.13, 49.13, 50.07, 52.57],
                        [69.79, 57.06, 46.63, 79.23, 61.49],
                        [50.43, 52.02, 50.57, 57.32, 49.78],
                        [49.68, 48.93, 51.07, 51.27, 50.37]
                    ],
                100: [
                        [],
                        [],
                        [],
                        [],
                        [],
                        [51.43, 48.20, 48.72, 51.28, 49.67], # 0.6
                        [50.97, 50.62, 51.47, 50.67, 48.53],
                        [66.58, 47.45, 52.3, 45.24, 61.49],
                        [55.52, 51.87, 56.62, 53.77, 51.37],
                        [55.87, 51.67, 49.88, 56.62, 50.27]
                    ],
                200: [
                        [65.23, 74.98, 65.68, 75.02, 75.57],
                        [62.22, 66.42, 62.97, 68.57, 59.47],
                        [57.22, 62.02, 59.56, 57.17, 58.90],
                        [57.22, 55.87, 54.57, 53.37, 54.02],
                        [51.97, 49.77, 50.74, 50.43, 52.83],
                        [51.64, 49.61, 53.73, 49.77, 51.95],
                        [53.52, 55.52, 52.42, 55.22, 52.47],
                        [62.81, 52.71, 58.95, 47.87, 64.61],
                        [63.37, 62.27, 58.97, 62.62, 62.57],
                        [68.87, 67.11, 70.11, 67.37, 67.07],
                ],
                1600: [
                        [92.81, 91.56, 88.87, 84.37, 80.72],
                        [78.86, 72.76, 74.51, 75.81, 86.81],
                        [55.38, 66.10, 70.38, 57.28, 68.88],
                        [56.42, 56.72, 56.52, 57.57, 53.42],
                        [51.15, 48.75, 49.97, 51.45, 52.58],
                        [53.88, 47.84, 52.16, 49.92, 54.56],
                        [63.17, 64.27, 56.12, 51.67, 58.77],
                        [77.01, 82.18, 81.77, 73.15, 73.32],
                        [84.16, 81.46, 80.01, 78.41, 82.36],
                        [80.1, 92.45, 93.65, 85.26, 89.26]
                    ]
            },
            # Done
            "1": {
                1600: [
                        [83.22, 82.67, 84.87, 77.72, 79.77],
                        [75.36, 76.01, 75.46, 65.62, 75.21],
                        [67.21, 64.81, 69.60, 65.09, 71.05],
                        [60.83, 55.47, 53.97, 60.07, 59.37],
                        [52.53, 54.06, 51.10, 51.25, 51.15],
                        [53.67, 50.96, 48.31, 53.0, 49.20],
                        [50.67, 51.72, 55.42, 54.82, 52.37],
                        [71.59, 46.31, 71.43, 57.72, 60.34],
                        [55.22, 58.12, 53.92, 56.97, 54.77],
                        [61.22, 55.82, 51.02, 56.17, 49.98]
                ],
                # 100: [
                #     [51.8, 51.9, 49.92, 51.49, 52.74], # 0.6
                #     [50.07, 52.67, 51.37, 51.47, 54.47], # 0.7
                #     [49.92, 34.65, 48.69, 32.35, 74.06],  # 0.8
                #     [56.52, 52.27, 56.37, 47.58, 57.57], # 0.9
                #     [54.32, 53.27, 50.03, 50.03, 57.37] # 1.0
                # ]
            },
            # Done
            "2": {
                1600: [
                        [82.12, 80.57, 79.72, 76.12, 83.12],
                        [74.36, 76.66, 80.61, 82.76, 74.21],
                        [65.76, 65.03, 63.08, 63.97, 59.17],
                        [58.57, 60.02, 60.42, 60.62, 59.62],
                        [50.38, 53.19, 53.45, 51.71, 53.96],
                        [49.40, 53.83, 51.54, 54.66, 53.99],
                        [58.62, 57.57, 58.32, 57.02, 59.07],
                        [71.10, 58.13, 73.81, 50.25, 40.97],
                        [74.76, 76.06, 74.61, 71.36, 73.86],
                        [72.21, 81.51, 88.26, 87.00, 87.86]
                ]
            },
            # Done
            "3": {
                1600: [
                        [75.22, 71.98, 69.13, 74.48, 73.78],
                        [68.22, 68.27, 69.47, 69.27, 68.67],
                        [75.22, 71.98, 69.13, 74.48, 73.78],
                        [60.22, 59.12, 57.17, 59.77, 60.52],
                        [55.03, 53.65, 54.88, 53.09, 51.25],
                        [52.94, 51.59, 55.60, 51.33, 53.15],
                        [60.82, 50.02, 51.67, 59.07, 61.07],
                        [81.53, 45.16, 61.82, 77.59, 46.88],
                        [70.81, 49.98, 70.51, 68.47, 70.86],
                        [75.013, 76.76, 70.91, 72.61]
                ]
            },
            # Done
            "4": {
                1600: [
                        [75.27, 72.73, 73.24, 73.38, 72.48],
                        [70.72, 72.26, 68.67, 49.98, 69.42],
                        [64.08, 66.31, 64.14, 66.37, 63.75],
                        [56.57, 50.03, 50.18, 56.12, 55.27],
                        [53.34, 52.22, 51.45, 51.40, 50.03],
                        [48.31, 50.55, 48.36, 51.02, 49.09],
                        [53.07, 52.97, 53.82, 50.03, 55.47],
                        [72.33, 59.20, 48.85, 71.26, 44.83],
                        [67.67, 65.32, 63.02, 64.12, 66.47],
                        [63.87, 66.67, 63.57, 66.37, 71.36]
                ]
            },
            # Done
            "5": {
                1600: [
                        [68.18, 70.18, 67.78, 70.43, 70.18],
                        [64.1, 62.62, 61.57, 60.67, 65.17],
                        [59.34, 59.62, 60.12, 58.73, 60.40],
                        [54.72, 54.47, 54.97, 53.52, 56.32],
                        [52.22, 51.71, 52.83, 52.58, 51.25],
                        [52.01, 52.16, 51.90, 51.38, 50.91],
                        [54.02, 53.57, 54.92, 53.52, 53.67],
                        [60.10, 56.65, 46.80, 74.47],
                        [59.12, 56.22, 59.17, 58.97, 59.22],
                        [61.77, 57.17, 56.47, 58.32, 57.82]
                ]
            },
            # Done
            "6": {
                1600: [
                        [71.08, 69.28, 68.43, 70.38, 66.83],
                        [64.7, 65.67, 63.62, 64.72, 66.72],
                        [56.72, 49.19, 56.78, 57.0, 57.06],
                        [52.22, 52.42, 52.92, 55.42, 49.98],
                        [50.13, 51.61, 51.66, 51.61, 51.05],
                        [47.84, 50.91, 51.85, 47.84, 50.81],
                        [53.02, 53.62, 49.98, 52.17, 52.62],
                        [49.75, 34.15, 70.20, 48.60, 57.06],
                        [58.42, 56.27, 58.92, 54.12, 57.32],
                        [61.92, 64.12, 60.62, 60.47, 59.37]
                ]
            },
            # Done
            "7": {
                1600: [
                        [49.95, 50.0, 50.0, 50.0, 50.5],
                        [50.02, 50.02, 50.18, 49.98, 49.98],
                        [46.51, 44.17, 55.83, 44.17, 55.83],
                        [50.03, 49.98, 49.98, 49.98, 50.03],
                        [48.90, 51.10, 51.10, 49.21, 50.64],
                        [48.462, 47.84, 51.49, 48.20, 52.16],
                        [49.98, 50.03, 49.98, 49.98, 50.08],
                        [59.85, 82.18, 66.34, 79.23],
                        [49.98, 52.38, 50.03, 50.03, 50.28],
                        [49.98, 49.98, 49.98, 50.03, 49.98]
                ]
            },
            # Done
            "8": {
                1600: [
                        [50.0, 50.0, 50.0, 50.0, 50.0],
                        [50.03, 50.03, 50.03, 49.98, 49.98],
                        [55.83, 44.17, 44.17, 55.83, 44.17],
                        [49.98, 49.98, 49.98, 49.98, 49.98],
                        [51.1, 48.90, 48.90, 48.902, 51.1],
                        [52.16, 52.16, 52.16, 47.84, 47.84],
                        [50.02, 49.98, 50.03, 49.98, 50.03],
                        [82.18, 82.18, 17.82, 82.18, 82.18],
                        [49.98, 49.98, 49.98, 50.02, 50.02],
                        [49.98, 49.98, 49.98, 50.025, 49.98]
                ]
            },
            "first 2": {
                # 10: [
                #         [50.5, 49.45, 60.44, 50, 49.55],
                #         [49.12, 50.23, 49.23, 50.47, 50.13],
                #         [50.98, 50.16, 53.54, 54.38, 51.09],
                #         [50.32, 51.97, 48.68, 51.97, 49.93],
                #         [47.93, 51.15, 51.2, 49.11, 50.59],
                #         [],
                #         [],
                #         []
                # ],
                # 20: [
                #         [52, 51.5, 58.14, 49.65, 50.55],
                #         [49.28, 51.27, 49.58, 50.97, 48.83],
                #         [49.42, 51.81, 50.98, 54.54, 53.82],
                #         [],
                #         []
                # ],
                # 50: [
                #         [53.1, 51.55, 52.6, 59.14, 52.95],
                #         [52.07, 50.42, 49.38, 57.62, 51.77],
                #         [53.49, 53.93, 50.47, 52.20, 47.74],
                #         [49.23, 50.32, 52.22, 48.53, 50.67],
                #         [50.49, 49.72, 51.45, 51.25, 50.28],
                # ],
                100: [
                    [58.34, 63.59, 66.93, 65.38, 61.54],
                    [54.42, 53.32, 53.77, 55.77, 58.62],
                    [47.07, 60.57, 53.26, 52.54, 63.19],
                    [50.38, 51.62, 50.87, 49.88, 53.42],
                    [50.38, 50.69, 51.35, 52.02, 49.31],
                    [49.09, 51.07, 50.13, 50.18, 52.74],
                    [50.47, 50.37, 50.73, 49.98, 51.22],
                    [46.56, 46.22, 64.04, 47.95, 45.65],
                    [50.18, 54.38, 49.88, 48.63, 51.87],
                    [55.57, 58.72, 54.52, 53.72, 53.97],
                ],
                200: [
                    [69.73, 73.33, 69.48, 70.83, 75.87],
                    [64.42, 67.47, 67.57, 68.52, 60.47],
                    [59.40, 55.61, 59.17, 52.98, 59.01],
                    [51.62, 50.48, 51.32, 54.62, 53.22],
                    [48.09, 51.45, 52.43, 52.43, 47.27],
                    [50.60, 48.67, 50.29, 50.39, 49.61],
                    [51.32, 53.47, 51.42, 52.17, 54.22],
                    [66.58, 48.03, 66.09, 60.92, 76.52],
                    [57.52, 52.77, 55.67, 56.57, 56.32],
                    [56.87, 53.67, 55.52, 56.47, 54.17],
                ],
                1600: [
                    [84.92, 85.76, 90.67, 79.37, 89.61],
                    [74.46, 71.86, 79.81, 82.0, 79.16],
                    [68.94, 63.02, 57.78, 68.66, 51.09],
                    [57.12, 55.32, 57.52, 57.72, 56.67],
                    [51.61, 52.19, 51.71, 53.91, 51.35],
                    [53.52, 48.88, 51.43, 52.32, 48.20],
                    [58.27, 57.92, 55.02, 55.32, 51.24],
                    [76.61, 61.99, 72.09, 52.3, 59.44],
                    [73.96, 69.51, 67.31, 72.81, 78.91],
                    [85.31, 56.67, 63.62, 74.26, 72.81]
                ]
            }
        }

    focus_n = 100
    for n, v1 in raw_data.items():
        if focus_n not in v1:
            continue
        v2 = v1[focus_n]
        for i in range(len(v2)):
            for j in range(len(v2[i])):
                data.append([categories[i], v2[i][j], n])

    df = pd.DataFrame(data, columns=columns)
    print(df.groupby(r"$n$").agg(["mean", "std"]))
    sns_plot = sns.boxplot(x=columns[0], y=columns[1], hue=columns[2],
                           data=df, showfliers=False)

    if args.novtitle:
        plt.ylabel("", labelpad=0)

    # Accuracy range, with space to show good performance
    sns_plot.set(ylim=(45, 101))

    # Add dividing line in centre
    lower, upper = plt.gca().get_xlim()
    midpoint = (lower + upper) / 2
    plt.axvline(x=midpoint, color='white' if args.darkplot else 'black',
                linewidth=1.0, linestyle='--')

    # Map range to numbers to be plotted
    targets_scaled = range(int((upper - lower)))
    # plt.plot(targets_scaled, baselines, color='C1', marker='x', linestyle='--')

    if not args.legend:
        plt.legend([],[], frameon=False)

    # Make sure axis label not cut off
    plt.tight_layout()

    sns_plot.figure.savefig("./meta_boxplot_varying_n_%s.png" % args.filter)
