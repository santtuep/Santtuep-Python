#harjoituksia

import math

user = input("Enter your name: ")
print(f"Nice to meet you, {user}!")

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight / (height / 100) ** 2 #huom. ** on potenssiin korotus ja * on kertolasku
print(f"Your BMI is {bmi:.2f}") #muotoilu

input_str = input("How old are you? ")
age = int(input_str)
print(f"So you were born in {2024 - age}.")

print(f"The first ten decimals of PI are {math.pi:.10f}")

farenheit_str = input("Enter temperature in Farenheit: ")
farenheit = float(farenheit_str)
celsius = (farenheit - 32) * 5 / 9
print(f"The temperature in Celsius is {celsius}")

