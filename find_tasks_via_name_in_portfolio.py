import asana

client = asana.Client.access_token('')

# replace with your portfolio ID and target project ID
portfolio_id = '1202247149396244'

# list of strings to check for
strings_to_check = ["BRSIC 408", "BRSC 32", "BRSC 53", "BR531 33", "BR531 51", "BRKAT 32", "BRSDT 34", "BR542 32", "BRDG 31", "BRDG 41", "BRSN 41", "600 3D3", "600 6B4", "600 10D1", "600 10C1", "BWY 305", "BWY 415", "BWY 419", "BWY 426", "BWY 444", "BWY 448", "BWY 505", "BWY 515", "BWY 538", "BWY 603", "BWY 609", "BWY 613", "BWY 616", "BWY 634", "BWY 638", "BWY 705", "BWY 739", "BWY 809", "BWY 818", "BWY 827", "BWY 926", "BWY 1109", "BWY 1122", "BWY 1327", "BWY 1331", "CRL 1C5", "CRL 1C6", "CRL 2C1", "CRL 3A1", "CRL 5A1", "CRL 6B6", "CRL 7D3", "CRL 9D3", "CRL 9A2", "CRL 10C5", "CRL 10A3", "CRL 10B2", "CAR 812A", "CAR 901B", "CAR 902", "CAR 903A", "CAR 905A", "CAR 906A", "CAR 907A", "CAR 914E", "CAR 1001A", "CAR 1003B", "CAR 1005B", "CAR 1005A", "CAR 1007A", "CAR 1011A", "CAR 1012B", "CAR 1012A", "CAR 1013B", "CAR 1014E", "CAR 1102", "CAR 1103B", "CAR 1103A", "CAR 1104", "CAR 1106A", "CAR 1112B", "CAR 1113B", "CAR 1113A", "CAR 1114B", "CAR 1203A", "CAR 1212B", "CAR 1212A", "CAR 1213B", "CAR 1214A", "CAR 1214E", "CAR 1301A", "CAR 1301B", "CAR 1302", "CAR 1306B", "CAR 1307B", "CAR 1312A", "CAR 1314D", "CAR 1314B", "CAR M03A", "CAR 203A", "CAR 206B", "CAR 207B", "CAR 207A", "CAR 305B", "CAR 305A", "CAR 307A", "CAR 311B", "CAR 311A", "CAR 401A", "CAR 403B", "CAR 405B", "CAR 405A", "CAR 411A", "CAR 505A", "CAR 507A", "CAR 508B", "CAR 509A", "CAR 601A", "CAR 603A", "CAR 605A", "CAR 605B", "CAR 606A", "CAR 607B", "CAR 607A", "CAR 608A", "CAR 608B", "CAR 614C", "CAR 701A", "CAR 702", "CAR 703A", "CAR 703B", "CAR 704", "CAR 709B", "CAR 711A", "CAR 712A", "CAR 712B", "CAR 714E", "CAR 801B", "CAR 802", "CAR 803B", "CAR 804", "CAR 805A", "CAR 807A", "CAR 807B", "CAR 808A", "CAR 808B", "CAR 809B", "EC 607", "EC 613", "EC 1404C", "EC 2004A", "FUR 106", "FUR 204", "FUR 303", "FUR 314", "FUR 319", "FUR 323", "FUR 403", "FUR 407", "FUR 409", "FUR 517", "FUR 521", "FUR 601", "FUR 602", "FUR 613", "FUR 616", "FUR 701", "FUR 707", "FUR 717", "FUR 818", "FUR 921", "FUR 1007", "HMY 803", "HTL 2A3", "HTL 2C1", "HTL 3C7", "HTL 3A14", "HTL 5B10", "HTL 5B2", "HTL 5C11", "HTL 5A10", "HTL 5C3", "HTL 5C7", "HTL 5C6", "HTL 6B7", "HTL 6C5", "HTL 6C9", "HTL 8C13", "HTL 8B3", "HOG 6E4", "JJ 1102", "JJ 1122", "JJ 1123", "JJ 1127", "JJ 1143", "JJ 1146", "JJ 1203", "JJ 1217", "JJ 1219", "JJ 1226", "JJ 1232", "JJ 1233", "JJ 1240", "JJ 1248", "JJ 1304", "JJ 1309", "JJ 1317", "JJ 1332", "JJ 1341", "JJ 1346", "JJ 1402", "JJ 1417", "JJ 1424", "JJ 1426", "JJ 1431", "JJ 1432", "JJ 1503", "JJ 1504", "JJ 1509", "JJ 1512", "JJ 1515", "JJ 1518", "JJ 504", "JJ 516", "JJ 523", "JJ 526", "JJ 529", "JJ 531", "JJ 602", "JJ 605", "JJ 620", "JJ 621", "JJ 637", "JJ 641", "JJ 647", "JJ 702", "JJ 706", "JJ 707", "JJ 709", "JJ 710", "JJ 716", "JJ 720", "JJ 721", "JJ 722", "JJ 723", "JJ 726", "JJ 732", "JJ 738", "JJ 741", "JJ 744", "JJ 747", "JJ 748", "JJ 805", "JJ 806", "JJ 821", "JJ 825", "JJ 830", "JJ 833", "JJ 841", "JJ 846", "JJ 920", "JJ 928", "JJ 933", "JJ 946", "JJ 1006", "JJ 1007", "JJ 1024", "JJ 1025", "JJ 1029", "JJ 1048", "MCB 210", "MCB 216", "MCB 223", "MCB 224", "MCB 225", "MCB 305", "MCB 306", "MCB 308", "MCB 313", "MCB 323", "MCB 324", "MCB 405", "MCB 415", "MCB 425", "MCB 427", "MCB 429", "MCB 519", "MCB 604", "MCB 607", "MCB 615", "MCB 620", "MCB 627", "MCB 703", "MCB 725", "MCB 729", "MCB 821", "MCB 823", "MCB 830", "MCB 831", "RIV 304", "RIV 316", "RIV 405", "RIV 621", "RUG 407", "SHP 201", "SHP 207", "SHP 208", "SHP 227", "SHP 230", "SHP 308", "SHP 330", "SHP 401", "SHP 404", "SHP 407", "SHP 416", "SHP 428", "SHP 431", "WAL 201", "WAL 207", "WAL 208", "WAL 227", "WAL 230", "WAL 308", "WAL 330", "WAL 401", "WAL 404", "WAL 407", "WAL 416", "WAL 428", "WAL 431", "WAL 508", "WAL 509", "WAL 529", "WAL 602", "WAL 618", "WAL 625", "WAL 627", "WAL 630", "WAL 725", "WAL 729", "WAL 802", "WAL 814", "WAL 818", "WAL 823", "WAL 907", "WAL 909", "WIN 325", "WIN 414", "WIN 416", "WIN 417", "WIN 432", "WIN 517", "WIN 542B", "WIN 615", "WIN 731", "WIN 812", "WIN 932", "WIN 1014", "WIN 1219", "WBH 6L"]

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
                    # add the task name to the found_strings set
                    found_strings.add(task['name'])

# print out a message for strings that were found
for string in found_strings:
        print(f"Task found with the name '{string}'")
