import pandas as pd
import requests
from dotenv import load_dotenv
import os
import time



if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    # List of cities to fetch weather data for
    cities = ['Tokyo', 'London', 'New York', 'Sydney', 'Mumbai', 'Rio de Janeiro', 'Paris', 'Cairo', 'Moscow', 'Toronto']
    session = requests.Session()
    results = []
    for city in cities:
        try:
            # Make API request
            resp = session.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"q": city, "appid": API_KEY, "units": "metric"},
                timeout=10,
            )
            # Check for HTTP errors
            resp.raise_for_status()
            d = resp.json()
            # Extract data
            results.append({
                "city": d.get("name", city),
                "temp_C": d.get("main", {}).get("temp"),
                "feels_like_C": d.get("main", {}).get("feels_like"),
                "description": d.get("weather", [{}])[0].get("description"),
                "humidity": d.get("main", {}).get("humidity"),
                "wind_m_s": d.get("wind", {}).get("speed"),
            })
        except Exception as e:
            # Log error for the city
            results.append({"city": city, "error": str(e)})
        time.sleep(1)  # small delay to avoid rate limits

    df = pd.DataFrame(results)
    df.to_csv("weather.csv", index=False)
   
