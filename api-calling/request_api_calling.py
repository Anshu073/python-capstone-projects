# How To Connect An API Using Python
import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retireve data {response.status_code}")

pokemon_name = "Pikachu"
pokemon_info = get_pokemon_info(pokemon_name)


try:
    if pokemon_info:
        print(pokemon_info["id"])
        print(pokemon_info["name"])
        print(pokemon_info["weight"])
        print(pokemon_info["height"])

except KeyError:
    print("some Keys not found!")

