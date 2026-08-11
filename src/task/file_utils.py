def save_and_read_notes(filename, note):
    with open(filename, "a") as writer:
        writer.write(note + "\n")


def show_last_notes(filename, limit=5):
    with open(filename, "r") as reader:
        lines = reader.readlines()[-limit:]
        print("Last notes:")
        for line in lines:
            print(line.strip())
