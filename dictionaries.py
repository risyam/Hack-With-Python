#! /bin/python3

# Key-Value Pairs
drinks={"Pepsi":100,"Coke":120,"Sprite":80,"Mirinda":75}
print(drinks)

print(drinks.get('Coke')) # Prints 120

drinks['Fruity']=50 # adds new Key-Value pair
print(drinks) # Prints {'Pepsi': 100, 'Coke': 120, 'Sprite': 80, 'Mirinda': 75, 'Fruity': 50}

drinks.update({"Thumbsup":60}) # adds new Key-Value pair
print(drinks) # {'Pepsi': 100, 'Coke': 120, 'Sprite': 80, 'Mirinda': 75, 'Fruity': 50, 'Thumbsup': 60}

drinks['Coke']=115 # updates value
print(drinks)  # Prints {'Pepsi': 100, 'Coke': 115, 'Sprite': 80, 'Mirinda': 75, 'Fruity': 50, 'Thumbsup': 60}

employees={"ProdSec":["ABC","DEF","GHI"],"InfoSec":["JKL","MNO","PQR"]}

print(employees)
print(employees.get('ProdSec'))
print(employees.get('ProdSec')[1]) # Prints DEF

employees['InfraSec']=["STU","VWX"] # adds new Key-Value pair
print(employees) # Prints {'ProdSec': ['ABC', 'DEF', 'GHI'], 'InfoSec': ['JKL', 'MNO', 'PQR'], 'InfraSec': ['STU', 'VWX']}

employees.update({"QA":["YZA","BCD"]}) # adds new Key-Value pair
print(employees) # Prints {'ProdSec': ['ABC', 'DEF', 'GHI'], 'InfoSec': ['JKL', 'MNO', 'PQR'], 'InfraSec': ['STU', 'VWX'], 'QA': ['YZA', 'BCD']}



