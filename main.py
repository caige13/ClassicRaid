import requests
import os

import requests

bosses = {
    "Flame Leviathan": "Mechanical",
    "Ignis the Furnace Master": "Elemental",
    "Razorscale": "Dragonkin",
    "XT-002 Deconstructor": "Mechanical",
    "Assembly of Iron": "Mechanical",
    "Kologarn": "Elemental",
    "Auriaya": "Beast",
    "Hodir": "Elemental",
    "Thorim": "Humanoid",
    "Freya": "Elemental",
    "Mimiron": "Mechanical",
    "General Vezax": "Elemental",
    "Yogg-Saron": "Aberration"
}
# Replace YOUR_API_KEY with your actual API key
api_key = "de2844824ab5dac91b1ed65cba906376"

# Replace REPORT_ID with the ID of the report you want to retrieve
report_id = "Mk2f7VQgKxNZzBPF"

# Construct the URL for the Report endpoint
url = f"https://www.warcraftlogs.com:443/v1/report/fights/{report_id}?api_key={api_key}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    data = response.json()
    # Order the fights by start time
    fights = sorted(data["fights"], key=lambda x: x["start_time"])
    print(fights)
    # Print the start time of each fight
    for fight in fights:
        time_diff = (fight['end_time']-fight['start_time'])/60000

        print(f"Fight started at: {fight['start_time']}, time diff: {time_diff: .3f}, Name: {fight['name']}")
else:
    # Print an error message
    print(f"Error: {response.status_code} - {response.text}")