## COVID-19 US County Analysis

A web-based application that utilizes the most recent 
data available from the COVID-19 Data 
[Repository](https://github.com/CSSEGISandData/COVID-19) by the Center for 
Systems Science and Engineering (CSSE) at Johns Hopkins University.
The application allows one to explore US covid-19 data
visually on a map and with various other plots at the county level.
An example of the deployed application can be found
[here](https://covid-19-us-county-analysis.herokuapp.com). Shout out to 
the creators of [Streamlit](https://docs.streamlit.io) 
for making it easy to build a web application for data 
science.


### Quick start

* Clone the repo: ```git clone https://github.com/kvanderveen/covid_19_us_county_analysis.git```
* cd into the directory: ```cd covid_19_us_county_analysis/```
* Install the requirements: ```pip install -r requirements.txt```
* Run the application: ```streamlit run app.py```

### What's included

Within the download you'll find the following directories and files.

```
covid_19_us_county_analysis/
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── covid_19_us_county_analysis
│   ├── __init__.py
│   ├── dataframes
│   │   ├── __init__.py
│   │   ├── cases.py
│   │   └── deaths.py
│   ├── mapping
│   │   ├── __init__.py
│   │   ├── map_cases.py
│   │   └── map_deaths.py
│   ├── page_content
│   │   ├── __init__.py
│   │   └── content.py
│   ├── page_data
│   │   ├── __init__.py
│   │   └── data.py
│   ├── plotting
│   │   ├── __init__.py
│   │   ├── plot_deaths.py
│   │   ├── plot_state_deaths.py
│   │   └── plot_weekly_change.py
│   └── statistics
│       ├── __init__.py
│       ├── top_death_rates.py
│       ├── top_death_rates_by_state.py
│       └── top_growing_counties.py
├── requirements.txt
└── setup.sh
```

### Creators
##### Kevin Vanderveen
* https://github.com/kvanderveen

