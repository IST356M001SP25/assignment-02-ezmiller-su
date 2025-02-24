'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

import json

packaging = []

def parse_packaging(packaging_data: str) -> list[dict]:
    itemlist = []

    for package in packaging_data.split(' / '):
        item = package.split(' in ')[0]
        item_data = item.split(' ')
        itemlist.append({item_data[1]: int(item_data[0])})

    item = package.split(' in ')[-1]
    item_data = item.split(' ')
    itemlist.append({item_data[1]: int(item_data[0].strip())})

    return(itemlist)

def calc_total_units(package: list[dict]) -> int:
    total = 1
    for item in package:
        number = list(item.values())[0]
        total = total * number
    return(total)

def get_unit(package: list[dict]) -> str:
    return(str(package[0]).split("'")[1])

with open('data/packaging.txt','r') as packagingtxt:
    for line in packagingtxt.read().split('\n'):
        parsed = parse_packaging(line)
        packaging.append(parsed)
        unit = get_unit(parsed)
        total_units = calc_total_units(parsed)
        print(f"{line} => total units: {total_units} {unit}")

with open('data/packaging.json','w') as file:
    json.dump(packaging, file, indent=4)