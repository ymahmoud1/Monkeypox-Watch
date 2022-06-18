import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import datetime
init_notebook_mode(connected=True)
cf.go_offline()
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

cases = pd.DataFrame({'num': [1, 2, 3], "let": ['a', 'b', 'c']})




# Total cases bar chart
@st.cache(suppress_st_warning=True)
def figure1():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    fig1 = px.bar(cases.groupby('Country').count().reset_index(), x='Country', y='ID',
                  title='Confirmed Cases in Countries (Figure 1)', labels={'ID': 'Total Cases'}, text_auto=True)
    return fig1


# Line chart of daily infections
@st.cache(suppress_st_warning=True)
def figure2():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    fig2 = px.line(cases.groupby('Date_confirmation').count().reset_index(),
                   x='Date_confirmation', y='ID', labels={'ID': 'Confirmed Cases', 'Date_confirmation': 'Date'},
                   markers=True)
    return fig2


# map of U.S infections
@st.cache(suppress_st_warning=True)
def states_fig():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    state_cases = cases.groupby(by=['Country', 'Location']).count().loc['United States'].reset_index()
    us_states = {'AK': 0, 'AL': 0, 'AR': 0, 'AZ': 0, 'CA': 0, 'CO': 0, 'CT': 0,
                 'DC': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'IA': 0, 'ID': 0, 'IL': 0, 'IN': 0,
                 'KS': 0, 'KY': 0, 'LA': 0, 'MA': 0, 'MD': 0, 'ME': 0, 'MI': 0, 'MN': 0, 'MO': 0,
                 'MS': 0, 'MT': 0, 'NC': 0, 'ND': 0, 'NE': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NV': 0, 'NY': 0,
                 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC': 0, 'SD': 0, 'TN': 0, 'TX': 0, 'UT': 0,
                 'VA': 0, 'VT': 0, 'WA': 0, 'WI': 0, 'WV': 0, 'WY': 0
                 }
    state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut",
                   "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois",
                   "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan",
                   "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska",
                   "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon",
                   "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                   "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

    for x in range(len(state_cases['Location'])):
        if 'California' in state_cases['Location'][x]:
            us_states['CA'] = us_states['CA'] + state_cases['ID'][x]
        elif 'Alaska' in state_cases['Location'][x]:
            us_states['AK'] = us_states['AK'] + state_cases['ID'][x]
        elif 'Arkansas' in state_cases['Location'][x]:
            us_states['AR'] = us_states['AR'] + state_cases['ID'][x]
        elif 'Arizona' in state_cases['Location'][x]:
            us_states['AZ'] = us_states['AZ'] + state_cases['ID'][x]
        elif 'Colorado' in state_cases['Location'][x]:
            us_states['CO'] = us_states['CO'] + state_cases['ID'][x]
        elif 'Connecticut' in state_cases['Location'][x]:
            us_states['CT'] = us_states['CT'] + state_cases['ID'][x]
        elif 'District of Columbia' in state_cases['Location'][x]:
            us_states['DC'] = us_states['DC'] + state_cases['ID'][x]
        elif 'Delaware' in state_cases['Location'][x]:
            us_states['DE'] = us_states['DE'] + state_cases['ID'][x]
        elif 'Florida' in state_cases['Location'][x]:
            us_states['FL'] = us_states['FL'] + state_cases['ID'][x]
        elif 'Georgia' in state_cases['Location'][x]:
            us_states['GA'] = us_states['GA'] + state_cases['ID'][x]
        elif 'Hawaii' in state_cases['Location'][x]:
            us_states['HI'] = us_states['HI'] + state_cases['ID'][x]
        elif 'Iowa' in state_cases['Location'][x]:
            us_states['IA'] = us_states['IA'] + state_cases['ID'][x]
        elif 'Idaho' in state_cases['Location'][x]:
            us_states['ID'] = us_states['ID'] + state_cases['ID'][x]
        elif 'Illinois' in state_cases['Location'][x]:
            us_states['IL'] = us_states['IL'] + state_cases['ID'][x]
        elif 'Indiana' in state_cases['Location'][x]:
            us_states['IN'] = us_states['IN'] + state_cases['ID'][x]
        elif 'Kansas' in state_cases['Location'][x]:
            us_states['KS'] = us_states['KS'] + state_cases['ID'][x]
        elif 'Kentucky' in state_cases['Location'][x]:
            us_states['KY'] = us_states['KY'] + state_cases['ID'][x]
        elif 'Louisiana' in state_cases['Location'][x]:
            us_states['LA'] = us_states['LA'] + state_cases['ID'][x]
        elif 'Massachusetts' in state_cases['Location'][x]:
            us_states['MA'] = us_states['MA'] + state_cases['ID'][x]
        elif 'Maryland' in state_cases['Location'][x]:
            us_states['MD'] = us_states['MD'] + state_cases['ID'][x]
        elif 'Maine' in state_cases['Location'][x]:
            us_states['ME'] = us_states['ME'] + state_cases['ID'][x]
        elif 'Michigan' in state_cases['Location'][x]:
            us_states['MI'] = us_states['MI'] + state_cases['ID'][x]
        elif 'Minnesota' in state_cases['Location'][x]:
            us_states['MN'] = us_states['MN'] + state_cases['ID'][x]
        elif 'Missouri' in state_cases['Location'][x]:
            us_states['MO'] = us_states['MO'] + state_cases['ID'][x]
        elif 'Mississippi' in state_cases['Location'][x]:
            us_states['MS'] = us_states['MS'] + state_cases['ID'][x]
        elif 'Montana' in state_cases['Location'][x]:
            us_states['MT'] = us_states['MT'] + state_cases['ID'][x]
        elif 'North Carolina' in state_cases['Location'][x]:
            us_states['NC'] = us_states['NC'] + state_cases['ID'][x]
        elif 'North Dakota' in state_cases['Location'][x]:
            us_states['ND'] = us_states['ND'] + state_cases['ID'][x]
        elif 'Nebraska' in state_cases['Location'][x]:
            us_states['NE'] = us_states['NE'] + state_cases['ID'][x]
        elif 'New Hampshire' in state_cases['Location'][x]:
            us_states['NH'] = us_states['NH'] + state_cases['ID'][x]
        elif 'New Jersy' in state_cases['Location'][x]:
            us_states['NJ'] = us_states['NJ'] + state_cases['ID'][x]
        elif 'New Mexico' in state_cases['Location'][x]:
            us_states['NM'] = us_states['NM'] + state_cases['ID'][x]
        elif 'Nevada' in state_cases['Location'][x]:
            us_states['NV'] = us_states['NV'] + state_cases['ID'][x]
        elif 'New York' in state_cases['Location'][x]:
            us_states['NY'] = us_states['NY'] + state_cases['ID'][x]
        elif 'Ohio' in state_cases['Location'][x]:
            us_states['OH'] = us_states['OH'] + state_cases['ID'][x]
        elif 'Oklahoma' in state_cases['Location'][x]:
            us_states['OK'] = us_states['OK'] + state_cases['ID'][x]
        elif 'Oregon' in state_cases['Location'][x]:
            us_states['OR'] = us_states['OR'] + state_cases['ID'][x]
        elif 'Pennsylvania' in state_cases['Location'][x]:
            us_states['PA'] = us_states['PA'] + state_cases['ID'][x]
        elif 'Rhode Island' in state_cases['Location'][x]:
            us_states['RI'] = us_states['RI'] + state_cases['ID'][x]
        elif 'South Carolina' in state_cases['Location'][x]:
            us_states['SC'] = us_states['SC'] + state_cases['ID'][x]
        elif 'South Dakota' in state_cases['Location'][x]:
            us_states['SD'] = us_states['SD'] + state_cases['ID'][x]
        elif 'Tennessee' in state_cases['Location'][x]:
            us_states['TN'] = us_states['TN'] + state_cases['ID'][x]
        elif 'Texas' in state_cases['Location'][x]:
            us_states['TX'] = us_states['TX'] + state_cases['ID'][x]
        elif 'Utah' in state_cases['Location'][x]:
            us_states['UT'] = us_states['UT'] + state_cases['ID'][x]
        elif 'Virginia' in state_cases['Location'][x]:
            us_states['VA'] = us_states['VA'] + state_cases['ID'][x]
        elif 'Vermont' in state_cases['Location'][x]:
            us_states['VT'] = us_states['VT'] + state_cases['ID'][x]
        elif 'Washington' in state_cases['Location'][x]:
            us_states['WA'] = us_states['WA'] + state_cases['ID'][x]
        elif 'Wisconsin' in state_cases['Location'][x]:
            us_states['WI'] = us_states['WI'] + state_cases['ID'][x]
        elif 'West Virginia' in state_cases['Location'][x]:
            us_states['WV'] = us_states['WV'] + state_cases['ID'][x]
        elif 'Wyoming' in state_cases['Location'][x]:
            us_states['WY'] = us_states['WY'] + state_cases['ID'][x]
    df_states = pd.DataFrame({'States': list(us_states.keys()), 'Cases': list(us_states.values())})
    data = dict(type='choropleth', locations=list(us_states.keys()), locationmode='USA-states',
                z=list(us_states.values()), text=state_names, colorbar={'title': 'Cases'}, colorscale='reds')
    layout = dict(geo={'scope': 'usa'})
    choromap = go.Figure(data=[data], layout=layout)
    return choromap


