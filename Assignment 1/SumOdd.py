def main():
    a = int(input('Enter the starting number: '))
    b = int(input('Enter the ending number: '))

    for x in range(a, b + 1):
        if x % 2 == 1:
            print(x)

main()