import streamlit as st
import requests

# Streamlit app title
st.title("Krishnamurti Ayanamsa Calculator")

# User inputs for date, time, and location
st.header("Input Details")

year = st.number_input("Year", min_value=1900, max_value=2100, value=2024)
month = st.number_input("Month", min_value=1, max_value=12, value=8)
day = st.number_input("Day", min_value=1, max_value=31, value=5)
hour = st.number_input("Hour (UTC)", min_value=0, max_value=23, value=12)
minute = st.number_input("Minute (UTC)", min_value=0, max_value=59, value=0)
second = st.number_input("Second (UTC)", min_value=0, max_value=59, value=0)
utc = st.selectbox("UTC Timezone", ["UTC", "GMT", "IST", "PST", "EST"])
latitude = st.number_input("Latitude", format="%.6f", value=0.0)
longitude = st.number_input("Longitude", format="%.6f", value=0.0)

# Button to calculate Ayanamsa
if st.button("Calculate Krishnamurti Ayanamsa"):
    # Prepare the input data for the API call
    input_data = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
        "utc": utc,
        "latitude": latitude,
        "longitude": longitude,
        "ayanamsa": "Krishnamurti",
        "house_system": "Placidus"
    }

    # Call the API to get the horary data
    response = requests.post("http://127.0.0.1:8088/get_all_horary_data", json=input_data)

    if response.status_code == 200:
        data = response.json()
        ayanamsa_value = data.get("planets_data", [])
        st.success(f"Krishnamurti Ayanamsa values: {ayanamsa_value}")
    else:
        st.error("Error retrieving data. Please check your inputs and try again.")
