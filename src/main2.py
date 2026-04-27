import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
LIST_ID = ""
url_list = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

TEAM_ID = ""
url_team = f"https://api.clickup.com/api/v2/list/{TEAM_ID}/task"


headers = {
    "Authorization": API_TOKEN

}

params = {
    "include_markdown_description": "true",
    "page": 0

}

response = requests.get(url_team, headers=headers, params = params, timeout = 30)
response_two = requests.get(url_list, headers=headers, params = params, timeout = 30)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Erro na API:', response.status_code)
    print(response.text)
    exit()

tasks = response.json()

print(tasks)


