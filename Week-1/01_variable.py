#string datatype
test_string = "Cohort"

#Integer datatype
test_int = 345

#Float datatype
test_float = 45.32

#Boolean datatype
test_bool = False

#Multiline String
test_multiline_string = """This is
a 
multiline
     String"""


# Printing the variables
print(test_string)
print(test_int)
print(test_float)
print(test_bool)
print(test_multiline_string)

# Printing the type of variables
print(type(test_string))
print(type(test_int))
print(type(test_float))
print(type(test_bool))
print(type(test_multiline_string))

"""Following example shows how in Python variables are just name which point to id of value stored in memory. When the variable is associated with 
another value the previous value is automatically released."""

test_value = "123"

print("ID of the value 123 is ",id("123"))
print("ID of the value variable test_value is ",id(test_value))

test_value = "HCL"

print("ID of the value HCL is ",id("HCL"))
print("ID of the value variable test_value is ",id(test_value))
