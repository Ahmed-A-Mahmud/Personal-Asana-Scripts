import asana

client = asana.Client.access_token('')

# replace with your project ID
project_id = '1204641478250112'

# get all sections in the project
sections = client.sections.find_by_project(project_id)

for section in sections:
    #print("'" + section['gid'] + "', ")
    print(f"Section ID: {section['gid']}, Section Name: {section['name']}")
