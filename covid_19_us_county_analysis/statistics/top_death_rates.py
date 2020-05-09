from covid_19_us_county_analysis.dataframes.deaths import death_df
import pandas as pd


def deaths_per_100k_dataframe(minimum_population: int = 1,
                              include_ny_nj: bool = True) -> pd.DataFrame:
    """
    A function for generating a dataframe of the top 10 US counties sorted in
    descending order by the number of deaths per 100k county residents.
    :param minimum_population: the minimum county population to filter by
    :type minimum_population: int
    :param include_ny_nj: a boolean value to filter out NY counties
    :type include_ny_nj: bool
    :return: a dataframe of the top 10 US counties
    :rtype: pd.DataFrame
    """
    data = death_df[death_df['Admin2'].notna()]
    mask = ~(
        data['Admin2'].str.contains('unassigned|out of|fci|mdoc', case=False,
                                    na=False)) & (
                   data['Population'] >= minimum_population)
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
            'County Population: ' + data['Population'].apply(
                lambda x: f'{x:,}'))
    sorted_data = data.sort_values(by='deaths_per_100k', ascending=False)[
        ['full_county_name', 'latest_date', 'deaths_per_100k', 'text']]
    if include_ny_nj:
        return sorted_data.head(10)
    return sorted_data[~(sorted_data['full_county_name'].str.contains(
        'New York|New Jersey'))].head(10)
