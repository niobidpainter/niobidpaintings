#asking user for name, welcoming
name = input("What's your name? ")
print("Hello,", name + "! I am a Python script.", end=" ")
print("I am text on the same line.")
# adding the argument end = " " overrides the default end "\n" which would create a new line,
# now ending with a space and placing the next print function next to the prev text.