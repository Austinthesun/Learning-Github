def greeting():
    name = input("What is your name")
    if not name:
        print("Good morning nameless one")
    else:
        print(f"Good morning {name}")


if __name__ == '__main__':
    greeting()
