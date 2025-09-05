age = int(input("Anna ikäsi: "))
if age >= 18:
    print("You are an adult!")
else:
    print("You are a teenager!")

password = input("Anna salasana: ")
if password == "kittycat":
    print("Password is correct!")
else:
    print("Password is incorrect!")

money = float(input("Anna rahasumma joka sinulla on: "))
if money >= 5:
    print("You can buy a coffee.")
else:
    print("You do not have enough money.")

height = int(input("Kuinka pitkä olet? "))
if 170 < height < 180:
    print("You are average height!")
elif height > 180:
    print("You are tall!")
else:
    print("You are short!")

a = True
b = False
if a & b:
    print("Both are true!")
if a | b:
    print("Either of them, or both, is true!")
if not a & b:
    print("Neither are true!")

number = int(input("Syötä numero: "))
if number > 0:
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
else:
    print("Number is negative!")

