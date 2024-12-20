import requests

NOTION_API_URL = "https://api.notion.com/v1/databases/{DATABASE_ID}/query"
HEADERS = {
    "Authorization": "Bearer YOUR_INTEGRATION_TOKEN",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def fetch_notion_data(database_id):
    url = NOTION_API_URL.replace("{DATABASE_ID}", database_id)
    response = requests.post(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    database_id = "your_database_id"
    data = fetch_notion_data(database_id)
    print(data)
