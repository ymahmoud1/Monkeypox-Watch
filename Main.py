import pandas as pd
import cufflinks as cf
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
from PIL import Image

nations = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
           'Anguilla', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
           'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
           'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia And Herzegowina',
           'Botswana', 'Bouvet Island', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso',
           'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Rep',
           'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos Islands', 'Colombia', 'Comoros', 'Congo',
           'Cook Islands', 'Costa Rica', 'Cote D`ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
           'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador',
           'Equatorial Guinea',
           'Eritrea', 'Estonia', 'Ethiopia', 'England', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji',
           'Finland' 'France', 'French Guiana', 'French Polynesia', 'French S. Territories', 'Gabon', 'Gambia',
           'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
           'Guatemala', 'Guinea', 'Guinea-bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary',
           'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
           'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
           'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi',
           'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius',
           'Mayotte',
           'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar',
           'Namibia',
           'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua',
           'Niger',
           'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Mariana Islands', 'Northern Ireland', 'Norway',
           'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn',
           'Poland',
           'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts And Nevis',
           'Saint Lucia',
           'St Vincent/Grenadines', 'Samoa', 'San Marino', 'Sao Tome', 'Saudi Arabia', 'Scotland', 'Senegal',
           'Seychelles', 'Sierra Leone', 'Singapore',
           'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain',
           'Sri Lanka', 'St. Helena',
           'St.Pierre', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
           'Tanzania', 'Thailand', 'Togo',
           'Tokelau', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
           'Ukraine', 'United Arab Emirates',
           'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State', 'Venezuela', 'Viet Nam',
           'Virgin Islands (British)',
           'Virgin Islands (U.S.)', 'Wales', 'Western Sahara', 'Yemen', 'Zaire', 'Zambia', 'Zimbabwe']


# a function that extracts and updates the monkeypox data
@st.cache(suppress_st_warning=True)
def data():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    cases = mp_data[mp_data['Status'] == 'confirmed']
    cases.rename(columns={'ID': 'Cases'}, inplace=True)
    return cases


# Total cases bar chart
def figure1():
    fig1 = px.bar(data().groupby('Country').count().reset_index(), x='Country', y='Cases', labels={'ID': 'Total Cases'},
                  text_auto=True)
    fig1.update_layout(width=800, height=500)
    return fig1


# Line chart of daily infections
def figure2():
    fig2 = px.line(data().groupby('Date_confirmation').count().reset_index(),
                   x='Date_confirmation', y='Cases', labels={'ID': 'Confirmed Cases', 'Date_confirmation': 'Date'},
                   markers=True)
    return fig2


