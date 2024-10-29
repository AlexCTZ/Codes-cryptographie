english_words = set()

def load_dictionary():
    with open('english_words_sample.txt', 'r') as f:
        for word in f:
            english_words.add(word.strip())


def count_matches(text):
    text = text.upper()

    words = text.split(' ')

    matches = 0

    for word in words:
        if word in english_words:
            matches += 1

    return matches

def check_if_text_is_english_or_not(text):
    words_found_in_dictionary = count_matches(text)
    total_words = len(text.split(' '))

    return (words_found_in_dictionary / total_words) * 100 >= 60

if __name__ == '__main__':
    load_dictionary()
    print(check_if_text_is_english_or_not('hello world I am here with my friends'))
