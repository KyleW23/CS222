def main():
    weight = float(input('Enter you weight in pounds: '))
    height = (float(input('Enter you height in inches: ')))

    # Round BMI to 2 decimal places
    BMI = (weight * 703) / (height **2)
    print('Your BMI is: ', BMI)

    if BMI < 18.5:
        print('You are underweight.')
    elif BMI > 25.0:
        print('You are overweight.')
    else:
        print('You are at the optimal weight.')

main()