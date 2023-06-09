import requests
import asciichartpy

# Notion API configuration
NOTION_API_TOKEN = 'YOUR_NOTION_API_TOKEN'
NOTION_DATABASE_ID = 'YOUR_NOTION_DATABASE_ID'

# Fetch the "views" data from the Notion database
def fetch_views_data():
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Content-Type': 'application/json',
        'Notion-Version': '2021-05-13',
    }

    data = {
        'sorts': [{
            'property': 'created_time',
            'direction': 'ascending'
        }]
    }

    response = requests.post(
        f'https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query',
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        response_data = response.json()
        views_data = []

        for view in response_data['results']:
            views_data.append(view['properties']['Views']['number'])

        return views_data
    else:
        print('Error fetching data from Notion database')
        return []

# Display the views data as an ASCII chart
def display_views_chart(views_data):
    chart = asciichartpy.plot(views_data, {'height': 20})
    print(chart)

# Main function
def main():
    views_data = fetch_views_data()
    display_views_chart(views_data)

if __name__ == '__main__':
    main()
