import nltk

import itertools
import nltk
from nltk.corpus import words

from trie import Trie

MIN_WORD_LEN = 2


def unmask_word(masked_word, available_letters):
    # Convert input to lowercase for consistency
    masked_word = masked_word.lower()

    # Generate words of the same length as the masked word
    possible_words = generate_words(
        available_letters,
        word_length_range=(len(masked_word), len(masked_word))
    )

    # Build Trie and find matching words
    trie = Trie()
    for word in possible_words:
        trie.insert(word)

    unmasked_words = trie.find_matching_words(masked_word)

    return unmasked_words


def generate_words(letters, word_length_range=None, prefix=None):
    # Convert input to lowercase for consistency
    letters = [letter.lower() for letter in letters]

    # Generate all possible combinations within the specified range
    if word_length_range:
        min_length, max_length = word_length_range
        combinations = []
        for i in range(min_length, max_length + 1):
            combinations.extend(itertools.permutations(letters, i))
    else:
        combinations = []

        for i in range(MIN_WORD_LEN, len(letters) + 1):
            combinations.extend(itertools.permutations(letters, i))

    # Convert combinations to words
    possible_words = [''.join(combo) for combo in combinations]

    # Filter for meaningful words using NLTK's words corpus
    english_words = set(word.lower() for word in words.words())
    meaningful_words = [word for word in possible_words if word in english_words]

    # Filter words starting with the given prefix, if provided
    if prefix:
        prefix = prefix.lower()
        meaningful_words = [word for word in meaningful_words if word.startswith(prefix)]

    return meaningful_words


# Example usage remains the same


def init_nltk():
    # Download words if not already downloaded
    nltk.download('words', quiet=True)


def main():
    init_nltk()

    # Example usage
    puzzle_str = "SIGHT"
    letter_list = list(puzzle_str)
    # word_range = 4, 4
    # meaningful_words = generate_words(letter_list, word_range)

    unmasked_word = unmask_word(masked_word="_H_S", available_letters=letter_list)
    print("Meaningful words:", unmasked_word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
