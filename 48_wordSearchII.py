"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""

class Node:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root

        for ch in word:
            if ch not in root.children:
                root.children[ch] = Node()
            root = root.children[ch]

        root.word = True   


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.rows = len(board)
        self.cols = len(board[0])
        self.ans = {}

        for word in words:
            self.trie.insert(word)

        def dfs(board, i, j, path, root):
            ch = board[i][j]

            # Check if current character is in trie
            root = root.children.get(ch)
            if root is None:
                return

            # Update path and mark visited
            path = path + [ch]
            board[i][j] = None

            # Add to solution if node is marked as a word in trie
            if root.word:
                word = ''.join(path)
                self.ans[word] = True

            # Right
            if j + 1 < self.cols and board[i][j+1]:
                dfs(board, i, j+1, path, root)

            # Left
            if j - 1 >= 0 and board[i][j-1]:
                dfs(board, i, j-1, path, root)

            # Down
            if i + 1 < self.rows and board[i+1][j]:
                dfs(board, i+1, j, path, root)

            # Up
            if i - 1 >= 0 and board[i-1][j]:
                dfs(board, i-1, j, path, root)
            
            board[i][j] = ch
        
        for i in range(self.rows):
            for j in range(self.cols):
                dfs(board, i, j, [], self.trie.root)

        return self.ans.keys()