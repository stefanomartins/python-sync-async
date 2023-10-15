import httpx
import time
import json


def get_pokemon_info(id: int) -> tuple:
    with httpx.Client() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        result = client.get(url, follow_redirects=True)
        result.raise_for_status()

        pokemon_name = result.json().get('name')
        pokemon_type_id = result.json().get('types')[0].get('type').get('url').split('/')[-2]

        url = f'https://pokeapi.co/api/v2/type/{pokemon_type_id}'
        result = client.get(url, follow_redirects=True)
        pokemon_type_name = result.json().get('name')

    return (
        id, 
        pokemon_name,
        pokemon_type_name
    )


def main():
    start_time = time.perf_counter()
    
    for i in range(1, 501):
        id, pokemon_name, pokemon_type_name = get_pokemon_info(id=i)
        print(f"ID: {id}, nome: {pokemon_name}, tipo: {pokemon_type_name}")

    end_time = time.perf_counter()
    print(f"Tempo total de execução: {round(end_time - start_time)} segundos.")


if __name__ == "__main__":
    main()
