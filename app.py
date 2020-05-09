import streamlit as st
from covid_19_us_county_analysis.mapping.map_cases import case_map
from covid_19_us_county_analysis.mapping.map_deaths import death_map
from covid_19_us_county_analysis.dataframes.cases import case_df
from covid_19_us_county_analysis.dataframes.deaths import death_df, states
from covid_19_us_county_analysis.plotting.plot_deaths import plot_deaths
from covid_19_us_county_analysis.plotting.plot_state_deaths import plot_state_deaths
from covid_19_us_county_analysis.page_content.content import page_content
from covid_19_us_county_analysis.page_data.data import page_data
from covid_19_us_county_analysis.plotting.plot_weekly_change import plot_weekly_change
from datetime import date, timedelta


def main():
    generate_intro()
    generate_case_map()
    generate_death_map()
    generate_death_plot()
    generate_state_death_plot()
    generate_weekly_change_plot()
    generate_conclusion()


def generate_intro():
    st.title("COVID-19 US County Analysis")
    st.subheader(page_data.current_date)
    st.markdown(page_content.introduction1)
    st.markdown(page_content.introduction2)


def generate_case_map():
    st.subheader(page_content.case_map_text)
    st.subheader("")
    day_count = st.slider("Days From First Confirmed Case on January 22, 2020",
                          min_value=0, max_value=page_data.max_case_days,
                          key='cases')
    cases = case_df.iloc[:, day_count + 11].sum()
    s = "" if cases == 1 else "s"
    date_str = (date(2020, 1, 22) + timedelta(days=day_count)).strftime(
        "%B %-d, %Y")
    st.markdown(
        f'### {cases:,} cumulative confirmed case{s} in the US on {date_str}')
    map_object = case_map(day_count)
    st.plotly_chart(map_object)


def generate_death_map():
    st.subheader(page_content.death_map_text)
    st.subheader("")
    days = st.slider("Days From First Death on March 1, 2020", min_value=0,
                     max_value=page_data.max_death_days, key="deaths")
    first_death_index = list(death_df.columns).index('3/1/20')
    deaths = death_df.iloc[:, days + first_death_index].sum()
    s = "" if deaths == 1 else "s"
    date_str = (date(2020, 3, 1) + timedelta(days=days)).strftime("%B %-d, %Y")
    st.markdown(
        f'### {deaths:,} cumulative covid-19 death{s} in the US on {date_str}')
    map_object = death_map(days)
    st.plotly_chart(map_object)


def generate_death_plot():
    st.subheader(page_content.death_plot_text)
    populations = ['5,000', '10,000', '25,000', '50,000', '100,000', '500,000',
                   '1,000,000']
    minimum_population = int(st.selectbox('Minimum Population', populations,
                                          key='death_plot').replace(',', ''))
    include_ny_nj = st.checkbox('Include New York and New Jersey counties?',
                                value=True)
    plot = plot_deaths(minimum_population=minimum_population,
                       include_ny_nj=include_ny_nj)
    st.plotly_chart(plot)


def generate_state_death_plot():
    st.subheader(page_content.state_death_plot_text)
    state = st.selectbox('State', states)
    plot = plot_state_deaths(state)
    st.plotly_chart(plot)


def generate_weekly_change_plot():
    populations = ['10,000', '25,000', '50,000', '100,000', '500,000',
                   '1,000,000']
    st.subheader(page_content.weekly_change_plot_text)
    minimum_population = int(st.selectbox('Minimum Population', populations,
                                          key='change_plot').replace(',', ''))
    plot = plot_weekly_change(minimum_population)
    st.plotly_chart(plot)


def generate_conclusion():
    st.markdown(page_content.conclusion)
    st.markdown("-Kevin Vanderveen, MD")


if __name__ == '__main__':
    main()
