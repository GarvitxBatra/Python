while True:
    age = input()
    if age.isdigit():
        age = int(age)
        print("Accepted:",age)
        break
    else :
        print("Invalid Number")

for a in range(0,3):
    number = input("Enter a Number:")
    if number.isdigit():
        number = int(number)
        print(number)
        break
    else:
        print("Invalid Number")
else:
    print("Maximum attempts reached")

while True:
    want = input("yes or no :")
    if want == "yes" or want == "no":
        print(want)
        break
    else :
        print("Invalid choice")

while True:
    name = input("enter your name :",)
    if name.strip() == "":
        print ("Name cannot be empty")
    else:
        print("Welcome,",name)
        break

while True:
    ask = input()
    if ask =="Yes" or ask =="yes" or ask == "YES" or ask=="NO" or ask == "No" or ask =="no":
        print(ask)
        break
    else:
        print("Invalid choice")

while True:
    age = input()
    if age.isdigit():
        age = int(age)
        if age >18 and age <60:
            print("Eligible")
        else:
            print("Not Eligible")
        break
    else:
        print("Invalid input")

for a in range(3):
    age = input()
    if age.isdigit():
        age = int(age)
        if age >= 18 and age <=60:
            print("Eligible")
        else :
            print("Not Eligible")
        break
    else:
        print("Invalid input")
else:
    print("Maximum attempts reached")

for a in range(3):
    password = input()
    if password == "python123":
            print("Login successful")
            break
    else :
        print("Incorrect password")
else:
    print("Maximum attempts reached")
