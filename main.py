# This will be a simple caesar cipher program

# ====================== DEFINING FUNCTIONS ======================

# FUNCTION THAT ALLOWS TO CHOOSE REGIME
def choose_regime():
    print("Choose regime: encode or decode")
    while True:
        regime = input("Enter regime: ")
        regime = regime.lower()
        if regime == "encode" or regime == "decode":
            return regime
        else:
            print("Wrong regime. Try again.")

#  TAKE A MESSAGE TO ENCODE AND DECODE FUNCTION


def get_message(regime):
    message = input(f"Enter the message you want to {regime}: ")
    return message.lower()

# TAKE A KEY


def get_key():
    key = int(input("Enter the key: "))
    return key

# ENCODE AND DECODE FUNCTION


def encode_decode(message, key, regime):
    if regime == "decode":
        key = -key

    message_output = ""
    for letter in message:
        if letter == " ":
            message_output += letter
        else:
            message_output += chr((ord(letter) + key - 97) % 26 + 97)
    return message_output

# REPLAY FUNCTION


def replay():
    replay = input("Do you want to encode or decode another message? (y/n): ")
    return replay.lower().startswith("y")


# ============================= PROGRAM LOGIC =============================

while True:

    regime = choose_regime()
    message = get_message(regime)
    key = get_key()
    message_output = encode_decode(message, key, regime)

    print(f"The message is: {message_output}")

    if not replay():
        break
