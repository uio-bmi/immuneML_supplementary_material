import pandas as pd

from util import make_roc_curve, draw_rocs


def main():
    """
    Makes figure 2B from the immuneML manuscript showing the performance (AUC = area under the ROC curve)
    for different dataset sizes. The csv files with roc curve data were provided by immuneML as a part of the
    use case. Full results are available at https://doi.org/10.11582/2021.00008.
    """
    roc_curve_50_data_path = "./data/2B/roc_curve_data_cmv2017_50 (AUC = 0.56).csv"
    roc_curve_100_data_path = "./data/2B/roc_curve_data_cmv2017_100 (AUC = 0.46).csv"
    roc_curve_200_data_path = "./data/2B/roc_curve_data_cmv2017_200 (AUC = 0.51).csv"
    roc_curve_400_data_path = "./data/2B/roc_curve_data_cmv2017_400 (AUC = 0.86).csv"

    # compute roc curve data from predictions available from the CMV status prediction replication run
    predictions_path = "./data/2B/test_predictions_cohort_2.csv"
    roc_curve_686_data = make_roc_curve(predictions_path, "CMV_true_class", "CMV_True_proba")

    result_path = "figures/"

    draw_rocs([roc_curve_686_data, pd.read_csv(roc_curve_400_data_path).to_dict("list"), pd.read_csv(roc_curve_200_data_path).to_dict("list"),
               pd.read_csv(roc_curve_100_data_path).to_dict("list"),
               pd.read_csv(roc_curve_50_data_path).to_dict("list")], [f"full dataset (AUC = {round(roc_curve_686_data['AUC'], 2)})",
                                                                      "400 subjects (AUC = 0.86)",
                                                                      "200 subjects (AUC = 0.51)", "100 subjects (AUC = 0.46)",
                                                                      "50 subjects (AUC = 0.56)"], result_path, figure_name="figure_2B.html")


if __name__ == "__main__":
    main()
