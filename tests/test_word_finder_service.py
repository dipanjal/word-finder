import unittest

from word_finder.ds.trie import Trie
from word_finder.word_finder import WordFinder


class TestWordFinder(unittest.TestCase):

    def test_generate_word(self):
        # Example usage
        puzzle_str = "SHITG"
        letter_list = list(puzzle_str)
        word_range = 4, 4
        meaningful_words = WordFinder().generate_words(letter_list, word_range)

        # assertions
        self.assertTrue(len(meaningful_words) > 0)
        for word in meaningful_words:
            self.assertTrue(len(word) == 4)

        # check contains
        self.assertIn("this", meaningful_words)
        self.assertIn("hist", meaningful_words)
        self.assertIn("gist", meaningful_words)
        self.assertNotIn("sight", meaningful_words)

    def test_unmasking_words(self):
        # Example usage
        puzzle_str = "SHITG"
        masked_word = "_H_S"  # THIS
        unmasked_words = WordFinder().unmask_word(
            available_letters=list(puzzle_str),
            masked_word=masked_word
        )

        # assertions
        self.assertTrue(len(unmasked_words) > 0)
        for word in unmasked_words:
            self.assertTrue(len(word) == 4)

        # check contains
        self.assertIn("this", unmasked_words)

    def test_trie(self):
        unmasked_words = ["THIS", "THIG", "HIST", "GIST"]
        masked_word = "_H_S"  # THIS
        trie = Trie()
        for word in unmasked_words:
            trie.insert(word)
        words = trie.find_matching_words(masked_word)
        self.assertIn("THIS", words)
