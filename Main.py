import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
import plotly.express as px
import urllib.request 
import streamlit as st


#data collection
url = 'https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv'
output = 'mp_updated_data.csv'
urllib.request.urlretrieve(url,output)
mp_data = pd.read_csv(output)
cases = mp_data[mp_data['Status'] == 'confirmed']

#Total cases bar chart
def figure1():
    fig1 = px.bar(cases.groupby('Country').count().reset_index(), x='Country', y='ID',
                  title='Confirmed Cases in Countries (Figure 1)', labels={'ID': 'Total Cases'}, text_auto=True)
    return fig1

#Line chart of daily infections
def figure2():
    fig2 = px.line(cases.groupby('Date_confirmation').count().reset_index(),
                   x='Date_confirmation', y='ID', title='Daily Infections',
                   labels={'ID': 'Confirmed Cases', 'Date_confirmation': 'Date'}, markers=True)
    return fig2

#main class
def main():
    #app setup
    st.set_page_config(layout="wide")
    st.title('Monkeypox - Dashboard')
    st.markdown('A project by Yazan Mahmoud')
    #data vis
    figure1()
    figure2()
    

if __name__ == '__main__':
    main()
