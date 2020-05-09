from covid_19_us_county_analysis.dataframes.cases import case_df
from covid_19_us_county_analysis.dataframes.deaths import death_df
from datetime import datetime
from dateutil import tz


class PageData:
    max_case_days = len(case_df.columns) - 12
    max_death_days = (
            len(death_df.columns) - list(death_df.columns).index('3/1/20') - 1)
    current_date = (
        datetime.utcnow().replace(tzinfo=tz.gettz('UTC')).astimezone(
            tz.gettz('America/Denver')).strftime('%B %-d, %Y'))
    latest_data_date = datetime.strptime(case_df.columns[-1],
                                         '%m/%d/%y').strftime('%B %-d, %Y')
    total_cases = case_df.iloc[:, -1].sum()
    total_deaths = death_df.iloc[:, -1].sum()


page_data = PageData()
