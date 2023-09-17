import asana
from datetime import datetime

client = asana.Client.access_token('')

# replace with your project ID
project_id = '1204603574200968'

# task names to be excluded from deletion
exclude_task_names = ['600 6B4', 'SHP 227', 'SHP 431']

# get all tasks in the project
tasks = client.tasks.find_by_project(project_id, {"opt_fields": "name,created_at"})

for task in tasks:
    # parse the created_at string into a datetime object
    created_at = datetime.strptime(task['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")

    # check if the task was created on May 15th and its name is not in the exclude list
    if created_at.date() == datetime(2023, 5, 15).date() and task['name'] not in exclude_task_names:
        # delete the task
        client.tasks.delete(task['gid'])
        print(f"Deleted task: {task['name']} with id {task['gid']}")
