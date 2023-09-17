import asana

client = asana.Client.access_token('')

# Define project IDs
project1_id = '1204691824802539' #Project Updating Fields From
project2_id = '1204685748088472' #Project Getting Fields From

# Fetch tasks from both projects
project1_tasks = list(client.tasks.find_by_project(project1_id, {"opt_fields": "name,custom_fields"}))
project2_tasks = list(client.tasks.find_by_project(project2_id, {"opt_fields": "name,custom_fields"}))

# Create a dictionary with task names as keys and custom fields as values for project2
project2_dict = {}
for task in project2_tasks:
    if 'custom_fields' in task:
        try:
            project2_dict[task['name']] = {field['gid']: field for field in task['custom_fields']}
        except KeyError as e:
            print(f"KeyError {e} occurred for task {task['name']} with custom_fields: {task['custom_fields']}")
            continue

# Loop through tasks in project1
for task1 in project1_tasks:
    task1_name = task1['name']
    # Check if a task with the same name exists in project2
    if task1_name in project2_dict:
        # Get the custom field values of the task from project2
        task2_custom_fields = project2_dict[task1_name]
        # Prepare the custom fields updates for the task in project1
        fields_to_update = {}
        for field in task1['custom_fields']:
            if field['gid'] in task2_custom_fields:
                # Get the new value or set it as None if it's missing
                new_value = task2_custom_fields[field['gid']].get('enum_value', {}).get('gid', None)
                # Add the new value to the update dict
                fields_to_update[field['gid']] = new_value
        # If there are any fields to update, make the update request
        if fields_to_update:
            print("Important Hello")
            client.tasks.update(task1['gid'], {'custom_fields': fields_to_update})