# map of U.S infections
def states_fig():
    state_cases = data().groupby(by=['Country', 'Location']).count().loc['United States'].reset_index()
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
            us_states['CA'] = us_states['CA'] + state_cases['Cases'][x]
        elif 'Alaska' in state_cases['Location'][x]:
            us_states['AK'] = us_states['AK'] + state_cases['Cases'][x]
        elif 'Arkansas' in state_cases['Location'][x]:
            us_states['AR'] = us_states['AR'] + state_cases['Cases'][x]
        elif 'Arizona' in state_cases['Location'][x]:
            us_states['AZ'] = us_states['AZ'] + state_cases['Cases'][x]
        elif 'Colorado' in state_cases['Location'][x]:
            us_states['CO'] = us_states['CO'] + state_cases['Cases'][x]
        elif 'Connecticut' in state_cases['Location'][x]:
            us_states['CT'] = us_states['CT'] + state_cases['Cases'][x]
        elif 'District of Columbia' in state_cases['Location'][x]:
            us_states['DC'] = us_states['DC'] + state_cases['Cases'][x]
        elif 'Delaware' in state_cases['Location'][x]:
            us_states['DE'] = us_states['DE'] + state_cases['Cases'][x]
        elif 'Florida' in state_cases['Location'][x]:
            us_states['FL'] = us_states['FL'] + state_cases['Cases'][x]
        elif 'Georgia' in state_cases['Location'][x]:
            us_states['GA'] = us_states['GA'] + state_cases['Cases'][x]
        elif 'Hawaii' in state_cases['Location'][x]:
            us_states['HI'] = us_states['HI'] + state_cases['Cases'][x]
        elif 'Iowa' in state_cases['Location'][x]:
            us_states['IA'] = us_states['IA'] + state_cases['Cases'][x]
        elif 'Idaho' in state_cases['Location'][x]:
            us_states['ID'] = us_states['ID'] + state_cases['Cases'][x]
        elif 'Illinois' in state_cases['Location'][x]:
            us_states['IL'] = us_states['IL'] + state_cases['Cases'][x]
        elif 'Indiana' in state_cases['Location'][x]:
            us_states['IN'] = us_states['IN'] + state_cases['Cases'][x]
        elif 'Kansas' in state_cases['Location'][x]:
            us_states['KS'] = us_states['KS'] + state_cases['Cases'][x]
        elif 'Kentucky' in state_cases['Location'][x]:
            us_states['KY'] = us_states['KY'] + state_cases['Cases'][x]
        elif 'Louisiana' in state_cases['Location'][x]:
            us_states['LA'] = us_states['LA'] + state_cases['Cases'][x]
        elif 'Massachusetts' in state_cases['Location'][x]:
            us_states['MA'] = us_states['MA'] + state_cases['Cases'][x]
        elif 'Maryland' in state_cases['Location'][x]:
            us_states['MD'] = us_states['MD'] + state_cases['Cases'][x]
        elif 'Maine' in state_cases['Location'][x]:
            us_states['ME'] = us_states['ME'] + state_cases['Cases'][x]
        elif 'Michigan' in state_cases['Location'][x]:
            us_states['MI'] = us_states['MI'] + state_cases['Cases'][x]
        elif 'Minnesota' in state_cases['Location'][x]:
            us_states['MN'] = us_states['MN'] + state_cases['Cases'][x]
        elif 'Missouri' in state_cases['Location'][x]:
            us_states['MO'] = us_states['MO'] + state_cases['Cases'][x]
        elif 'Mississippi' in state_cases['Location'][x]:
            us_states['MS'] = us_states['MS'] + state_cases['Cases'][x]
        elif 'Montana' in state_cases['Location'][x]:
            us_states['MT'] = us_states['MT'] + state_cases['Cases'][x]
        elif 'North Carolina' in state_cases['Location'][x]:
            us_states['NC'] = us_states['NC'] + state_cases['Cases'][x]
        elif 'North Dakota' in state_cases['Location'][x]:
            us_states['ND'] = us_states['ND'] + state_cases['Cases'][x]
        elif 'Nebraska' in state_cases['Location'][x]:
            us_states['NE'] = us_states['NE'] + state_cases['Cases'][x]
        elif 'New Hampshire' in state_cases['Location'][x]:
            us_states['NH'] = us_states['NH'] + state_cases['Cases'][x]
        elif 'New Jersy' in state_cases['Location'][x]:
            us_states['NJ'] = us_states['NJ'] + state_cases['Cases'][x]
        elif 'New Mexico' in state_cases['Location'][x]:
            us_states['NM'] = us_states['NM'] + state_cases['Cases'][x]
        elif 'Nevada' in state_cases['Location'][x]:
            us_states['NV'] = us_states['NV'] + state_cases['Cases'][x]
        elif 'New York' in state_cases['Location'][x]:
            us_states['NY'] = us_states['NY'] + state_cases['Cases'][x]
        elif 'Ohio' in state_cases['Location'][x]:
            us_states['OH'] = us_states['OH'] + state_cases['Cases'][x]
        elif 'Oklahoma' in state_cases['Location'][x]:
            us_states['OK'] = us_states['OK'] + state_cases['Cases'][x]
        elif 'Oregon' in state_cases['Location'][x]:
            us_states['OR'] = us_states['OR'] + state_cases['Cases'][x]
        elif 'Pennsylvania' in state_cases['Location'][x]:
            us_states['PA'] = us_states['PA'] + state_cases['Cases'][x]
        elif 'Rhode Island' in state_cases['Location'][x]:
            us_states['RI'] = us_states['RI'] + state_cases['Cases'][x]
        elif 'South Carolina' in state_cases['Location'][x]:
            us_states['SC'] = us_states['SC'] + state_cases['Cases'][x]
        elif 'South Dakota' in state_cases['Location'][x]:
            us_states['SD'] = us_states['SD'] + state_cases['Cases'][x]
        elif 'Tennessee' in state_cases['Location'][x]:
            us_states['TN'] = us_states['TN'] + state_cases['Cases'][x]
        elif 'Texas' in state_cases['Location'][x]:
            us_states['TX'] = us_states['TX'] + state_cases['Cases'][x]
        elif 'Utah' in state_cases['Location'][x]:
            us_states['UT'] = us_states['UT'] + state_cases['Cases'][x]
        elif 'Virginia' in state_cases['Location'][x]:
            us_states['VA'] = us_states['VA'] + state_cases['Cases'][x]
        elif 'Vermont' in state_cases['Location'][x]:
            us_states['VT'] = us_states['VT'] + state_cases['Cases'][x]
        elif 'Washington' in state_cases['Location'][x]:
            us_states['WA'] = us_states['WA'] + state_cases['Cases'][x]
        elif 'Wisconsin' in state_cases['Location'][x]:
            us_states['WI'] = us_states['WI'] + state_cases['Cases'][x]
        elif 'West Virginia' in state_cases['Location'][x]:
            us_states['WV'] = us_states['WV'] + state_cases['Cases'][x]
        elif 'Wyoming' in state_cases['Location'][x]:
            us_states['WY'] = us_states['WY'] + state_cases['Cases'][x]
    datas = dict(type='choropleth', locations=list(us_states.keys()), locationmode='USA-states',
                 z=list(us_states.values()), text=state_names, colorbar={'title': 'Cases'}, colorscale='reds')
    layout = dict(geo={'scope': 'usa'})
    choromap = go.Figure(data=[datas], layout=layout)
    choromap.update_layout(width=900, height=600)
    return choromap


