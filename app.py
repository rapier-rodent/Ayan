import streamlit as st
import swisseph as swe

# Set the path to the ephemeris files (update this path accordingly)
# Note: In Streamlit Cloud, you may need to upload the ephemeris files or use a public URL.
swe.set_ephe_path('/path/to/ephemeris')  # Update this path if necessary

# Set the ayanamsa mode to Krishnamurti
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# Streamlit app title
st.title("Krishnamurti Ayanamsa Calculator")

# Date input
date_input = st.date_input("Select a date", value=None)

if date_input:
    # Convert the date to Julian day
    jd = swe.julday(date_input.year, date_input.month, date_input.day)

    # Calculate the ayanamsa value
    ayanamsa_value = swe.ayanamsa(jd)

    # Display the result
    st.write(f"Ayanamsa value for {date_input}: {ayanamsa_value:.6f}")
