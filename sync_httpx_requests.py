import httpx
import time

def anything():
    url = 'https://httpbin.org/anything'
    headers = {
        'Content-Type': 'application/json'
    }

    with httpx.Client() as client:
        result = client.get(url, headers=headers)
        
    return result.json().get('origin')


def main():
    start_time = time.perf_counter()
    for i in range(0, 10):
        print(f'Chamada {i}: {anything()}')
    
    end_time = time.perf_counter()
    print(f'Tempo total de execução: {round(end_time - start_time)} segundos')

if __name__ == '__main__':
    main()