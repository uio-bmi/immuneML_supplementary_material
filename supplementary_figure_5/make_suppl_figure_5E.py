from util import draw_rocs, make_roc_curve


def main():
    """
    Makes plots showing area under the ROC curve for use case 2 of the immuneML manuscript. Plots separate figures for three different
    datasets (for epitopes AVFDRKSDAK, KLGGALQAK, and GILGFVFTL) where the methods were compared.

    All figures were made using the Plotly library (https://plotly.com/).
    """

    # where the predictions for different epitopes and methods are stored (as provided by immuneML):
    paths = {"AVFDRKSDAK": ["data/tcrdist_test_predictions_AVFDRKSDAK.csv", "data/cnn_test_predictions_AVFDRKSDAK.csv",
                            "data/logreg_test_predictions_AVFDRKSDAK.csv"],
             "GILGFVFTL": ["data/tcrdist_test_predictions_GILGFVFTL.csv", "data/cnn_test_predictions_GILGFVFTL.csv",
                           "data/logreg_test_predictions_GILGFVFTL.csv"],
             "KLGGALQAK": ["data/tcrdist_test_predictions_KLGGALQAK.csv", "data/cnn_test_predictions_KLGGALQAK.csv",
                           "data/logreg_test_predictions_KLGGALQAK.csv"]}

    # methods that were compared:
    names = ["TCRdist", "CNN", "logreg"]

    for epitope in paths.keys():
        data = []
        for predictions_path in paths[epitope]:
            roc = make_roc_curve(predictions_path=predictions_path, label_name=f"{epitope}_true_class", proba_name=f"{epitope}_True_proba")
            data.append(roc)

        draw_rocs(data=data,
                  labels=[names[i] + f" (AUROC = {round(data[i]['AUC'], 2)})" for i, path in enumerate(paths[epitope])],
                  result_path="./figures/", figure_name=f"figure_{epitope}.html", legend_title=f"{epitope}-specific vs naive TCRs")


if __name__ == "__main__":
    main()
