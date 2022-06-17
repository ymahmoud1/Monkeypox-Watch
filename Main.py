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

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv'
    output = 'mp_updated_data.csv'
    urllib.request.urlretrieve(url,output)
    mp_data = pd.read_csv(output)
    conf_cases = mp_data[mp_data['Status'] == 'confirmed']
    fig1 = px.bar(conf_cases.groupby('Country').count().reset_index(), x='Country', y='ID',
                  title='Confirmed Cases in Countries (Figure 1)', labels={'ID': 'Total Cases'}, text_auto=True)
    fig2 = px.line(conf_cases.groupby('Date_confirmation').count().reset_index(),
                   x='Date_confirmation', y='ID', title='Daily Infections',
                   labels={'ID': 'Confirmed Cases', 'Date_confirmation': 'Date'}, markers=True)
    fig1.show()
    fig2.show()
