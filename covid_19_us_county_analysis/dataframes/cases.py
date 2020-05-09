import pandas as pd

case_url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/' \
           'csse_covid_19_data/csse_covid_19_time_series/' \
           'time_series_covid19_confirmed_US.csv?raw=true'

case_df = pd.read_csv(case_url)
