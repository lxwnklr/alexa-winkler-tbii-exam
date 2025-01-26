import streamlit as st
import requests
import pandas as pd
import time

def weather_waxing():
    st.title("Find the perfect wax")
    # number input to get temperature from user
    temp_input = st.number_input(label="What is the temperature on your ski day?")
    st.write("If you don't know the temperature yet, just enter the location and your ski date down below to get the forecast temperature.")

    # condition to show the right wax choice for certain temperatures
    # :color[text] to display the text in a fitting color
    if temp_input <= -12:
        st.subheader(":blue[Use blue wax.]")
    elif -12 < temp_input <= -10:
        st.subheader(":rainbow[Use blue or red wax.]")
    elif -10 < temp_input <= -6:
        st.subheader(":red[Use red wax.]")
    elif -6 < temp_input <= -4:
        st.subheader(":rainbow[Use yellow or red wax.]")
    else:
        st.subheader(":orange[Use yellow wax.]")

    # html to make part of it bold
    st.write(
        f"<b>Pay attention:</b> Usually these colors match with the temperature you just entered. But to make sure look onto the wax you have at home or want to buy. Which air temperature scale is recommended?",
        unsafe_allow_html=True)


    # the following part was created with the help of ChatGPT - the next four comments explain the procedure a bit more to be as transparent as possible
    # I researched the APIs  myself, started with the Open-Meteo API and made it functional with the help of ChatGPT, since I couldn't make it work alone
    # after this was working, I included the Nominatim API that convert longitude and latitude - this was largely done with the help of ChatGPT
    # while working with ChatGPT I had to adjust the code since some things wouldn't work the way ChatGPT suggested it
    # lastly I rewrote the last part (starting with the columns). Here I did most of the work again, since I didn't like the layout ChatGPT suggested at all


    # function to get latitude and longitude if user inputs a certain city
    def get_coordinates(city_name):
        # make sure only one request per second is possible
        time.sleep(1)
        # fetch latitude and longitude for a given city name using Nominatim API.
        params = {
            "q": city_name,
            "format": "json",
            "limit": 1
        }

        # recall email from secrets.toml-file
        email = st.secrets['weather_email']

        # custom User-Agent header to identify the application
        headers = {"User-Agent": F"WeatherApp/1.0 ({email})"}

        # Nominatim API from secrets.toml-file
        nominatim_url = st.secrets['weather_nominatim_url']

        # get() request to Nominatim API
        response = requests.get(nominatim_url, params=params, headers=headers)

        # check if request was successful
        if response.status_code == 200:
            results = response.json()
            # check if results were returned
            if results:
                # check if results were returned
                location = results[0]
                # return latitude and longitude as floats
                return float(location["lat"]), float(location["lon"])
            else:
                # if no results are found - notify user
                st.error("City not found. Please try a different name.")
                return None, None
        else:
            # handle API errors
            st.error(f"Error: Unable to fetch coordinates (Status code: {response.status_code})")
            return None, None

    # function to fetch weather data
    def fetch_weather_data(latitude, longitude):
        # fetch weather data from Open-Meteo API (using longitude and latitude)

        # parameters for API request
        parameters = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "daily": "temperature_2m_max,temperature_2m_min",
            "hourly": "temperature_2m",
            "timezone": "auto"
        }

        # Open-Meteo Weather API from secrets.toml-file
        meteo_api_url = st.secrets['weather_meteo_api_url']

        # get() request to Open-Meteo API
        response = requests.get(meteo_api_url, params=parameters)

        # check if request was successful
        if response.status_code == 200:
            # return the JSON response
            return response.json()
        else:
            # handle API errors
            st.error(f"Error: Unable to fetch weather data (Status code: {response.status_code})")
            return None

    # function to calculate averages for a specific date
    def calculate_averages_for_date(hourly_data, date):
        # calculate daily, morning, afternoon, and evening averages for a specific date.

        # extract hourly temperature and time data
        # list of timestamps
        time_data = hourly_data['time']
        # list of corresponding temperatures
        temperature_data = hourly_data['temperature_2m']

        # Create a DataFrame for easier data manipulation
        df = pd.DataFrame({
            "time": pd.to_datetime(time_data),
            "temperature": temperature_data
        })

        # extract date and hour from datetime
        df['date'] = df['time'].dt.date
        df['hour'] = df['time'].dt.hour

        # Filter DataFrame for the selected date
        daily_data = df[df['date'] == pd.to_datetime(date).date()]

        # Calculate averages (if data is available)
        if not daily_data.empty:
            daily_avg = daily_data['temperature'].mean()
            morning_avg = daily_data[daily_data['hour'].between(6, 11)]['temperature'].mean()
            afternoon_avg = daily_data[daily_data['hour'].between(12, 17)]['temperature'].mean()
            evening_avg = daily_data[daily_data['hour'].between(18, 23)]['temperature'].mean()
            return daily_avg, morning_avg, afternoon_avg, evening_avg
        else:
            # if data is not available for selected date return None
            return None, None, None, None

    # display weather and location in two columns
    c1, c2 = st.columns(2)

    # first column
    with c1:
        st.subheader("Location Settings")
        # input for city
        city_name = st.text_input("Enter City Name", value="Berlin")
        # get latitude and longitude from city_name
        latitude, longitude = get_coordinates(city_name)
        st.write(f"Selected Location: {city_name}")

        # Fetch weather data for the selected location
        data = fetch_weather_data(latitude, longitude)

        # Display current weather
        st.subheader("Current Weather")
        current = data.get("current_weather", {})
        st.write(f"Time: {current.get('time', 'N/A')}")
        st.write(f"Temperature: {current.get('temperature', 'N/A')} °C")

    # second column
    with c2:
        st.subheader("Daily Forecast")
        daily = data.get("daily", {})
        dates = daily.get("time", [])
        # user can select date (choosing from the next few days possible)
        selected_date = st.selectbox("Select a Date", dates)

        # display daily forecast for the selected date
        st.write(f"Selected Date: {selected_date}")
        hourly = data.get("hourly", {})

        # display temperature for the different times of the day or else write "No data available for the selected date."
        if hourly:
            daily_avg, morning_avg, afternoon_avg, evening_avg = calculate_averages_for_date(hourly, selected_date)
            if daily_avg is not None:
                st.write(f"Daily Average Temperature: {daily_avg:.2f}°C")
                st.write(f"Morning Average Temperature: {morning_avg:.2f}°C")
                st.write(f"Afternoon Average Temperature: {afternoon_avg:.2f}°C")
                st.write(f"Evening Average Temperature: {evening_avg:.2f}°C")
            else:
                st.write("No data available for the selected date.")

    # credit for the sources where the APIs are from
    st.write("The weather forecast is using APIs from [Open-Meteo](https://open-meteo.com/) and [Nominatim](https://nominatim.org/)")
