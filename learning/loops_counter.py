Sentence = "cat is just like dog"
length = 0
for ch in Sentence:
    if ch == " ":
        print(length)
        length = 0
    else:
        length +=1
print(length)


sentence = "one two three four"
words = 0
for ch in sentence:
    if ch == " ":
        words +=1
words +=1
print(words)

sentence = "go for it"
length = 0
for ch in sentence:
    if ch == " ":
        print(length)
        length = 0
    else :
        length +=1
print(length)

sentence = "a lovely sunny day"
length = 0
short = 1000
for a in sentence:
    if a == " ":
        if length < short and length >0:
            short = length
            length = 0
    else :
        length +=1
if length < short and length >0:
    short = length 

print(short)

sentence = "keep on coding"
length = 0
count = 0
for ch in sentence:
    if ch == " ":
        count = count + length 
        length = 0
    else:
        length +=1
count = count + length
print(count)

sentence = "the cat sat on a big mat"
length = 0  
count = 0
for a in sentence :
    if a ==" ":
        if length == 3:
            count += 1
        length = 0
    else :
        length +=1
if length == 3:
    count +=1
print(count)

sentence = "an apple or a orange"
count =  0
length = 0
for a in sentence:
    if a == " ":
        length = 0
    elif a == "a" or a == "e" or a == "i" or a == "o" or a=="u":
        count += 1
    else:
        length +=1
print(count)

sentence = "short and simple words"
length =0
count = 0
total_length = 0
for a in sentence:
    if a == " ":
        count +=1
        total_length += length
        length =0
    else :
        length +=1
count += 1
total_length += length
print (total_length / count)

