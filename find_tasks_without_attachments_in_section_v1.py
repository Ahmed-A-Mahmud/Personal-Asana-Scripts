import asana

client = asana.Client.access_token('')

# replace with your section ID
section_id = '1204622306203890'

# get all tasks in the section
tasks = client.tasks.find_all({"section": section_id})

for task in tasks:
    # get all attachments for the task
    attachments = client.attachments.find_by_task(task['gid'])

    # check if the task has any attachments
    if not any(True for _ in attachments):
        print(f"Task Name: {task['name']}")
