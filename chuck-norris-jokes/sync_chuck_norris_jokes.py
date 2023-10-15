import httpx
import time
import json


def main():
    url = "https://api.chucknorris.io/jokes/random"
    jokes = []

    for i in range(0, 50):
        res = httpx.get(url=url)
        res_json = res.json()
        jokes.append({"joke_id": i, "joke": res_json["value"]})

    print(json.dumps(jokes, indent=4))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Tempo total de execução: {round(end_time - start_time)} segundos")
