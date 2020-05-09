import pandas as pd

deaths_url = ("https://github.com/CSSEGISandData/COVID-19/raw/master/"
              "csse_covid_19_data/csse_covid_19_time_series/"
              "time_series_covid19_deaths_US.csv")

death_df = pd.read_csv(deaths_url)

mask = (death_df['Admin2'].notna()) & (
        death_df['Province_State'] != 'District of Columbia')

states = sorted(death_df[mask]['Province_State'].unique())
