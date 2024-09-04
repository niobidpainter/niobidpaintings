def main():
    name = input("Please enter your name: ")
    name = name.strip()

    # unique message if name is a number
    if name.isdigit():
        print("H3ll0,", name + ", b33p b00p.")
    else:
        hello(name)

def hello(to="to you. Stand by - something has gone wrong."):
    print("Hello,", to + ".")

main()