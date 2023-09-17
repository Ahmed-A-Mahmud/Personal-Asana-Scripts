import asana
import requests
import os
import tempfile

# Initialize the Asana client
client = asana.Client.access_token('')

# GIDs for your two projects
project1_gid = '1204685958384929' #Project Getting Subtasks From
project2_gid = '1204691824802544' #Project Adding Subtasks To

# Get tasks for both projects
tasks_project1 = client.tasks.get_tasks_for_project(project1_gid, opt_pretty=True)
tasks_project2 = client.tasks.get_tasks_for_project(project2_gid, opt_pretty=True)

# Map tasks by name
tasks_map = {task['name']: task for task in tasks_project2}

# Iterate over each task in the first project
for task1 in tasks_project1:
    task2 = tasks_map.get(task1['name'])
    if not task2:
        continue  # Skip if no matching task found in the second project

    # Get subtasks for the task in the first project
    subtasks = client.tasks.get_subtasks_for_task(task1['gid'], opt_pretty=True)

    # Iterate over each subtask
    for subtask in subtasks:
        # Create the same subtask in the corresponding task in the second project
        new_subtask = client.tasks.create_subtask_for_task(task2['gid'],
                                                           {'name': subtask['name'],
                                                            'notes': subtask.get('notes', '')},
                                                           opt_pretty=True)
