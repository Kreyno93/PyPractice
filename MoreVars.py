
## List, Tuples, Dictionaries
# List: ordered, changeable, allows duplicate members
myFruits = ["apple", "banana", "cherry"]
print(myFruits)
print (type(myFruits))

print(myFruits[0])
print(myFruits[1])
print(myFruits[2])

myFruits[2] = "orange"
print(myFruits)

# Tuple: ordered, unchangeable, allows duplicate members
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print (type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# myFinalAnswerTuple[2] = "orange" # This will fail because tuples are unchangeable

# Dictionary: unordered, changeable, indexed, no duplicate members

myFavouriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print("This is my Dict " + str(myFavouriteFruitDictionary))

print(type(myFavouriteFruitDictionary))

print(myFavouriteFruitDictionary["Akua"])
print(myFavouriteFruitDictionary["Saanvi"])
print(myFavouriteFruitDictionary["Paulo"])