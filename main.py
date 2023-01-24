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
    st.subheader(f"{type_data} in {place} for {forecast} days")
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temps = [20, 23, 21]
    temps = [forecast * i for i in temps]
    dates, temps = get_data(place, forecast, type_data)
    if type_data == 'Temperature':
        figure = px.line(x=dates, y=temps,
                         labels={'x':'Date', 'y': 'Temperature (C)'})
    # else:
        # figure = px.bar()
    st.plotly_chart(figure)
