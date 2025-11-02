import pandas as pd
import requests

API_KEY = "435535bcdbaeaff59fcc1a224bd6d927"

def get_weather(destination):
    """Fetch current weather for a destination using OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={destination}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        print(f"🌦️ API Response for {destination}:", data)  # Debug line

        if data.get("cod") != 200:
            return "Weather info unavailable"
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        return f"{temp}°C, {desc}"
    except Exception as e:
        print("❌ Error fetching weather:", e)
        return "Weather info unavailable"

def get_recommendations(budget, interest, start_date, end_date):
    data = [
        {"Destination": "Goa", "Best Time": "Nov-Feb", "Cost": 15000, "Category": "Beaches"},
        {"Destination": "Manali", "Best Time": "Dec-Mar", "Cost": 20000, "Category": "Mountains"},
        {"Destination": "Jaipur", "Best Time": "Oct-Mar", "Cost": 12000, "Category": "Culture"},
        {"Destination": "Andaman", "Best Time": "Oct-May", "Cost": 50000, "Category": "Beaches"},
        {"Destination": "Rishikesh", "Best Time": "Feb-May", "Cost": 8000, "Category": "Mountains"},
        {"Destination": "Darjeeling", "Best Time": "Mar-Jun", "Cost": 10000, "Category": "Mountains"},
        {"Destination": "Lonavala", "Best Time": "Jul-Sep", "Cost": 7000, "Category": "Mountains"},
    ]

    df = pd.DataFrame(data)

    # Apply flexible filtering
    filtered_df = df[
        (df["Cost"] <= budget + 2000)
        & (df["Category"].isin(interest) if interest else True)
    ].copy()

    # ✅ Fix: use .loc[] to avoid SettingWithCopyWarning
    filtered_df.loc[:, "Weather"] = filtered_df["Destination"].apply(get_weather)

    return filtered_df
