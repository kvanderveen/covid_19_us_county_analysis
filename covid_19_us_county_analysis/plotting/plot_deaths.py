from covid_19_us_county_analysis.statistics.top_death_rates import \
    deaths_per_100k_dataframe
import plotly.graph_objects as go


def plot_deaths(minimum_population: int = 1,
                include_ny_nj: bool = True) -> go.Figure:
    """
    A function for generating a plotly figure object represented by a bar
    plot of the covid deaths per 100k for the top 10 US counties.
    :param minimum_population: the minimum county population to filter by
    county population
    :type minimum_population: int
    :param include_ny_nj: a boolean value to filter out NY counties
    :type include_ny_nj: bool
    :return: a plotly figure object
    :rtype: go.Figure
    """
    ny = '' if include_ny_nj else '<br>(New York and New Jersey not included)'
    data = deaths_per_100k_dataframe(minimum_population, include_ny_nj)
    fig = go.Figure(data=[
        go.Bar(x=data['full_county_name'], y=data['deaths_per_100k'], name='',
               marker={'color': 'red', 'opacity': 0.5}, text=data['text'],
               hoverinfo='text')],
        layout=go.Layout(yaxis={'title': 'Deaths per 100k'},
                         xaxis={'title': 'County'},
                         title=f'Top 10 Death Rates Among US Counties with a '
                               f'Population of '
                               f'{minimum_population:,} or More{ny}'))
    fig.update_layout(height=600, width=900, showlegend=False)
    return fig
