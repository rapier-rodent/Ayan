import streamlit as st
from datetime import datetime
from vedicastro import VedicAstro
import swisseph as swe
import os

# Set the path to the ephemeris files
swe.set_ephe_path('./ephemeris')

def calculate_krishnamurti_ayanamsa():
    try:
        # Get the current date and time
        now = datetime.utcnow()

        # Define the parameters for the calculation
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        utc = "0:00"
        latitude = 0.0  # Set the actual latitude
        longitude = 0.0  # Set the actual longitude
        ayanamsa = "Krishnamurti"

        # Create an instance of VedicHoroscopeData
        horoscope = VedicAstro.VedicHoroscopeData(year, month, day, hour, minute, second, utc, latitude, longitude, ayanamsa)

        # Generate the chart
        chart = horoscope.generate_chart()

        # Get the ayanamsa value
        ayanamsa_value = horoscope.get_ayanamsa()

        return ayanamsa_value
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app
st.title("Krishnamurti Ayanamsa Calculator")
if st.button("Calculate Ayanamsa for Today"):
    ayanamsa_value = calculate_krishnamurti_ayanamsa()
    if ayanamsa_value is not None:
        st.write(f"Krishnamurti Ayanamsa for today: {ayanamsa_value}")
