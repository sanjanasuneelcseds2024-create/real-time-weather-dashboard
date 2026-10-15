
import streamlit as st
import requests

# -------------------------------
# Weather Detection App
# -------------------------------

st.set_page_config(page_title="Weather Detection App", page_icon="🌦️")

st.title("🌦️ Weather Detection System")
st.write("Get real-time weather updates using OpenWeatherMap API")

api_key = "9ffed7ac04988e27e7ce2edb8c01cc59"  # Replace with your OpenWeatherMap API key

city = st.text_input("Enter City Name")
if st.button("Get Weather"):
    if city == "":
        st.warning("Please enter a city name")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            weather = data["weather"][0]["description"].title()
            wind = data["wind"]["speed"]
            st.success(f"Weather details for {city.upper()}")

            st.metric("🌡️ Temperature (°C)", temp)
            st.metric("💧 Humidity (%)", humidity)
            st.metric("🌬️ Wind Speed (m/s)", wind)
            st.metric("🌤️ Condition", weather)

        else:
            st.error("City not found. Please check the city name.")
