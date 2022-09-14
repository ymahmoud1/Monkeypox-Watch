# Monkeypox-Watch - Welcome!
Welcome to my data visualization app on the spread of the monkeypox virus. This is the first major outbreak of the virus that is being tracked worldwide, and as such data is made available. 
The only issue is that unlike wide spreading pandemics such as COVID, the data on the monkeypox is very limited. 
However, with those limitations in mind, I thought it might still be handy to produce an app that can display the fragmented data in a simple, and easily understood manner. 

You can view the app using this link: https://ymahmoud1-monkeypox-watch-app-1ft3py.streamlitapp.com/

**OR**

You can clone the repository, install all the modules found in the requirements file and then in the directory run the command:
```
streamlit run app.py
```
**UPDATE**: App has slowed down because of the large data set,the app still works but some functionalities might take some time to load! Sorry about the inconvenience, I am working on a fix ASAP!

# The App's Functions

**1. Cases by Country:** This page in the app displays a bar chart of total confirmed cases in each country with at least 1 confirmed case. There is also a metric that shows the total worldwide cases of monkeypox. A table of the ten countries with the most cases is also displayed. Lastly, there is a select-box widget in which a peron can select a country of their choice and recieve three graphs that represent more data on the specific country chosen. The three graphs being: Gender Distribution, Symptoms of Cases, and Daily Cases.

**2. Daily Worldwide Infections:** This page presents a line chart of the daily reported confirmed cases worldwide. It also shows a metric of the last day cases were reported, how many cases were reported that day, and the difference between the report day and the day before it. There is a select box too that displays the last day of reported confirmed cases and the number of confirmed cases for a selected country.

**3. Cases in the United States:** This page holds an interractive U.S map that displays confirmed cases of the virus in each state. It also shows a metric of the total cases in the U.S.

# Data:
[Monkeypox Data](https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv) by Global.health

