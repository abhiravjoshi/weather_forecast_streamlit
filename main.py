import streamlit as st
import matplotlib.pyplot as plt

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
