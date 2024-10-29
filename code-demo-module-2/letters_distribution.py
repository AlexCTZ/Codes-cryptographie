import matplotlib.pyplot as plt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    text = text.upper()

    letters_frequency = dict.fromkeys(ALPHABET, 0)

    for letter in text:
        if letter in ALPHABET:
            letters_frequency[letter] += 1

    return letters_frequency

def main():
    # frequencies = frequency_analysis('Hello tout le monde. Promis dernier exemple.')
    # plt.bar(frequencies.keys(), frequencies.values())
    # plt.show()

    frequencies = frequency_analysis('NUCKBKXZNOYMOBKYZNKLXKWAKTIEULRKZZKXYOTKTMROYNZKDZCNOINOYJUSOTGZKJHEGXKRGZOBKREYSGRRTASHKXULIUSSUTCUXJY')
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()

if __name__ == '__main__':
    main()
