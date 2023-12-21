def get_key(operator: str, char1: str, char2: str, message: str) -> int:
    ''' Outputs the key for the decrypt function. It finds the first ocurrence
    of the first char, then finds the first ocurrence of the second one after
    the first, then uses the operator to get the decryption key.
    '''
    for i in range(len(message)):
        if message[i] in char1:
            index1 = i
            break
    for j in range(index1, len(message)):
        if message[j] in char2:
            index2 = j
            break
    if operator == "*":
        return index1 * index2
    elif operator == "+":
        return index1 + index2
    elif operator == "-":
        return index1 - index2


def decrypt(key: int, message: str) -> list:
    ''' Outputs the decrypted message. It performs the subtraction funtion between
    the key and each character of the message string to return a printable ASCII
    character.
    '''
    ascii_message = []
    for i in message:
        ascii_message.append(ord(i))
    for i in range(len(ascii_message)):
        ascii_message[i] = ascii_message[i] + key
        while ascii_message[i] > 126:
            ascii_message[i] = ascii_message[i] - 95
        while ascii_message[i] < 32:
            ascii_message[i] = ascii_message[i] + 95
        ascii_message[i] = chr(ascii_message[i])
    return ascii_message


if __name__ == "__main__":
    operator = input()

    #Getting the char1 and char2 strings if something other than a character is inputed.
    char1 = input()
    if char1 == "vogal":
        char1 = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    elif char1 == "consoante":
        char1 = ["b", "c", "d", "f", "g", "h", "i", "j", "h", "k", "l", "m", "n", "p",
                 "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "J",
                 "H", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y",
                 "Z"]
    elif char1 == "numero":
        char1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char2 = input()
    if char2 == "vogal":
        char2 = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    elif char2 == "consoante":
        char2 = ["b", "c", "d", "f", "g", "h", "i", "j", "h", "k", "l", "m", "n", "p",
                 "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "J",
                 "H", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y",
                 "Z"]
    elif char2 == "numero":
        char2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    #Getting and concatenating all the messages to then find the key for the decryption.
    number_of_messages = int(input())
    all_messages= []
    all_messages_concaneted = ""
    for i in range(number_of_messages):
        message = input()
        all_messages_concaneted = all_messages_concaneted + message
        all_messages.append(message)
    key = get_key(operator, char1, char2, all_messages_concaneted)
    print(key)

    #Decrypting every message individually.
    for i in range(number_of_messages):
        decrpyted_message = decrypt(key, all_messages[i])
        for i in decrpyted_message:
            print(i, end="")
        print()
