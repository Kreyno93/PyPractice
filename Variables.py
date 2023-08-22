myValue = 1
print(myValue)

print (str(myValue) + " is of type " + str(type(myValue)))


## Float data type

myValue = 3.14
print(myValue)
print (type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))

## Complex data type

myValue = 5j
print(myValue)
print (type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))

## Boolean data type

myValue = True
print(myValue)
print (type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))

myValue = False
print(myValue)
print (type(myValue))
print(str(myValue) + " is of type " + str(type(myValue)))


## String data type

myString = "This is a string"
print(myString)
print (type(myString))
print(str(myString) + " is of type " + str(type(myString)))

## String concatenation

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

## Input Strings

name = input("What is your name? ")
print("Hello " + name + "!")

## Output Strings

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name, color, animal))