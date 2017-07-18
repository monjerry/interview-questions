# Given an array of words, return a list of lists, each inner list is a list of anagrams
def anagrams(words):
    dictionary = {}
    for word in words:
        key = tuple(sorted(word))
        if key in dictionary:
            dictionary[key].append(word)
        else:
            dictionary[key] = [word]
    return sorted(dictionary.values())


print anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
