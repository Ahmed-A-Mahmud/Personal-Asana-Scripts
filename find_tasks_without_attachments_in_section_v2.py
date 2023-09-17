import asana

client = asana.Client.access_token('')

# replace with your section ID
section_id = '1204622306203890'

# replace with your custom fields' gid
name_last_field_gid = '1204440962955012'
name_first_field_gid = '1204440962955016'

# get all tasks in the section
tasks = client.tasks.find_by_section(section_id, {"opt_fields": "name,gid,custom_fields,attachments"})

for task in tasks:
    # check if the task has any attachments
    if not task['attachments']:
        # get custom field values
        custom_fields = task['custom_fields']

        # find the custom fields "Name Last" and "Name First"
        name_last_field = next((field for field in custom_fields if field['gid'] == name_last_field_gid), None)
        name_first_field = next((field for field in custom_fields if field['gid'] == name_first_field_gid), None)

        # check if the custom fields have values
        if name_last_field and name_first_field and name_last_field['text_value'] and name_first_field['text_value']:
            print(f"Task Name: {task['name']}, Task ID: {task['gid']}")
