import plotly.graph_objects as go
from covid_19_us_county_analysis.dataframes.cases import case_df

public_token = 'pk.eyJ1IjoidmFuZGVydmVlbjYwNjExIiwiYSI6ImNrOWZzNzVpazBnMWUzZm' \
               '80NGJpaXNxeHEifQ.rqXDV922WXypN6RO7UaJgQ'

population_dict = {1: 0, 10: 5, 100: 10, 500: 15, 1000: 20, 5000: 25, 10000: 30,
                   25000: 45, 50000: 40}


def calculate_size(x):
    for count, size in population_dict.items():
        if x < count:
            return size
    return 100


def case_dataframe(days=0):
    """
    A function for generating a dataframe containing the necessary data for
    the create_case_map function.
    :param days: the number of days from the first documented covid-19 case
    in the US
    :type days: int
    :return: a pandas dataframe
    :rtype: pd.DataFrame
    """
    mask = ((case_df.iloc[:, 11 + days] > 0) & ~(
        case_df['Admin2'].str.contains('unassigned|fci|mdoc|out of', case=False,
                                       na=False)))
    data = case_df[mask]
    data['text'] = (
            data['Admin2'] + ' County, ' + data['Province_State'] + '<br>' +
            'Case Count: ' + data.iloc[:, 11 + days].apply(lambda x: f'{int(x):,}'))
    return data


def case_map(days=0):
    """
    A function for generating a plotly scattermapbox figure containing points
    that represent US counties with associated covid-19 case data.
    :param days: the number of days from the first documented covid-19 case
    :type days: int
    :return: a plotly figure object
    :rtype: go.Figure
    """
    data = case_dataframe(days)
    opacity = 0.2 if data.shape[0] > 30 else 0.8
    fig = go.Figure(
        go.Scattermapbox(lat=data['Lat'], lon=data['Long_'], mode='markers',
                         marker=go.scattermapbox.Marker(
                             size=data.iloc[:, 11 + days].apply(calculate_size),
                             opacity=opacity, color="red"), text=data['text'],
                         hoverinfo='text'))
    fig.update_layout(autosize=True, hovermode='closest',
                      mapbox=dict(accesstoken=public_token,
                                  center=dict(lat=41, lon=-95), zoom=3),
                      height=700, width=1000)
    return fig
