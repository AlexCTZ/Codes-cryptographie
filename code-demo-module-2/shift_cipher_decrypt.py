ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

KEY = 6

def shift_cipher_decrypt(cipher_text):
    cipher_text = cipher_text.upper()

    decrypted_text = ''

    for char in cipher_text:
        char_index = ALPHABET.find(char)

        decrypted_char_index = (char_index - KEY) % len(ALPHABET)

        decrypted_text += ALPHABET[decrypted_char_index]

    return decrypted_text

def main():
    print(shift_cipher_decrypt('NUCKBKXZNOYMOBKYZNKLXKWAKTIEULRKZZKXYOTKTMROYNZKDZCNOINOYJUSOTGZKJHEGXKRGZOBKREYSGRRTASHKXULIUSSUTCUXJY'))

if __name__ == '__main__':
    main()
