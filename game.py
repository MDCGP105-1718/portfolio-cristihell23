print("One night , you get out with your friend in a pub , you get wasted , Somehow You get Home.")
print("The next day you woke up , you realise that this is not your house and you are not alone.")
print("Find out What's Happening!")
print("Room 1")
print("You Should Look Around.")

Action = input("What Will You Do Next?:")

if Action == ("look around"):
     print ("You see a table , a chair and a door.")
     print ("Yourself:Should I Try To Move The Table? Maybe the Chair? Or I Might Even Break The Door.")
if Action == ("move table"):
     print ("You Move The Table")
     print ("Yourself:I Can See Something , It Looks Like A Key")
     print ("You Now Have A Key.")
elif Action == ("move chair"):
     print ("You Move The Chair")
     print ("Yourself:I Moved The Chair , Found Nothing , Did That Really Worth?")
elif Action == ("break door"):
     print ("You Did It , But Is That Really Ok?")
     print ("Yourself:I Broke The Door , I Feel Insecure.")
     print ("I should procced to the next room.")
else:
     print ("This Is Not A Valid Action!")
