import requests


def myGenerator(a, b):
    result = requests.get(f"https://www.random.org/integers/?num=1&min={a}&max={b}&col=1&base=10&format=plain&rnd=new")
    return int(result.text)


if __name__ == "__main__":
    result = myGenerator(1, 1000)
    print(result)