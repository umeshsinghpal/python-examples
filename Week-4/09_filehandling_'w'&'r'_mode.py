f = open("demot1.txt", "w")
f.write("Welcome to the session")
f.close()

f = open("demot1.txt", "r")
print(f.read())
f.close()