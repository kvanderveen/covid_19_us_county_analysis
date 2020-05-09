import plotly.graph_objects as go
from covid_19_us_county_analysis.statistics.top_death_rates_by_state import \
    state_deaths_per_100k_dataframe


def plot_state_deaths(state: str) -> go.Figure:
    """
    A function for generating a plotly figure object represented by a bar
    plot of the covid deaths per 100k for the top 10 counties of a selected
    state.
    :param state: the state of interest
    :type state: str
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = state_deaths_per_100k_dataframe(state)
    fig = go.Figure(data=[
        go.Bar(x=data['Admin2'], y=data['deaths_per_100k'], name='',
               marker={'color': 'red', 'opacity': 0.5}, text=data['text'],
               hoverinfo='text')],
        layout=go.Layout(yaxis={'title': 'Deaths per 100k'},
                         xaxis={'title': 'County'},
                         title=f'Deaths per 100,000 in {state} Counties'),)
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig
