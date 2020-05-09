from covid_19_us_county_analysis.dataframes.cases import case_df
from covid_19_us_county_analysis.dataframes.deaths import death_df

latest_date = case_df.columns[-1]
week_earlier = case_df.columns[-8]


def growing_cases(minimum_population=1):
    """
    A function for generating a dataframe of the top 10 counties sorted in
    descending order by week over week percentage increase in confirmed
    covid-19 cases.
    :param minimum_population: the minimum population to filter counties
    :type minimum_population: int
    :return: a pandas dataframe of a maximum 10 rows
    :rtype: pd.DataFrame
    """
    data = case_df[case_df['Admin2'].notna()].merge(
        death_df[['FIPS', 'Population']])
    mask = (
        ~data['Admin2'].str.contains('unassigned|out of|fci|mdoc', case=False)
        & (data.loc[:, week_earlier] > 100)
        & (data['Population'] > minimum_population))
    data = data[mask]
    data['week_change'] = data.loc[:, latest_date].sub(
        data.loc[:, week_earlier]).div(data.loc[:, week_earlier]).mul(
        100).round(1)
    data['full_county_name'] = data['Admin2'] + ', ' + data['Province_State']
    data['text'] = (
            'County: ' + data['full_county_name'] + '<br>' +
            'Population: ' + data['Population'].apply(lambda x: f'{x:,}') +
            '<br>' +
            'Week Over Week Change: ' + data['week_change'].astype(str) + '%' +
            '<br>' +
            'Cases Last Week: ' + data[week_earlier].astype(str) + '<br>' +
            'Latest Cases: ' + data[latest_date].astype(str)
    )
    sorted_data = data.sort_values(by='week_change', ascending=False)
    print(sorted_data.columns)
    return sorted_data[['full_county_name', 'text', 'week_change', week_earlier,
                        latest_date]].head(10)
