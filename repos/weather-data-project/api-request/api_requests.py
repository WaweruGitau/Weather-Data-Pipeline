import requests

api_key = "dfcffbb838b29e5517d02d44126321f4"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

# def fetch_data():
#     print("Fetching weather...")
#     try:
#         response = requests.get(api_url)
#         print("Status code:", response.status_code)
#         print("Response text:", response.text)
#     except Exception as e:
#         print("Error occurred:", e)

# fetch_data()


def mock_fetch_data():
    return {"request":{"type":"City","query":"New York, United States of America","language":"en","unit":"m"},"location":{"name":"New York","country":"United States of America","region":"New York","lat":"40.714","lon":"-74.006","timezone_id":"America\/New_York","localtime":"2025-06-11 23:06","localtime_epoch":1749683160,"utc_offset":"-4.0"},"current":{"observation_time":"03:06 AM","temperature":24,"weather_code":113,"weather_icons":["https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0008_clear_sky_night.png"],"weather_descriptions":["Clear "],"astro":{"sunrise":"05:25 AM","sunset":"08:27 PM","moonrise":"09:24 PM","moonset":"05:07 AM","moon_phase":"Full Moon","moon_illumination":100},"air_quality":{"co":"627.15","no2":"46.065","o3":"67","so2":"16.65","pm2_5":"35.335","pm10":"35.705","us-epa-index":"2","gb-defra-index":"2"},"wind_speed":17,"wind_degree":244,"wind_dir":"WSW","pressure":1018,"precip":0,"humidity":45,"cloudcover":0,"feelslike":26,"uv_index":0,"visibility":16,"is_day":"no"}}