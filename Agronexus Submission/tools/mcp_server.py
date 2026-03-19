import json

"""
AGRINEXUS MCP SERVER (Prototype Data Store)
-------------------------------------------
For this hackathon prototype, we are utilizing an in-memory mock database.
In a production environment, this MCP server is designed to connect 
directly to a Google Cloud Spanner instance.
"""

# In-Memory Prototype Database
FARM_DATABASE = {
    "farm_001": {"location": "North River", "crop": "Wheat", "status": "Healthy", "water_source": "Main Aquifer"},
    "farm_002": {"location": "South Valley", "crop": "Corn", "status": "At Risk - Drought", "water_source": "Lake Alpha"},
    "farm_003": {"location": "North River", "crop": "Wheat", "status": "Infected - Rust", "water_source": "Main Aquifer"}
}

def get_farm_data(location: str) -> str:
    """
    Fetches farm data based on a specific location or river system.
    Args:
        location: The region to search for (e.g., 'North River', 'South Valley').
    """
    # Query the prototype database for farms matching the location
    results = [f for f in FARM_DATABASE.values() if location.lower() in f['location'].lower()]
    
    if results:
        return json.dumps(results)
    return f"No farms found in the {location} region."

def get_weather_forecast(location: str) -> str:
    """
    Fetches the current weather and 3-day forecast for a farming region.
    Args:
        location: The region to check (e.g., 'North River', 'South Valley').
    """
    loc = location.lower()
    if "north river" in loc:
        return json.dumps({"condition": "Heavy Rain", "humidity": "85%", "warning": "High risk for fungal spread."})
    elif "south valley" in loc:
        return json.dumps({"condition": "Severe Drought", "humidity": "15%", "warning": "Critical water shortage."})
    return json.dumps({"condition": "Clear", "humidity": "50%", "warning": "None"})