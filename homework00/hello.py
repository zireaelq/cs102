def get_greeting(name: str) -> str:
    if name == "World":
        text = "Hello, World!"
    if name == "Anonymous":
        text = "Hello, Anonymous!"
    return text


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
