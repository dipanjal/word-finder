# Filter words that match the masked pattern using a custom Trie implementation
class TrieNode:
    def __init__(self, val: str = "<ROOT>"):
        self.val = val
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(f"<{char}>")
            node = node.children[char]
        node.is_end = True

    # def find_matching_words(self, masked_word):
    #     def dfs(node, index, current_word):
    #         if index == len(masked_word):
    #             if node.is_end:
    #                 matching_words.append(current_word)
    #             return
    #
    #         if masked_word[index] == '_':
    #             for char, child in node.children.items():
    #                 dfs(child, index + 1, current_word + char)
    #         elif masked_word[index] in node.children:
    #             dfs(node.children[masked_word[index]], index + 1, current_word + masked_word[index])
    #
    #     matching_words = []
    #     dfs(self.root, 0, '')
    #     return matching_words

    def find_matching_words(self, masked_word):
        stack = [(self.root, 0, "")]
        matching_words = []

        # DFS in word tree
        while stack:
            node, index, current_word = stack.pop()

            if index == len(masked_word):
                if node.is_end:
                    matching_words.append(current_word)
                continue

            if self._is_masked(masked_word[index]):
                for char, child in node.children.items():
                    stack.append((child, index + 1, current_word + char))
            elif masked_word[index] in node.children:
                curr_char = masked_word[index]
                child = node.children[curr_char]
                stack.append((child, index + 1, current_word + curr_char))

        return matching_words

    def _is_masked(self, value: str) -> bool:
        return value == "_"

# Breakdown of this code ::find_matching_words::
    # Initial state:
    # Stack: [(root, 0, '')]
    # Masked word: "_H_S"
    #
    # Step 1:
    # Pop: (root, 0, '')
    # Push: (child_T, 1, 'T'), (child_I, 1, 'I'), (child_H, 1, 'H'), (child_S, 1, 'S')
    # Stack: [(child_S, 1, 'S'), (child_H, 1, 'H'), (child_I, 1, 'I'), (child_T, 1, 'T')]
    #
    # Step 2:
    # Pop: (child_T, 1, 'T')
    # Push: (child_H, 2, 'TH')
    # Stack: [(child_H, 2, 'TH'), (child_S, 1, 'S'), (child_H, 1, 'H'), (child_I, 1, 'I')]
    #
    # Step 3:
    # Pop: (child_H, 2, 'TH')
    # Push: (child_I, 3, 'THI'), (child_S, 3, 'THS')
    # Stack: [(child_S, 3, 'THS'), (child_I, 3, 'THI'), (child_S, 1, 'S'), (child_H, 1, 'H'), (child_I, 1, 'I')]
    #
    # Step 4:
    # Pop: (child_S, 3, 'THS')
    # Push: (leaf, 4, 'THIS')
    # Stack: [(leaf, 4, 'THIS'), (child_I, 3, 'THI'), (child_S, 1, 'S'), (child_H, 1, 'H'), (child_I, 1, 'I')]
    #
    # Step 5:
    # Pop: (leaf, 4, 'THIS')
    # Add 'THIS' to matching_words
    # Stack: [(child_I, 3, 'THI'), (child_S, 1, 'S'), (child_H, 1, 'H'), (child_I, 1, 'I')]
    #
    # ... (continue until stack is empty) ...
    #
    # Final state:
    # Stack: []
    # Matching words: ['THIS']
