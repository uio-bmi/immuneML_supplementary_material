import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score
import plotly.express as px
import plotly.graph_objects as go

# constants:
PLOTLY_BLACK = "#2A3F5E"


# util functions:
def make_roc_curve(predictions_path: str, label_name, proba_name):
    df = pd.read_csv(predictions_path)
    fpr, tpr, _ = roc_curve(y_true=df[label_name].values, y_score=df[proba_name].values)
    return {
        "FPR": fpr,
        "TPR": tpr,
        "AUC": roc_auc_score(true_y=df[label_name].values, predicted_y=df[proba_name].values)
    }


def draw_rocs(data: list, labels: list, result_path: str, figure_name: str = "figure.html", legend_title: str = ""):
    figure = go.Figure()
    colors = px.colors.sequential.Viridis[::2][::-1]

    figure.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='baseline (AUROC = 0.50)', line=dict(color=PLOTLY_BLACK, dash='dash'),
                                hoverinfo="skip"))

    for index, item in enumerate(data):
        figure.add_trace(go.Scatter(x=item["FPR"], y=item["TPR"], mode='lines', name=labels[index], marker=dict(color=colors[index], line=dict(width=3)), hoverinfo="skip"))

    figure.update_layout(template='plotly_white', xaxis_title='false positive rate', yaxis_title='true positive rate')

    figure.update_layout(legend=dict(
        yanchor="bottom",
        y=0.06,
        xanchor="right",
        x=0.99
    ))

    figure.update_layout(font_size=20, legend_title_text=legend_title)

    figure.write_html(result_path + figure_name)

