import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")

place = st.text_input("Place:", key='text')
forecast = st.slider("Forecast Days",
                     min_value=1, max_value=10,
                     key='slider',
                     help="Select the amount of days you'd like to see "
                         "forecast.")
type_data = st.selectbox("Select Data To View:",
                         ("Temperature", "Sky"),
                         key='select')

if place:
    filtered_data = get_data(place=place, forecast=forecast)
    st.subheader(f"{type_data} in {place} for {forecast} days")
    dates = [dict['dt_txt'] for dict in filtered_data]
    print(dates)
    match type_data:
        case 'Temperature':
            temps = [dict['main']['temp'] / 10 for dict in filtered_data]
            figure = px.line(x=dates, y=temps,
                             labels={'x': 'Date', 'y': 'Temperature (C)'})
        case 'Sky':
            skies = [dict['weather'][0]['main'] for dict in filtered_data]
            figure = px.line(x=dates, y=skies,
                             labels={'x': 'Date', 'y': 'Weather'})
    st.plotly_chart(figure)
