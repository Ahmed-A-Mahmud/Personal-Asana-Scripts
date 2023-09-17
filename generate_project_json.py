import requests

# Replace with your Asana Personal Access Token
access_token = ''

# Replace with your Asana project ID
project_id = '1204641478250112'

headers = {
    'Authorization': 'Bearer ' + access_token,
}

response = requests.get('https://app.asana.com/api/1.0/projects/' + project_id + '/custom_field_settings', headers=headers)

print(response.json())
