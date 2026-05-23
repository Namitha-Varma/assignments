def checkout(*prices, **info):
    total = sum(prices)
    print("Total:", total)

    for key, value in info.items():
        print(f"{key}: {value}")

checkout(100, 200, 50, name="Alex", payment="Card")


# 1) Arbitrary Arguments (*args)

def student_marks(*marks):
    total = sum(marks)
    average = total / len(marks)

    print("Total Marks =", total)
    print("Average Marks =", average)

student_marks(20, 30, 40, 50)


# 2) Arbitrary Arguments (*args)

def calculate_average(*marks):
    average = sum(marks) / len(marks)
    print("Average marks =", average)

calculate_average(35, 40, 45, 30, 50)


# 3) Arbitrary Arguments (*args, **kwargs)

def student_info(*subjects, **details):
    print("\nSubjects:")
    for subject in subjects:
        print(subject)

    print("\nStudent Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(
    "Telugu",
    "English",
    "Maths",
    name="Mahi",
    age=15,
    grade="A+",
    section="B"
)


# 4) Arbitrary Arguments (*args, **kwargs)

def checkout(*products, **details):
    print("\nProducts:")
    for product in products:
        print(product)

    print("\nProduct Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

checkout(
    "Foundation",
    "Sunscreen",
    "Moisturizer",
    category="Makeup",
    brand="Mamaearth",
    price="250, 140, 300",
    availability="Yes"
)


# Pure Functions

def double_list(numbers):
    return [n * 2 for n in numbers]

print("\nDouble List:", double_list([1, 2, 3]))


# 1) Celsius to Fahrenheit Conversion

def conversion_list(temperatures):
    return [n * 9 / 5 + 32 for n in temperatures]

print("Fahrenheit Values:", conversion_list([25, 35, 45]))


# 2) Cube of each number

def cube(numbers):
    return [n ** 3 for n in numbers]

print("Cube Values:", cube([3, 2, 4, 6]))


# 3) Odd or Even

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("\nEnter a number: "))
result = check_even_odd(n)
print(f"{n} is {result}")


# Returning Multiple Values

# 1) Maximum and Minimum

def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 2, 9, 1])
print("\nMinimum =", low)
print("Maximum =", high)


# 2) Sum and Average

def students_result(numbers):
    if len(numbers) == 0:
        return 0, 0

    total = sum(numbers)
    avg = total / len(numbers)

    return total, avg

total, avg = students_result([35, 56, 76, 40])
print("\nSum =", total)
print("Average =", avg)


# 3) Quotient and Remainder

def dividend_divisor(num1, num2):
    quotient = num1 // num2
    remainder = num1 % num2

    return quotient, remainder

q, r = dividend_divisor(25, 2)
print("\nQuotient =", q)
print("Remainder =", r)


# 4) Square and Cube of a Number

def values_of_number(num):
    square = num * num
    cube = num * num * num

    return square, cube

n = int(input("\nEnter a number: "))
square, cube = values_of_number(n)

print(f"Square of {n} =", square)
print(f"Cube of {n} =", cube)


# Recursive Functions

# 1) Factorial

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print("\nFactorial of 5 =", factorial(5))


# 2) Print numbers from n to 1

def print_n_to_1(n):
    if n < 1:
        return

    print(n)
    print_n_to_1(n - 1)

print("\nNumbers from 5 to 1:")
print_n_to_1(5)


# 3) Power of a Number

def power_of_number(x, n):
    if n == 0:
        return 1

    return x * power_of_number(x, n - 1)

print("\n2 power 3 =", power_of_number(2, 3))


# 4) Sum of numbers from 1 to n

def sum_to_n(n):
    if n == 1:
        return 1

    return n + sum_to_n(n - 1)

n = int(input("\nEnter a positive integer: "))
print("Sum from 1 to", n, "is:", sum_to_n(n))