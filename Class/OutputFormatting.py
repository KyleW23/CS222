def main():
    firstName = "Alice"
    age = 30
    print(f"Your name is {firstName} and you are {age} years old.")
    average = 92.12203948
    print("Student: {}, Score: {:.2f}".format(firstName, average))
    print(f"Student: {firstName}, Score: {average:.2f}")
    print("Hello {0} {1}".format("Bob", "Jones"))
    print("Hello {1} {0}".format("Bob", "Jones"))

main()