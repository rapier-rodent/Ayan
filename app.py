import streamlit as st
from datetime import datetime
from vedicastro import VedicAstro

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
        horoscope = VedicAst
