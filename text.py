def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
number = int(input("Enter a number: "))
result = even_or_odd(number)
print(f"The number {number} is {result}.")
