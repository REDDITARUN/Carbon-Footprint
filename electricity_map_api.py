import requests
import json

# Set coordinates
coordinates = {"lat": 34.00906474557528, "lon": -118.4984580927553}

# Replace with your Electricity Map API key
API_KEY = 'your_api_key_here'

# Build URL for carbon intensity
url_intensity = f"https://api.electricitymap.org/v3/carbon-intensity/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"

# Fetch data
response_intensity = requests.get(url_intensity, headers={"auth-token": API_KEY})
carbon_intensity = json.loads(response_intensity.content)

# Print carbon intensity
print("Carbon Intensity:", carbon_intensity)

# Build URL for power breakdown
url_breakdown = f"https://api.electricitymap.org/v3/power-breakdown/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"

# Fetch power breakdown
response_breakdown = requests.get(url_breakdown, headers={"auth-token": API_KEY})
power_breakdown = json.loads(response_breakdown.content)

# Display renewable and fossil-free percentages
print("Renewable Percentage:", power_breakdown['renewablePercentage'])
print("Fossil Free Percentage:", power_breakdown['fossilFreePercentage'])

# Calculate and print power consumption breakdown in percentages
total_power = power_breakdown['powerConsumptionTotal']
consumption_percent = {k: round((v / total_power) * 100, 2) for k, v in power_breakdown['powerConsumptionBreakdown'].items()}
print("Power Consumption Breakdown:", consumption_percent)
