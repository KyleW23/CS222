def main():
    tuition = 8000
    increase = .03

    for x in range(1, 6):
        tuition += tuition * increase
        print(f'Year {x}: The projected tuition is ${tuition:.2f}')

main()