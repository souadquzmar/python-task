def read_raw_input(prompt=""):
    return input(prompt)


def get_user_info():
    name = read_raw_input("Name : ").strip().title()
    topic = read_raw_input("Topic : ").strip()

    return f"Hello {name}! Welcome to learning {topic}."
