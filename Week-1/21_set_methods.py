# Creating an empty set
emptySet = set()
print(type(emptySet))

## Adding values to an empty set
emptySet.add(4)
emptySet.add(4)
emptySet.add(5)
emptySet.add(5) # Adding a value repeatedly does not changes a set
emptySet.add((4, 5, 6))

## Accessing Elements
# emptySet.add({4:5}) # Cannot add list or dictionary to sets
print(emptySet)

## Length of the Set
print(len(emptySet)) # Prints the length of this set

## Removal of an Item
emptySet.remove(5) # Removes 5 fromt set emptySet
# emptySet.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(emptySet)

print(emptySet.pop())
print(emptySet)
