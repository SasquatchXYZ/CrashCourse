names = ["Rick", "Robbie", "John", "Jason"]


def greet_user(name):
    message = f"Hello, {name.title()}!"
    print(message)


greet_user(names[0])
greet_user(names[1])
greet_user(names[2])
greet_user(names[3])
