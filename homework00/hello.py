def get_greeting(name):
    text = "Hello, {name}!".format(name=name) 
    return text


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
