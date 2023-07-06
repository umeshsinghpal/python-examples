myDict = {
    "fast": "In a Quick Manner",
    "krish": "A Team-member",
    "marks": [1, 2, 5],
    "anotherdict": {'krish': 'Player'},
    1: 2
}

# Dictionary Methods
#print(list(myDict.keys())) # Prints the keys of the dictionary
#print(myDict.values()) # Prints the keys of the dictionary 
#print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
'''
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "krish": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("krish")) # Prints value associated with key "krish"
print(myDict["krish"]) # Prints value associated with key "krish"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("krish2")) # Returns None as harry2 is not present in the dictionary
print(myDict["krish2"]) # throws an error as harry2 is not present in the dictionary

'''