@st.cache(suppress_st_warning=True)
def value():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    val=int(cases.groupby('Date_confirmation').count().reset_index().iloc[-1]['ID'])
    return val

@st.cache(suppress_st_warning=True)
def delta():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    delt = (int(cases.groupby('Date_confirmation').count().reset_index().iloc[-2]['ID'])
          - int(cases.groupby('Date_confirmation').count().reset_index().iloc[-1]['ID'])) * -1
    return delt

def data_date():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    global cases
    cases = mp_data[mp_data['Status'] == 'confirmed']
    date = pd.to_datetime(cases.groupby('Date_confirmation').count().reset_index().iloc[-1]['Date_confirmation']).strftime('%B %d, %Y')
    return date

# main class

def main():
    # app setup
    # st.set_page_config(layout="wide")
    st.title('Monkeypox - Dashboard')
    st.subheader('A project by Yazan Mahmoud')
    st.sidebar.title("Navigate")
    navigation = st.sidebar.selectbox('To where?',
                                      ("Cases by Country", 'Daily Worldwide Infections', "Cases in the United States"))
    # data vis
    if navigation == 'Cases by Country':
        st.plotly_chart(figure1())
    elif navigation == 'Daily Worldwide Infections':
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.subheader('Daily Worldwide Infections')
            st.plotly_chart(figure2())
        with col3:
            st.metric(label=data_date(),
                      value=value(),
                      delta=delta())

    elif navigation == "Cases in the United States":
        st.plotly_chart(states_fig())


if __name__ == '__main__':
    main()
