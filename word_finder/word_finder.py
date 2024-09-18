import itertools

import nltk
from nltk.corpus import words

from word_finder.ds.trie import Trie

MIN_WORD_LEN = 2

class WordFinder:

    def __init__(self):
        # self.trie = Trie()
        nltk.download('words', quiet=True)


    def unmask_word(self, masked_word, available_letters):
        if len(masked_word) < MIN_WORD_LEN:
            return []

        # Convert input to lowercase for consistency
        masked_word = masked_word.lower()

        # get if there is any prefix available
        prefix = masked_word[0] if masked_word[0] != "_" else None

        # Generate words of the same length as the masked word
        possible_words = self.generate_words(
            available_letters,
            word_length_range=(len(masked_word), len(masked_word)),
            prefix=prefix,
        )

        # Build Trie and find matching words
        # TODO: Need optimization here, maybe we can cache trie data
        trie = Trie()
        for word in possible_words:
            trie.insert(word)

        unmasked_words = trie.find_matching_words(masked_word)

        return unmasked_words


    def generate_words(self, letters, word_length_range=None, prefix=None):
        # Convert input to lowercase for consistency
        letters = [letter.lower() for letter in letters]

        if word_length_range == (0, 0):
            word_length_range = None

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
