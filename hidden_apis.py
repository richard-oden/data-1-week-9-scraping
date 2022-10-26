import requests

def get_json(url: str, params: dict = None):
    response = requests.get(url, params=params)

    if not response.ok or 'json' not in response.headers['content-type']:
        return None

    return response.json()

def post_json(url: str, json: dict = None):
    response = requests.post(url, json=json)

    if not response.ok or 'json' not in response.headers['content-type']:
        return None

    return response.json()

def get_locations() -> list | None:
    return get_json('https://enterpriseservice.pullapart.com/Location')

def get_makes() -> list | None:
    return get_json('https://inventoryservice.pullapart.com/Make')

def get_models(make_id: int) -> list | None:
    return get_json('https://inventoryservice.pullapart.com/Model', {'makeID': make_id})

def get_vehicles(location_ids: list[int], make_id: int, model_ids: list[int], years: list[int] = []) -> list | None:
    return post_json('https://inventoryservice.pullapart.com/Vehicle/Search', 
        {'Locations': location_ids, 'MakeID': make_id, 'Years': years, 'Models': model_ids})

def main():
    locations = get_locations()
        
    print('Select a location:')
    for location in sorted(locations, key=lambda _: _['locationName']):
        print(f' - [{location["locationID"]}] {location["locationName"]}')

    location_id = int(input())

    makes = get_makes()

    print('Select a make:')
    for make in sorted(makes, key=lambda _: _['makeName']):
        print(f' - [{make["makeID"]}] {make["makeName"]}')

    make_id = int(input())

    models = get_models(make_id)

    print('Select a model:')
    for model in sorted(models, key=lambda _: _['modelName']):
        print(f' - [{model["modelID"]}] {model["modelName"]}')

    model_id = int(input())

    vehicles = get_vehicles([location_id], make_id, model_ids=[model_id])

    for vehicle in vehicles:
        for exact_info in vehicle['exact']:
            print(f'\n - {exact_info["makeName"]} {exact_info["modelName"]} {exact_info["modelYear"]}')
            print(f'   date on yard: {exact_info["dateYardOn"]}')
            print(f'   row: {exact_info["row"]}')
            print(f'   vin: {exact_info["vin"]}')

main()