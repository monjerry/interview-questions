def addWords(looking_word, list_words):
    if looking_word in list_words:
        list_words.remove(looking_word)
    next_words = []
    for word in list_words:

        for i in range(len(word)):
            looking_modified = list(looking_word)
            looking_modified[i] = '_'
            looking_modified = ''.join(looking_modified)
            word_modified = list(word)            
            word_modified[i] = '_'
            word_modified = ''.join(word_modified)
            if looking_modified == word_modified:
                next_words.append(word)
    for x in next_words:
        list_words.remove(x)
    return next_words
            

def wordLadder(begin_word, endword, list_words):
    
    list_words = sorted(list_words)
    to_visit = addWords(begin_word, list_words)
    dist = 2
    while len(to_visit) != 0:
        next_to_visit = []
        initial_length = len(to_visit)
        for i in range(initial_length):
            word = to_visit.pop(0)
            if word == endword:
                return dist
            next_to_visit = next_to_visit + addWords(word, list_words)
        to_visit += next_to_visit
        dist+=1
    return 0        

print wordLadder('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
