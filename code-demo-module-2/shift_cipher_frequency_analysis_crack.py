import matplotlib.pyplot as plt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    text = text.upper()

    letters_frequency = dict.fromkeys(ALPHABET, 0)

    for letter in text:
        if letter in ALPHABET:
            letters_frequency[letter] += 1

    return letters_frequency

def shift_cipher_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()

    decrypted_text = ''

    for char in cipher_text:
        char_index = ALPHABET.find(char)

        decrypted_char_index = (char_index - key) % len(ALPHABET)

        decrypted_text += ALPHABET[decrypted_char_index]

    return decrypted_text

def shift_cipher_frequency_analysis_crack(cipher_text):
    frequencies = frequency_analysis(cipher_text)
    most_frequent_letter = max(frequencies.items(), key=lambda item: item[1])[0]
    
    # clé = valeur de la lettre la plus fréquente du message chiffré - valeur de E
    key = ALPHABET.find(most_frequent_letter) - ALPHABET.find('E')
    print(f'Possible key = {key}')
    print(f'Decrypted message: {shift_cipher_decrypt(cipher_text, key)}')

def main():
    cipher_text = "NUCKBKXZNOYMOBKYZNKLXKWAKTIEULRKZZKXYOTKTMROYNZKDZCNOINOYJUSOTGZKJHEGXKRGZOBKREYSGRRTASHKXULIUSSUTCUXJY"
    shift_cipher_frequency_analysis_crack(cipher_text)


if __name__ == '__main__':
    main()
