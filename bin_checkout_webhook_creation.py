import requests

def create_webhook():
    # Set your personal access token and project ID
    access_token = ''
    project_id = '1204641478250112'

    # Set the webhook endpoint URL of your Glitch server
    webhook_url = 'https://bloom-wooden-sandwich.glitch.me/'

    # Set the events you want to trigger the webhook
    events = ['changed']  # For example, task due date changes

    # Create the request body
    data = {
        'data': {
            'target': webhook_url,
            'resource': project_id,
            'filters': [
                {'resource_type': 'task'}
            ],
            'events': events
        }
    }

    # Set the headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Make the POST request to create the webhook
    response = requests.post('https://app.asana.com/api/1.0/webhooks', json=data, headers=headers)

    # Check the response status
    if response.status_code == 200:
        print('Webhook created successfully.')
    else:
        print('Failed to create webhook.')
        print('Response:', response.json())


# Call the function to create the webhook
create_webhook()
