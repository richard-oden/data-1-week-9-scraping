import requests

locations = requests.get('https://enterpriseservice.pullapart.com/Location').json()

makes = requests.get('https://inventoryservice.pullapart.com/Make').json()

models = requests.get('https://inventoryservice.pullapart.com/Model',
    params={'makeID': 21}).json()

cars = requests.post('https://inventoryservice.pullapart.com/Vehicle/Search', 
    json={'Locations':[8],'MakeID':21,'Years':[],'Models':[195]}).json()

print(cars)