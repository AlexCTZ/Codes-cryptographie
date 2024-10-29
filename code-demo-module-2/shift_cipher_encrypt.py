ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

KEY = 3

def shift_cipher_encrypt(plain_text):
    plain_text = plain_text.upper()

    cipher_text = ''

    for char in plain_text:
        char_index = ALPHABET.find(char)

        encrypted_char_index = (char_index + KEY) % len(ALPHABET)

        cipher_text += ALPHABET[encrypted_char_index]

    return cipher_text


# def shift_cipher_encrypt(plain_text):
#     return ''.join(ALPHABET[(ALPHABET.find(char) + KEY) % len(ALPHABET)] for char in plain_text.upper())

def main():
    print(shift_cipher_encrypt('hello'))

if __name__ == '__main__':
    main()
