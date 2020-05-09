import plotly.graph_objects as go
from covid_19_us_county_analysis.dataframes.deaths import death_df
from datetime import date, timedelta
import pandas as pd

public_token = 'pk.eyJ1IjoidmFuZGVydmVlbjYwNjExIiwiYSI6ImNrOWZzNzVpazBnMWUzZm' \
               '80NGJpaXNxeHEifQ.rqXDV922WXypN6RO7UaJgQ'

population_dict = {1: 0, 10: 5, 50: 10, 100: 15, 500: 20, 1000: 25, 10000: 30,
                   25000: 45, 50000: 40}


def calculate_size(x: int) -> int:
    for count, size in population_dict.items():
        if x < count:
            return size
    return 100


def death_dataframe(days: int = 0) -> pd.DataFrame:
    """
    A function for generating a dataframe containing the necessary data for
    the create_death_map function.
    :param days: the number of days from the first documented covid-19 death
    in the US
    :type days: int
    :return: a pandas dataframe
    :rtype: pd.DataFrame
    """
    first_death_index = list(death_df.columns).index('3/1/20')
    date_str = (date(2020, 3, 1) + timedelta(days=days)).strftime('%B %-d, %Y')
    mask = ((death_df.iloc[:, first_death_index + days] > 0) & ~(
        death_df['Admin2'].str.contains('unassigned|fci|mdoc|out of',
                                        case=False, na=False)))
    data = death_df[mask]
    data['deaths_per_100k'] = data.iloc[:, first_death_index + days].div(
        data['Population']).mul(100000).round(1)
    data['text'] = (
            data['Admin2'] + ' County, ' + data['Province_State'] + '<br>' +
            'Cumulative Deaths: ' +
            data.iloc[:, first_death_index + days].apply(
                lambda x: f'{int(x):,}') + '<br>' +
            'Deaths per 100K: ' + data['deaths_per_100k'].astype(str) + '<br>' +
            date_str
    )
    data['point_size'] = data.iloc[:, first_death_index + days].apply(
        calculate_size)
    return data


def death_map(days: int = 0) -> go.Figure:
    """
    A function for generating a plotly scattermapbox figure containing points
    that represent US counties with associated covid-19 death data.
    :param days: the number of days from the first documented covid-19 death
    :type days: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = death_dataframe(days)
    opacity = 0.2 if data.shape[0] > 30 else 0.8
    fig = go.Figure(
        go.Scattermapbox(lat=data['Lat'], lon=data['Long_'], mode='markers',
                         marker=go.scattermapbox.Marker(size=data['point_size'],
                                                        opacity=opacity,
                                                        color="red"),
                         text=data['text'], hoverinfo='text'))
    fig.update_layout(autosize=True, hovermode='closest',
                      mapbox=dict(accesstoken=public_token,
                                  center=dict(lat=41, lon=-95), zoom=3),
                      height=700, width=1000)
    return fig
