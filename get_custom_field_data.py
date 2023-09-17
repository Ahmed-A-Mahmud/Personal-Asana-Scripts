import requests

# Replace with your Asana Personal Access Token
access_token = ''

# Replace with the ID of the custom field
custom_field_gid = '1204800731885544'

headers = {
    'Authorization': 'Bearer ' + access_token,
}

response = requests.get('https://app.asana.com/api/1.0/custom_fields/' + custom_field_gid, headers=headers)

print(response.json())
