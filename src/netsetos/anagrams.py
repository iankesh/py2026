def anagram():
    word1 = "fried"
    word2 = "fired"

    if sorted(word1) == sorted(word2):
        print("anagram")

anagram()

def anagram_index():
    arr = ["cat", "dog", "tac", "god", "act"]
    anagram_dict = {}
    for i in range(len(arr)):
        print(sorted(arr[i]))



anagram_index()

