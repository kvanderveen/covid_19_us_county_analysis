from covid_19_us_county_analysis.page_data.data import page_data


class PageContent:
    introduction1 = (
        f"On January 19, 2020, a 35 year old man walked into an urgent care "
        f"center in Snohomish County, Washington, with a 4-day history of "
        f"cough and fever. He had returned from Wuhan, China 4 days earlier "
        f"after visiting family there. In the days that followed, the CDC "
        f"would confirm that nasopharyngeal and oropharyngeal swab specimens "
        f"obtained from the man tested positive for 2019-nCoV, the novel "
        f"coronavirus that was responsible for a major disease outbreak in "
        f"Wuhan, China. In the weeks and months that followed, over a million "
        f"Americans would test positive for covid-19 and tens of thousands "
        f"would succumb to the disease.")
    introduction2 = (
        f"Early in the course of the pandemic one dashboard emerged as the "
        f"leader for the latest covid-19 statistics updated in real-time, the "
        f"[dashboard](https://gisanddata.maps.arcgis.com/apps/opsdashboard/"
        f"index.html#/bda7594740fd40299423467b48e9ecf6) created by a team at "
        f"Johns Hopkins University. As an open-source project, the team has "
        f"generously made their data publicly available. This "
        f"[data](https://github.com/CSSEGISandData/COVID-19) is used to "
        f"generate the plots and tables on this site. As of "
        f"{page_data.latest_data_date}, covid-19 has resulted in "
        f"{page_data.total_cases:,} confirmed cases and "
        f"{page_data.total_deaths:,} deaths in the US. The code repository "
        f"for this web application can be found [here]"
        f"(https://github.com/kvanderveen/covid_19_us_county_analysis). For "
        f"covid-19 trends at the national, state and county levels, "
        f"this [site](https://analysis-covid-19.herokuapp.com) may be helpful "
        f"(give it a few moments to load).")
    case_map_text = (
        "The following map illustrates the spread of covid-19 across the US.  "
        "To visualize the spread of covid-19 at a particular point in time, "
        "use the slider below to select the number of days from the date the "
        "first case of covid-19 was confirmed (January 22, 2020). The size of "
        "each point on the map is correlated with the number of cumulative "
        "confirmed cases at that location at that moment in time. Hover over "
        "a point to see data associated with that location. The zoom "
        "level can be adjusted for greater detail.")
    death_map_text = (
        "The following map illustrates cumulative deaths due to covid-19 "
        "across the US.  To visualize deaths due to covid-19 at a particular "
        "point in time, use the slider below to select the number of days from "
        "the date the first death from covid-19 was confirmed (March 1, 2020). "
        "The size of each point on the map is correlated with the number of "
        "cumulative deaths at that location at that moment in time. Hover "
        "over a point to see data associated with that location. The zoom "
        "level can be adjusted for greater detail.")
    death_plot_text = (
        "Which US counties have the highest per capita number of deaths due "
        "to covid-19? The following plot provides information about the "
        "number of deaths in  US counties per 100,000 county residents. "
        "Select the minimum  population of counties you wish to examine and "
        "whether or not to  include New York and New Jersey counties. Hover "
        "over a bar to see additional data.")
    state_death_plot_text = (
        "How are the counties in my own state faring? The following plot "
        "provides information about the number of deaths in counties per "
        "100,000 county residents for a selected state. A maximum of 15 "
        "counties are included.  Select the state of interest below. Hover "
        "over a bar to see additional data.")
    weekly_change_plot_text = (
        "Where are confirmed covid-19 cases increasing the most rapidly? The "
        "following plot provides information about US counties with the "
        "greatest week over week increases in cases (measured as a "
        "percentage). To filter by county size, select a minimum population "
        "below. Hover over a bar to see additional data.")
    conclusion = (
        f"There is little doubt this pandemic will continue to increase in "
        f"scope until widespread immunity has developed in communities around "
        f"the world. Based upon past precedent and decades of accumulated "
        f"scientific knowledge, the most rapid and effective way to accomplish "
        f"this while preserving the lives of countless individuals is with a "
        f"vaccine.  To all of the scientists around the world working on "
        f"this problem, here's to you.")


page_content = PageContent()
