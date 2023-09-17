import asana

client = asana.Client.access_token('')

# replace with your source and target project IDs
source_project_id = '1202267255528475'
target_project_id = '1204640450530063'

# dictionary to keep track of sections created in the target project
section_mapping = {}

# get all tasks in the source project ordered by their list order
tasks = client.tasks.find_by_project(source_project_id, {"opt_fields": "name,memberships.section.name"})

for task in tasks:
    # get section name in source project
    source_section_name = task['memberships'][0]['section']['name'] if task['memberships'] else None

    # check if the task belongs to a section
    if source_section_name:
        # check if the section has already been created in the target project
        if source_section_name not in section_mapping:
            # create a new section in the target project with the same name
            new_section = client.sections.create_in_project(target_project_id, {"name": source_section_name})
            section_mapping[source_section_name] = new_section['gid']

        # create a new task in the target section with the same name
        new_task = client.tasks.create_in_workspace("1156738660966273",
                                                    {"name": task['name'],
                                                     "projects": [target_project_id],
                                                     "memberships": [{"project": target_project_id,
                                                                      "section": section_mapping[
                                                                          source_section_name]}]})
    else:
        # create a new task in the target project with the same name (no section)
        new_task = client.tasks.create_in_workspace("1156738660966273",
                                                    {"name": task['name'],
                                                     "projects": [target_project_id]})

    print(f"Created task: {new_task['name']} with id {new_task['gid']} in the target project.")
