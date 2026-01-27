import requests

from datetime import datetime
from typing import Annotated, Optional

from fastmcp import FastMCP
from settings import get_settings

mcp = FastMCP("OpenWeatherMap Server")
settings = get_settings()

API_KEY = settings.openweather_api_key
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
DAILY_URL = "http://api.openweathermap.org/data/2.5/forecast/daily"
MONTHLY_URL = "https://history.openweathermap.org/data/2.5/aggregated/month"


def get_coords(city: str) -> tuple[float, float]:
    response = requests.get(GEO_URL, params={"q": city, "limit": 1, "appid": API_KEY})
    response.raise_for_status()
    data = response.json()
    return data[0]["lat"], data[0]["lon"]


@mcp.tool(description="Get daily weather forecast for a city up to 16 days.")
def get_daily_forecast(
    city: Annotated[str, "The city name"],
    days: Annotated[int, "Number of days (1-16)"] = 7,
) -> str:
    try:
        if days < 1 or days > 16:
            raise ValueError("Number of days must be between 1 and 16.")

        lat, lon = get_coords(city)
        params = {"lat": lat, "lon": lon, "cnt": days, "appid": API_KEY, "units": "standard"}
        resp = requests.get(url=DAILY_URL, params=params)
        resp.raise_for_status()
        data = resp.json()

        results = [f"Forecast for {city}:"]
        for day in data["list"]:
            date = day["dt"]
            date = datetime.fromtimestamp(int(date))
            temp = day["temp"]
            desc = day["weather"][0]["description"]
            line = f"- Day {date}: {desc}, " f"High: {temp['max']}K, Low: {temp['min']}K, "
            results.append(line)

        return "\n".join(results)

    except Exception as e:
        return f"Error getting daily forecast: {e}"


@mcp.tool(description="Get monthly weather forecast for a city.")
def get_monthly_forecast(
    city: Annotated[str, "The city name"],
    month: Annotated[Optional[int], "Month number (1-12). Defaults to current month"] = None,
) -> str:
    if month is None:
        month = datetime.now().month

    try:
        if month < 1 or month > 12:
            raise ValueError("Month number must be between 1 and 12.")

        lat, lon = get_coords(city)
        params = {"lat": lat, "lon": lon, "month": month, "appid": API_KEY}
        resp = requests.get(url=MONTHLY_URL, params=params)
        resp.raise_for_status()
        stats = resp.json()["result"]

        return "\n".join(
            (
                f"Average monthly weather statistics for {city.title()} in {month}",
                f"Avg Temp: {stats['temp']['mean']}K",
                f"Avg Humidity: {stats['humidity']['mean']}%",
                f"Avg Wind Speed: {stats['wind']['mean']} m/s",
            )
        )

    except Exception as e:
        return f"Error getting monthly statistics: {e}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=settings.openweather_mcp_port)
