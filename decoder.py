"""i wanna cry """
# Decryption table as a dictionary
decryption_table = {
    'a': 'H', 'b': 'a', 'c': 'I', 'd': 'b', 'e': 'J', 'f': 'c',
    'g': 'K', 'h': 'd', 'i': 'L', 'j': 'e', 'k': 'M', 'l': 'f',
    'm': 'N', 'n': 'g', 'o': 'O', 'p': 'h', 'q': 'P', 'r': 'i',
    's': 'Q', 't': 'j', 'u': 'R', 'v': 'k', 'w': 'S', 'x': 'l',
    'y': 'T', 'z': 'm', 'A': 'U', 'B': 'n', 'C': 'V', 'D': 'o',
    'E': 'W', 'F': 'p', 'G': 'X', 'H': 'q', 'I': 'Y', 'J': 'r',
    'K': 'Z', 'L': 's', 'M': '0', 'N': 't', 'O': '1', 'P': 'u',
    'Q': '2', 'R': 'v', 'S': '3', 'T': 'w', 'U': '4', 'V': 'x',
    'W': '5', 'X': 'y', 'Y': '6', 'Z': 'z', '0': '7', '1': 'A',
    '2': '8', '3': 'B', '4': '9', '5': 'C', '6': '.', '7': 'D',
    '8': ',', '9': 'E', ' ': 'G', '.': '?', ',': 'F', '?': ' '
}

# Length of the decryption table
cnt = len(decryption_table)

def decode(p_what):
    message = []

    for i in range(len(p_what)):
        if p_what[i] not in decryption_table:
            message.append(p_what[i])
            continue

        c = p_what[i]

        for j in range(i % cnt + 1):
            c = decryption_table[c]

        message.append(c)

    return ''.join(message)

# Example usage:
encoded_message = "some_encoded_message_here"
decoded_message = decode(encoded_message)
print("Decoded Message:", decoded_message)
