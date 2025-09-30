def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

fruits = ['apple', 'banana', 'cherry']
wordLength = map(len, fruits)
print(list(wordLength))