print("Welcome to the love calculator")

name1 = input("What is your name?")
name2 = input("What is your partner's name?")

#name1 and name2 as one word
combined_names = name1 + name2
lower_names = combined_names.lower()
#names_length = len(lower_names)

#check the times of the letters occurrences for the word true love
#t = lower_names.count("t")
#r = lower_names.count("r")
#u = lower_names.count("u")
#e = lower_names.count("e")
#first_digit = t + r + u + e

#l = lower_names.count("l")
#o = lower_names.count("o")
#v = lower_names.count("v")
#e = lower_names.count("e")
#second_digit = l + o + v + e

firstWord = "true"
secondWord = "love"

first_digit = 0
second_digit = 0

for letter in lower_names:
    if letter in firstWord:
        first_digit += 1

    if letter in secondWord:
        second_digit += 1

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")