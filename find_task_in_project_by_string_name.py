import asana

client = asana.Client.access_token('')

# replace with your project ID
project_id = '1204435490926040'

# string to check for
string_to_check = 'SHP 1608'

# get all tasks in the project
tasks = client.tasks.find_by_project(project_id, {"opt_fields": "name"})

# flag to keep track if a matching task was found or not
found = False

for task in tasks:
    if string_to_check in task['name']:
        print(f"Found task: {task['name']} with id {task['gid']}")
        found = True

# print a message if no matching tasks were found
if not found:
    print(f"No task found with the name containing '{string_to_check}'")
