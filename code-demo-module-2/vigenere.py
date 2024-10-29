ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ''
    key_index = 0

    for char in plain_text:
        crypted_char_index = (ALPHABET.find(char) + ALPHABET.find(key[key_index % len(key)])) % len(ALPHABET)

        cipher_text += ALPHABET[crypted_char_index]

        key_index += 1

    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()

    decrypted_text = ''
    key_index = 0

    for char in cipher_text:
        decrypted_char_index = (ALPHABET.find(char) - ALPHABET.find(key[key_index % len(key)])) % len(ALPHABET)

        decrypted_text += ALPHABET[decrypted_char_index]
        
        key_index += 1

    return decrypted_text

if __name__ == '__main__':
    cipher_text = vigenere_encrypt('helloworld', 'abc')
    print(cipher_text)
    print(vigenere_decrypt('HFNLPYOSND', 'abc'))
