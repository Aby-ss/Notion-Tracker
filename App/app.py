import requests
import matplotlib.pyplot as plt
import datetime

# Set up your Notion API credentials and headers
token = '<YOUR_NOTION_API_TOKEN>'
database_id = '<YOUR_NOTION_DATABASE_ID>'
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

# Retrieve data from the Notion API
url = f'https://api.notion.com/v1/databases/{database_id}/query'
response = requests.post(url, headers=headers)
data = response.json()

# Process the retrieved data to determine activity levels
activity_dates = []
activity_counts = []

for item in data['results']:
    # Assuming your Notion database has a "Date" property
    activity_date = datetime.datetime.strptime(item['properties']['Date']['date']['start'], '%Y-%m-%d')
    activity_dates.append(activity_date)
    
    # Add your own logic here to determine the activity count based on your desired metrics
    activity_count = len(item['properties']) - 1  # Subtracting 1 to exclude the "Date" property
    activity_counts.append(activity_count)

# Generate the activity chart using Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(activity_dates, activity_counts, color='green')
plt.title('My Notion Activity')
plt.xlabel('Date')
plt.ylabel('Activity Count')
plt.grid(True)
plt.show()