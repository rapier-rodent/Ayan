import streamlit as st
import swisseph as swe

# Set the path to the ephemeris files (update this path accordingly)
# Note: In Streamlit Cloud, you may need to upload the ephemeris files or use a public URL.
swe.set_ephe_path('ephemeris/')  # Update this path if necessary

# Set the ayanamsa mode to Krishnamurti
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# Function to convert decimal degrees to DMS format
def decimal_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    return degrees, minutes, seconds

# Streamlit app title
st.title("Krishnamurti Ayanamsa Calculator")

# Date input
date_input = st.date_input("Select a date", value=None)

if date_input:
    # Convert the date to Julian day
    jd = swe.julday(date_input.year, date_input.month, date_input.day)

    # Calculate the position of the Sun (or any other celestial body)
    sun_position, _ = swe.calc_ut(jd, swe.SUN)  # Extract the position and ignore the second value

    # Calculate the sidereal time
    sidereal_time = swe.sidtime(jd)

    # Calculate the ayanamsa value
    ayanamsa_value = sun_position[0] - sidereal_time  # Use sun_position[0] for the ecliptic longitude

    # Convert ayanamsa value to DMS
    dms_value = decimal_to_dms(ayanamsa_value)

    # Display the result
    st.write(f"Ayanamsa value for {date_input}: {ayanamsa_value:.6f} degrees")
    st.write(f"Ayanamsa in DMS format: {dms_value[0]}° {dms_value[1]}′ {dms_value[2]:.2f}″")
