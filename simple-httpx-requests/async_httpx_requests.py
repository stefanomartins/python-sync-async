import httpx
import asyncio
import time

async def anything():
    url = 'https://httpbin.org/anything'
    headers = {
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        result = await client.get(url, headers=headers)

    return result.json().get('origin')


async def main():
    start_time = time.perf_counter()
    tasks = []
    for i in range(0, 10):
        tasks.append(anything())

    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    print(f'Tempo total de execução: {round(end_time - start_time)} segundos')


if __name__ == '__main__':
    asyncio.run(main())