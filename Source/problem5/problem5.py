
# Represents a single node in the Trie
from ipywidgets import interact
from IPython.display import display
from ipywidgets import widgets


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        arr = []
        for key, value in self.children.items():
            if value.is_word:
                arr.append(suffix + key)
                if len(value.children) != 0:
                    arr += value.suffixes(suffix + key)
            else:
                arr += value.suffixes(suffix + key)
        return arr


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.insert(char)
            current = current.children[char]
        current.is_word = True

    def find(self, prefix):
        return self.root.children.get(prefix)


MyTrie = Trie()
wordList = [
    "ant", "anthology", "ntagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')

# f => expect : [un,unction,actory]
# t => expect : [rie,rigger,rigonometry,ripod]
# a => expect : [nthology,antagonist,ntonym]
