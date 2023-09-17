import asana

client = asana.Client.access_token('')

# replace with your task ID
task_id = '1204643367984144'

# get the task with custom fields
task = client.tasks.get_task(task_id, opt_fields='custom_fields')
task_one = client.tasks.get_task(task_id, opt_pretty='yes')
print(task_one)

# iterate over custom fields
for custom_field in task['custom_fields']:
    print(f"Custom Field Name: {custom_field['name']}, Custom Field ID: {custom_field['gid']}")
