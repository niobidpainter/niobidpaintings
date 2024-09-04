def main():
    name = input("Please enter your name: ")
    hello(name)

def hello(to="to you. Stand by - something has gone wrong."):
    print("Hello,", to)

main()