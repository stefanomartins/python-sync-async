import httpx
import time
import json
import asyncio



async def get_jokes(joke_id: int):
    url = "https://api.chucknorris.io/jokes/random"
    jokes = []

    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        result = result.json()["value"]
        jokes.append({"joke_id": joke_id, "joke": result})
        print(json.dumps(jokes, indent=4))


async def main():
    tasks = []

    for i in range(0, 50):
        tasks.append(get_jokes(joke_id=i))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"Tempo total de execução: {round(end_time - start_time)} segundos")
