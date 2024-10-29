ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift_cipher_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()

    decrypted_text = ''

    for char in cipher_text:
        char_index = ALPHABET.find(char)

        decrypted_char_index = (char_index - key) % len(ALPHABET)

        decrypted_text += ALPHABET[decrypted_char_index]

    return decrypted_text


def brute_force_shift_cipher(cipher_text):
    for key in range(len(ALPHABET)):
        print(f'key = {key}, decrypted_text = {shift_cipher_decrypt(cipher_text, key)}')

def main():
    brute_force_shift_cipher('KHOOR')

if __name__ == '__main__':
    main()
