import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go


def _make_dataframe(df) -> pd.DataFrame:
    x, y = [], []
    for hp_setting in df['hp_setting'].unique():
        x.append("0." + hp_setting.split("enc")[1].split("_ml")[0])
        y.append(df[df['hp_setting'] == hp_setting]['auc'].mean())

    return pd.DataFrame({"x": x, "y": y})


def make_suppl_figure_4B(result_path: str, row_col_names, overlap_matrix):
    """Plot overlap of disease-associated TCRB sequences in CV splits"""
    figure = ff.create_annotated_heatmap(z=overlap_matrix[::-1], x=row_col_names, y=row_col_names[::-1], annotation_text=overlap_matrix[::-1], colorscale=px.colors.sequential.Teal)
    figure_path = f"{result_path}suppl_fig_4B.html"
    figure.write_html(figure_path)


def make_suppl_figure_4D(result_path: str, test_performance_df, training_performance_df):
    """Plot area under the ROC curve over p-value thresholds in training and test data"""
    training_dataframe = _make_dataframe(training_performance_df)
    test_dataframe = _make_dataframe(test_performance_df)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=training_dataframe['x'].values, y=training_dataframe["y"].values, name="CV performance", mode="markers", marker_size=11, marker_color="#CC79A7",
                   opacity=0.6))
    fig.add_trace(go.Scatter(x=test_dataframe["x"], y=test_dataframe["y"], name="test performance", mode="markers", marker_size=11, marker_color="#009E73",
                             opacity=0.6))
    fig.update_layout(template="plotly_white")
    fig.update_xaxes(title_text='p-value threshold')
    fig.update_xaxes(type='category')
    fig.update_yaxes(title_text=f"performance (AUROC)")
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        font=dict(size=18)
    ))

    file_path = f"{result_path}suppl_fig_4D.html"
    fig.write_html(file_path)


def main():
    """
    Makes figures 4B and 4D for supplementary figure 4 of the immuneML manuscript.
    Supplementary figures 4A and 4C are directly provided by immuneML.
    Plots are made with Plotly library (https://plotly.com/).

    All of these figures can now be obtained directly from immuneML as well.
    """

    result_path = "./figures/"

    make_suppl_figure_4B(result_path, [f"CV split {i}" for i in range(1, 11)],
                         pd.read_csv("./data/4B/sequence_overlap_CMV_selection_1_split.csv", index_col=0).values)

    make_suppl_figure_4D(result_path, pd.read_csv("./data/4D/CMV_all_assessment_performances.csv"),
                         pd.read_csv("./data/4D/CMV_assessment_split_1_selection_performance.csv"))


if __name__ == "__main__":
    main()
