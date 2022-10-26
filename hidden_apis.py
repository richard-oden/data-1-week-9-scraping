import requests

def get_json(url: str, params: dict):
    response = requests.get(url, params=params)

    if not response.ok or 'json' not in response.headers['content-type']:
        return None

    return response.json()

def post_json(url: str, json: dict):
    response = requests.post(url, json=json)

    if not response.ok or 'json' not in response.headers['content-type']:
        return None

    return response.json()

def get_locations():
    return get_json('https://enterpriseservice.pullapart.com/Location')

def get_makes():
    return get_json('https://inventoryservice.pullapart.com/Make')

def get_models(make_id: int):
    return get_json('https://inventoryservice.pullapart.com/Model', {'makeID': make_id})

def get_vehicles(location_ids: list[int], make_id: int, years: list[int], model_ids: list[int]):
    return post_json('https://inventoryservice.pullapart.com/Vehicle/Search', 
        {'Locations': location_ids, 'MakeID': make_id, 'Years': years, 'Models': model_ids})
