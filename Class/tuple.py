def add(a: int, b: int) -> int:
    return a + b

def quotientRemainder(a, b):
    return (a // b, a % b)

def generateSeries() -> list[float]:
    return [value for value in range(10,1000, 50)]

def main():
    print(quotientRemainder(10, 3))
    x, y = quotientRemainder(10, 3)
    print(x)
    print(y)
    print(generateSeries())

main()