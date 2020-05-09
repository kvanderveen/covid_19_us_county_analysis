import plotly.graph_objects as go
from covid_19_us_county_analysis.statistics.top_growing_counties import growing_cases


def plot_weekly_change(minimum_population=1) -> go.Figure:
    """
    A function for generating a plotly figure object represented by a bar
    plot of the percent change of covid-19 cases for the 10 counties filtered
    by a minimum population.
    :param minimum_population: the minimum population of counties to filter
    :type minimum_population: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = growing_cases(minimum_population)
    fig = go.Figure(data=[
        go.Bar(x=data['full_county_name'], y=data['week_change'], name='',
               marker={'color': 'red', 'opacity': 0.5}, text=data['text'],
               hoverinfo='text')],
        layout=go.Layout(yaxis={'title': 'Week over Week Increase (%)'},
                         xaxis={'title': 'County'},
                         title=f'Week over Week Case Increase in Counties with '
                               f'a Minimum Population of '
                               f'{minimum_population:,}'))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig
