import pandas as pd
import random

df = pd.read_csv('data\general.csv')
w = df["word"]
index = random.randint(0, 18)
d = df["definition"]
word = w[index]
c = 0
letter = ""
lst = []
used = []
str = word
atmpts = 0

print(f"Hint: {d[index].capitalize()}")

for i in word:
    if i != " ":
        str = str.replace(i, "_")

print(str)

def checking():
    global atmpts
    global str
    lst = []
    if atmpts < 5 :
        letter = input("Enter a letter: ")
        if len(letter) == 1:
            if letter in word:
                if letter in used:
                    print("You've used the word once already. Try again")
                    checking()
                else:
                    for k,h in enumerate(word):
                        if(h == letter):
                            lst.append(k)
                    for j in lst:
                        str = str[:j] + letter + str[j+1:] 

                    print("You got a letter right")
                    print(str)

                    if str == word:
                        atmpts = 69

                    used.append(letter)

                    checking()  
                
            else:
                atmpts = atmpts + 1
                checking()
    
    elif atmpts == 69:
        print("You got the word right!")

    else:
        print("You're out of moves")
        print(f"The right word was {word}")

checking()

