import sys

def decode_cipher(ciphertext, codebook):
    """
    Decodes the ciphertext using a provided codebook, preserving character case.
    """
    plaintext = ""
    for char in ciphertext:
        if 'a' <= char.lower() <= 'z':
            # Check for the lowercase version in the codebook
            decoded_char = codebook.get(char.lower())
            if decoded_char:
                if char.isupper():
                    plaintext += decoded_char.upper()
                else:
                    plaintext += decoded_char
            else:
                # If a character is not in the codebook, keep it as is.
                plaintext += char
        else:
            # Append non-alphabetic characters directly.
            plaintext += char
    return plaintext

def main():
    # Define the codebook exactly as it is in the C++ file.
    codebook = {
        'a': 'c', 'b': 'i', 'c': 'o', 'd': 'v', 'e': 'y', 'f': 'b', 'g': 'l', 'h': 'k', 'i': 'f', 
        'j': 't', 'k': 'q', 'l': 'm', 'm': 'a', 'n': 'd', 'o': 'z', 'p': 'h', 'q': 'p', 'r': 's', 
        's': 'j', 't': 'n', 'u': 'u', 'v': 'r', 'w': 'g', 'x': 'e', 'y': 'w', 'z': 'x'
    }

    if len(sys.argv) != 2:
        print("Warning: need exactly one command line argument.")
        print("Usage:", sys.argv[0], "<input_file_name>")
        sys.exit(1)

    input_file_name = sys.argv[1]

    try:
        with open(input_file_name, 'r') as in_file:
            whole_file = in_file.read()
    except IOError:
        print(f"Warning: cannot open file named {input_file_name}!")
        sys.exit(2)

    plaintext = decode_cipher(whole_file, codebook)

    print("Codebook Pairings:")
    for key, value in codebook.items():
        print(f"{key}->{value}")

    print("\n")
    print("deciphered plaintext:")
    print(plaintext)

if __name__ == "__main__":
    main()