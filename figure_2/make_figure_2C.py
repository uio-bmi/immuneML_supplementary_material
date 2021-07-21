import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def main():
    """
    Makes figure 2C showing the number of CMV-associated TCRB sequences across datasets of
    different sizes. The sequences counts were obtained from immuneML output as a part of use case 1. The sequences selected
    as a part of the optimal model for each split were used.

    Full results are available at: https://doi.org/10.11582/2021.00008
    """
    data = {"full dataset": {"seqs": [539], "p-value": 0.001},
            "400 subjects": {"seqs": [3365, 165, 248, 241, 213], "p-value": [0.01, 0.001]},
            "200 subjects": {"seqs": [64, 73, 1, 0, 57], "p-value": [0.001, 0.00001]},
            "100 subjects": {"seqs": [0, 49, 0, 1, 0], "p-value": [0.00001, 0.001]},
            "50 subjects": {"seqs": [1, 0, 0, 0, 0], "p-value": [0.0001]}}

    figure = go.Figure()

    i = 0
    for key in data:
        figure.add_box(boxpoints='all', name=key, y=data[key]['seqs'], marker_color=px.colors.diverging.Tealrose[i], text=np.median(data[key]['seqs']))
        figure.add_annotation(x=key, y=np.median(data[key]['seqs']), text=str(np.median(data[key]['seqs']).astype(int)), showarrow=False, yshift=15)
        i += 1

    figure.update_layout(yaxis={"title": "number of CMV-associated sequences"}, template='plotly_white', font_size=20)
    figure.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ))

    figure.write_html("./figures/figure_2C.html")


def std(x):
    return x.std()


if __name__ == "__main__":
    main()
