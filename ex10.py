#defined x,y
x = 0
y = 0
#Fizzbuzz definition
def Fizzbuzz(x,y):
    """
    Input x to be positive from 1 to 100
    Return Fizz buzz
    """
#inputs
x = int(input("Minimum Value:"))
y = int(input("Maximum Value:"))
#Condition
for n in range(x,y+1):
    if (n % 3 == 0 ) and (n % 5 == 0):
        print("Fizzbuzz")
    elif (n % 3 == 0):
        print("fizz")
    elif (n % 5 == 0):
        print("buzz")
    else:
        print(n)
#Fizzbuzz
