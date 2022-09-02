In this problem
Like your suggestion i use Trie to handle this problem
Each character have list children to reduce memory use

I think i will explain some function:

class Trie:
insert()
-> This function , i use dictionary to save character and it's child element

class TrieNode:
i have 2 variable : is_word and children
is word : check this location -> what end character can make word or not
children : dictionary to save next character in a word

suffiexs()
-> I iterate dictionary :
-> if element is word : append
but i have special case : when u save fun and function
-> fun : n have propery is_word: true
-> function: n is the same -> so we can't get it
-> i fix it to and more case:
i check if len of sub children is not empty
-> continue append suffiexs
-> else:
continue call recursive append another element (what have is_word is true)

Time Complexity algorithmn: O(log(n))
Space Complexity : O(1)

Base(Trie & dictonary)
