numbers = [4, 9, 2, 7, 8, 1]
count = 0
for num in numbers:
    if num >5:
        count+=1
print(count)

numbers = [3, 6, 9, 12, 15, 18]
even =[]
for num in numbers:
    if num % 2 ==0:
        even.append(num)
print(even)

word = "education"
count = 0
for ch in word :
    if ch == "a" or ch == "e" or  ch == "i" or ch == "o" or ch == "u":
        count+=1
print(count)

numbers = [12, 5, 8, 20, 3, 17]
count = 0
new =[]
for num in numbers :
    if 5<=num<=15:
        count+=1
        new.append(num)
print(count)
print(new) 

text = "Rs 1,299 only"
number =""
for ch in text:
    if ch.isdigit():
        number +=ch
print(number)

numbers = [3, 11, 7, 2, 15, 6]
short = 0
long = 0
for ch in numbers:
    if ch >= 8:
        long += 1
    elif ch < 8:
        short += 1
print("short:",short)
print("long:",long)

numbers = [10, 25, 30, 45, 50]
new = []
for a in numbers:
    if a >= 30:
        b=a+(a/10)
        new.append(b)
print(new)

numbers = [7, 4, 9, 4, 2, 7, 4]
list =[]
for a in numbers:
    if a > numbers[0]:
        list.append(a)
print(list)

numbers = [15, 22, 8, 40, 11, 30]
sum = 0
count = 0
average = 0
count =0
for a in numbers:
    sum = sum + a
    numcount += 1
average = sum/numcount
for a in numbers:
    if a > average:
        count +=1

print("average:",average)
print("count:",count)

word ="Hello World 2024"
new =""
for ch in word:
    if ch.isdigit():
        new = new +"#"
    else :
        new = new + ch
print(new)

