with open("BadWords.txt", "r") as file:
    badwords = [line.strip().lower() for line in file]

def contains_badword(text):
    text = text.lower().split()
    for badword in badwords:
        if badword in text:
            return True
    return False


while True:
    user_input = input("Choose (coder/decoder/stop): ").lower()

    if user_input == "stop":
        break

    if user_input == "coder":
        while True:
            message = input("Text: ")
            if message == "stop":
                break

            if contains_badword(message):
                print("Message contains a banned word!")
                continue

            binary = " ".join(format(ord(c), "b") for c in message)
            print(binary)

    elif user_input == "decoder":
        while True:
            try:
                message = input("Binary text: ")
                if message == "stop":
                    break

                if contains_badword(message):
                    print("Message contains a banned word!")
                    continue

                text = "".join(chr(int(c, 2)) for c in message.split())
                print(text)

            except ValueError:
                print("Invalid binary input, try again")

    else:
        print("Unknown option, choose 'coder' or 'decoder'")
