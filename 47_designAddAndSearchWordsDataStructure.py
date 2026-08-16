"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""

class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        
        current.is_word = True

    def search(self, word: str) -> bool:
        index = 0

        return self.__dfs(self.root, index, word)
    
    def __dfs(self, node, index, word):
        if index == len(word):
            return node.is_word

        if word[index] in node.children:
                return self.__dfs(node.children[word[index]], index+1, word)

        if word[index] == ".":
            for letter in node.children:
                if self.__dfs(node.children[letter], index+1, word):
                    return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)