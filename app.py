import streamlit as st
import random
import time

st.set_page_config(page_title="IoT Dashboard", layout="centered")

st.title("🌡️ IoT Dashboard")
st.subheader("Real-time Sensor Data")

# Store data
if "data" not in st.session_state:
    st.session_state.data = []

# Generate fake sensor value
new_temp = random.randint(20, 35)

# Save it
st.session_state.data.append(new_temp)

# Show current value
st.metric("Temperature", f"{new_temp} °C")

# Show chart
st.line_chart(st.session_state.data)

# Auto refresh
time.sleep(2)
st.rerun()