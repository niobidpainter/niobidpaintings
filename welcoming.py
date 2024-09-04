def main():
    name = input("Please enter your name: ")
    name = name.strip()

    # unique message if name is a number or UPPER
    if name.isdigit():
        print("\nH3ll0,", name + ", beep boop.\n")
    elif name.isupper():
        print("\nHELLO,", name + ", HOW DO YOU DO?\nA fan of capital letters?\n")
    else:
        hello(name)

def hello(to="to you. Stand by - something has gone wrong."):
    print("\nHello,", to + ".\n")

main()