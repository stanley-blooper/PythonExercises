


word = input("What is your choice of word(s)? ")
letter = input("What letter are we looking for? ")
count = 0
countlet=0
for char in word:
    if char == letter:
        count +=1

for char in word:
    countlet +=1
 
if countlet >=50:
    print (f"There are {count}'s {letter} in the string, \n{word}")
else:
    print(f"There are {count}'s {letter} in the string, {word}")

"""
Theres also a count function
count()
attach the string, which would be word along with a "." with the function and within the function you type the specific letter you are trying to find.
word.count(letter).

In this example, we used the for loop route. Breaking down the string through char(s).


word =input("Enter Text: ")
letter = input("Enter letter you are counting: ")

count = word.count(letter)
print(f"There are {count}'s {letter} in the text")





"""
