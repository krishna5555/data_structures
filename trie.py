#Building Trie using python

#creating a node
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=false

class Trie:
    def __init__(self):
        self.root=self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    def insert(self,key):
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index]=self.getNode()
            pCrawl=pCrawl.children[index]
        pCrawl.isEndOfWord=True
    def search(self,key):
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl=pCrawl.children[index]
        return pCrawl!=None and pCrawl.isEndOfWord

#t-number of test cases
t=int(input())
for g in range(t):
    n=int(input())
    ls=list(map(str,input().split(" ")))
    x=input()
    t=Trie()
    for g in ls:
        t.insert(g)
    return t.search(x)
