# asking user for name
name = input("What's your name? ")
name = name.strip()

# if some silly goose puts their name as a digit, recieve this message instead.
if name.isdigit() == True:
    print("H3ll0,", name + ", b33p b00p. I am a python script.")

# if some silly goose wants their name in all caps (Sorry JJ)
elif name.isupper():
    print("HELLO,", name, "HOW DO YOU DO? Fan of capital letters?")

# welcoming by name
else:
    print("Hello,", name + "! I am a Python script.", end=" ")
    print("I am text on the same line.")
# adding the argument end = " " overrides the default end "\n" which would create a new line,
# now ending with a space and placing the next print function next to the prev text.

# for SOME reason telling python to format {name} as a string can be used too.
print(f"\nwho are you, {name}, who am i to you?")