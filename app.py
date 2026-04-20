import streamlit as st
import random
import time

# Page settings
st.set_page_config(page_title="IoT Dashboard", layout="centered")

# Title
st.title("🌡️ Smart IoT Dashboard")

st.write(
    "This IoT system monitors real-time environmental data using simulated sensors. "
    "It processes and visualizes temperature and humidity dynamically."
)

# Initialize storage
if "temp_data" not in st.session_state:
    st.session_state.temp_data = []

if "humidity_data" not in st.session_state:
    st.session_state.humidity_data = []

# Generate fake sensor data
new_temp = random.randint(20, 35)
new_humidity = random.randint(40, 80)

# Store data
st.session_state.temp_data.append(new_temp)
st.session_state.humidity_data.append(new_humidity)

# Display metrics
col1, col2 = st.columns(2)

col1.metric("🌡️ Temperature", f"{new_temp} °C")
col2.metric("💧 Humidity", f"{new_humidity} %")

# Charts
st.subheader("📈 Temperature Trend")
st.line_chart(st.session_state.temp_data)

st.subheader("📊 Humidity Trend")
st.line_chart(st.session_state.humidity_data)

# Simple device control (simulation)
st.subheader("🔌 Device Control")

if "device_status" not in st.session_state:
    st.session_state.device_status = "OFF"

if st.button("Toggle Device ON/OFF"):
    if st.session_state.device_status == "OFF":
        st.session_state.device_status = "ON"
    else:
        st.session_state.device_status = "OFF"

st.write(f"Device is currently: **{st.session_state.device_status}**")

# Auto refresh
time.sleep(2)
st.rerun()
