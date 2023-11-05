import json

with open('paths.json','rb') as file:
    file_data = json.load(file)

firebasesdk_file_path = file_data['firebasesdk_file_path']
DatabaseUrl = file_data["DatabaseUrl"]
API_KEY = file_data["API_KEY"]