import asana

client = asana.Client.access_token('')

# replace with your portfolio ID and target project ID
portfolio_id = '1204641598871316'
target_project_id = '1204771134877487'

# list of strings to check for
strings_to_check = ["JJ 501", "JJ 502", "JJ 503", "JJ 505", "JJ 506", "JJ 509", "JJ 510", "JJ 516", "JJ 517", "JJ 518", "JJ 519", "JJ 520", "JJ 521", "JJ 522", "JJ 523", "JJ 524", "JJ 525", "JJ 526", "JJ 527", "JJ 528", "JJ 529", "JJ 530", "JJ 531", "JJ 532", "JJ 533", "JJ 534", "JJ 535", "JJ 536", "JJ 538", "JJ 539", "JJ 540", "JJ 543", "JJ 544", "JJ 546", "JJ 547", "JJ 548", "JJ 601", "JJ 602", "JJ 603", "JJ 604", "JJ 605", "JJ 606", "JJ 609", "JJ 610", "JJ 616", "JJ 617", "JJ 618", "JJ 619", "JJ 620", "JJ 621", "JJ 622", "JJ 623", "JJ 624", "JJ 625", "JJ 626", "JJ 627", "JJ 628", "JJ 629", "JJ 630", "JJ 631", "JJ 632", "JJ 633", "JJ 634", "JJ 635", "JJ 636", "JJ 638", "JJ 639", "JJ 640", "JJ 643", "JJ 644", "JJ 646", "JJ 647", "JJ 648", "JJ 701", "JJ 702", "JJ 703", "JJ 704", "JJ 705", "JJ 706", "JJ 709", "JJ 710", "JJ 716", "JJ 717", "JJ 718", "JJ 719", "JJ 720", "JJ 721", "JJ 722", "JJ 723", "JJ 724", "JJ 725", "JJ 726", "JJ 727", "JJ 728", "JJ 729", "JJ 730", "JJ 731", "JJ 732", "JJ 733", "JJ 734", "JJ 735", "JJ 736", "JJ 737", "JJ 738", "JJ 739", "JJ 740", "JJ 743", "JJ 744", "JJ 746", "JJ 747", "JJ 748"]
# a set to hold found strings
found_strings = set()

# get all projects in the portfolio
portfolio_items = client.portfolios.get_items_for_portfolio(portfolio_id)

for item in portfolio_items:
    # check if the item is a project
    if item['resource_type'] == 'project':
        project_id = item['gid']

        # get all tasks in the project
        tasks = client.tasks.find_by_project(project_id, {"opt_fields": "name"})

        for task in tasks:
            for string in strings_to_check:
                if string in task['name']:
                    # add the task to the target project
                    client.tasks.add_project(task['gid'], {"project": target_project_id})
                    found_strings.add(string)

# print out a message for strings that were not found
for string in strings_to_check:
    if string not in found_strings:
        print(f"No task found with the name '{string}'")
