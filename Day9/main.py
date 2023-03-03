def encode_message(message, key):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            shift = key % 26
            if letter.isupper():
                encoded_message += chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                encoded_message += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            encoded_message += letter
    return encoded_message


def decode_message(encoded_message, key):
    decoded_message = ""
    for letter in encoded_message:
        if letter.isalpha():
            shift = key % 26
            if letter.isupper():
                decoded_message += chr((ord(letter) - 65 - shift) % 26 + 65)
            else:
                decoded_message += chr((ord(letter) - 97 - shift) % 26 + 97)
        else:
            decoded_message += letter
    return decoded_message


message = input("Enter the message to encode or decode: ")
key = input("Enter the key value (1-25): ")

while not key.isdigit() or int(key) < 1 or int(key) > 25:
    print("Invalid key! Please enter a number between 1 and 25.")
    key = input("Enter the key value (1-25): ")
key = int(key)

choice = input("Enter 'E' to encode the message, 'D' to decode the message: ")
if choice == "E":
    encoded_message = encode_message(message, key)
    print("Encoded message:", encoded_message)
elif choice == "D":
    decoded_message = decode_message(message, key)
    print("Decoded message:", decoded_message)
else:
    print("Invalid choice!")
