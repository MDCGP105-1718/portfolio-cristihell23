#Random numbers generator
from random import randint
#Random number radius
x = randint (1, 100)
count = 0
guess = 0
#Guessing definition
def guessing (guess,count):

    """
    Try to guess the corect number!
    This counts how many time you tried!
    Try now!
    """

#While Condition
while guess !=x:
    guess = int(input("Put your lucky Number:"))
    count+=1
    if (guess < x):
        print("The number is lower, put a higher one.")
    elif (guess > x):
        print("The number is higher , put a lower one.")
    if (guess == x):
        print ("Congratulation , you've guessed the number")
        print ("You found the number in", count)
#Fizzbuzz
