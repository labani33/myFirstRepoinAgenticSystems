def greet_person(name):
    message = f"Hello, {name}!"
    return message

user_name = input("Enter your name: ")
result = greet_person(user_name)
print(result)