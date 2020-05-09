from covid_19_us_county_analysis.dataframes.deaths import death_df
import pandas as pd


def state_deaths_per_100k_dataframe(state: str) -> pd.DataFrame:
    """
    A function for generating a dataframe of the top 10 counties sorted in
    descending order filtered by a state.
    :param state: the state of interest
    :type state: str
    :return: a dataframe of the top 10 US counties
    :rtype: pd.DataFrame
    """
    data = death_df[death_df['Admin2'].notna()]
    mask = (
        (data['Province_State'] == state) &
        ~(data['Admin2'].str.contains('unassigned|out of|fci|mdoc', case=False))
        & (data['Population'] > 0)
    )
    data = data[mask]
    data['latest_date'] = data.iloc[:, -1]
    data['deaths_per_100k'] = data['latest_date'].div(data['Population']).mul(
        100000).round(1)
    data['full_county_name'] = data['Admin2'] + ', ' + data['Province_State']
    data['text'] = (
            'County: ' + data['full_county_name'] + '<br>' +
            'Deaths per 100k: ' + data['deaths_per_100k'].apply(
                lambda x: f'{x:,}') + '<br>' +
            'Deaths: ' + data['latest_date'].apply(
                lambda x: f'{x:,}') + '<br>' +
            'County Population: ' + data['Population'].apply(lambda x: f'{x:,}'))
    sorted_data = data.sort_values(by='deaths_per_100k', ascending=False)[
        ['Admin2', 'latest_date', 'deaths_per_100k', 'text']]
    return sorted_data[sorted_data['deaths_per_100k'] > 0].head(15)
