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

