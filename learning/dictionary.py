prices = {
    "apple": 30,
    "banana": 10,
    "cherry": 50,
    "mango": 40
}
for key in prices.keys():
    print(key)

products = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000
}
for values in products.values():
    print(values)

employees = {
    "Aman": 25000,
    "Riya": 30000,
    "Rahul": 28000,
    "Simran": 35000
}
for key,values in employees.items():
    print(key, "earns" ,values)

marks = {
    "Aman": 80,
    "Riya": 90,
    "Rahul": 75,
    "Simran": 95
}
total = 0
for value in marks.values():
    total += value
print(total)

marks = {
    "Aman": 80,
    "Riya": 95,
    "Rahul": 75,
    "Simran": 90,
    "Karan": 85
}
count = 0
for value in marks.values():
    if value > 80:
        count += 1
print(count)

marks = {

    "Aman": 80,
    "Riya": 95,
    "Rahul": 75,
    "Simran": 90,
    "Karan": 85
}
highest = 0
topper =""
for key , value in marks.items():
    if value > highest:
        highest = value
        topper = key 
print(topper,highest)

