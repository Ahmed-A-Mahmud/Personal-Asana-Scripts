import asana
import time

client = asana.Client.access_token('')

# Define the GID lists for the sections in the first and second projects.
section_gids_project_1 = ['1202267410157928', '1202267410152774', '1202267410146556', '1202267410141187', '1202267410138035', '1202267410136791', '1202267410132605', '1202267255528606', '1202267255528595', '1202267255528584', '1202267255528573']
section_gids_project_2 = ['1204671469559333', '1204671469559336', '1204671469559337', '1204671469559338', '1204671469559339', '1204671469559340', '1204671469559341', '1204671469559342', '1204671469559343', '1204671469559344', '1204671469559345']

project_gid_1 = '1202267255528571'
project_gid_2 = '1204671469559273'

# For each section GID in the first project...
for i in range(len(section_gids_project_1)):
    section_gid_project_1 = section_gids_project_1[i]

    # Get the tasks in this project.
    tasks_project_1 = client.tasks.find_by_project(project_gid_1, {'opt_fields': 'name,memberships'})

    # For each task in the project...
    for task_project_1 in tasks_project_1:
        # Check if the task is in the current section
        if any(membership.get('section', {}).get('gid') == section_gid_project_1 for membership in
               task_project_1['memberships']):
            # Extract the task's name.
            task_name = task_project_1['name']

            # Define the properties for the new task.
            # The task's name is the same as the task in the first project.
            # The task is in the corresponding section of the second project.
            new_task = {
                'name': task_name,
                'projects': [project_gid_2],
                'sections': [section_gids_project_2[i]]
            }

            # Create the new task in the second project.
            client.tasks.create(new_task)
