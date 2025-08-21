def main():
    target = float(input('Enter the target price: '))
    current = float(input('Enter the current price: '))

    while current < target:
        current = float(input('Enter the new current price: '))

    print('Shares can be sold now.')

main()