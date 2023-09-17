import asana

client = asana.Client.access_token('')

# get all workspaces
workspaces = list(client.workspaces.find_all())

for workspace in workspaces:
    print(f"Workspace Name: {workspace['name']}, Workspace ID: {workspace['gid']}")
