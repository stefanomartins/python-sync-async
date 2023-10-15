import httpx
import time
import asyncio


async def get_pokemon_info(id: int) -> str:
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        result = await client.get(url, follow_redirects=True)
        result.raise_for_status()

        pokemon_name = result.json().get('name')
        pokemon_type_id = result.json().get('types')[0].get('type').get('url').split('/')[-2]

        # url = f'https://pokeapi.co/api/v2/type/{pokemon_type_id}'
        # result = await client.get(url, follow_redirects=True)
        # pokemon_type_name = result.json().get('name')
        pokemon_type_name = await get_pokemon_type(client, type_id=pokemon_type_id)

    return (
        id, 
        pokemon_name,
        pokemon_type_name
    )


async def get_pokemon_type(client, type_id) -> str:
    url = f'https://pokeapi.co/api/v2/type/{type_id}'
    result = await client.get(url, follow_redirects=True)

    return result.json().get('name')


async def main():
    start_time = time.perf_counter()

    tasks = [get_pokemon_info(id=i) for i in range(1, 501)]

    result = await asyncio.gather(*tasks)
    
    for pokemon_id, pokemon_name, pokemon_type_name in result:
        print(f'ID: {pokemon_id}, nome: {pokemon_name}, tipo: {pokemon_type_name}')

    end_time = time.perf_counter()
    print(f"Tempo total de execução: {round(end_time - start_time)} segundos.")


if __name__ == "__main__":
    asyncio.run(main())