# A list of countries with confirmed monkeypox cases
def with_cases():
    with_mp = data()['Country'].unique()
    return with_mp


# A list of countries with no confirmed monkeypox cases
def no_cases():
    nations_list = nations.copy()
    i = 0
    for z in data().groupby('Country').count().reset_index()['Country']:
        if data().groupby('Country').count().reset_index()['Country'][i] in nations_list:
            nations_list.remove(data().groupby('Country').count().reset_index()['Country'][i])
        i += 1
    return nations_list


# to start working on
# def country_info_graph1(country):


# Number of confirmed daily worldwide cases, used in metric
def value():
    mp_data = pd.read_csv('https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv')
    cases = mp_data[mp_data['Status'] == 'confirmed']
    val = int(data().groupby('Date_confirmation').count().reset_index().iloc[-1]['Cases'])
    return val


# the change in confirmed cases between most recent date and the date before
def delta():
    delt = (int(data().groupby('Date_confirmation').count().reset_index().iloc[-2]['Cases'])
            - int(data().groupby('Date_confirmation').count().reset_index().iloc[-1]['Cases'])) * -1
    return delt


# the date of the most recent batch of confirmed cases
def data_date():
    date = pd.to_datetime(
        data().groupby('Date_confirmation').count().reset_index().iloc[-1]['Date_confirmation']).strftime('%B %d, %Y')
    return date


# main class, creates app and displays data
def main():
    # app setup
    st.set_page_config(layout="wide")
    st.sidebar.title("Navigate")
    navigation = st.sidebar.selectbox('To where?',
                                      ("Home", "Cases by Country", 'Daily Worldwide Infections',
                                       "Cases in the United States"))
    # data vis
    if navigation == 'Home':
        st.title('Monkeypox - Dashboard')
        st.subheader('A project by Yazan Mahmoud')
        st.markdown("Welcome! This app's purpose is to provide people with data visualization of the Monkeypox virus.")
        image = Image.open('app pics/Monkeypox.jpg')
        st.image(image)
    elif navigation == 'Cases by Country':
        st.header('Confirmed Cases in Countries')
        st.plotly_chart(figure1())
        st.subheader('Nations With Most Confirmed Cases')
        st.table(data().groupby('Country').count()['Cases'].sort_values(ascending=False).head(10))
        selected_nation = st.selectbox('Select a country:', (nations))
        if selected_nation in no_cases():
            st.write("This country has no confirmed cases of the monkeypox virus.")
        # Will work on
        # elif selected_nation in with_cases():
    elif navigation == 'Daily Worldwide Infections':
        col3, col4, col5 = st.columns([3, 2, 1])
        with col3:
            st.subheader('Daily Worldwide Infections')
            st.plotly_chart(figure2())
        with col5:
            st.metric(label=data_date(),
                      value=value(),
                      delta=delta())

    elif navigation == "Cases in the United States":
        st.header('Number of Cases in Every State')
        st.plotly_chart(states_fig())


if __name__ == '__main__':
    main()
