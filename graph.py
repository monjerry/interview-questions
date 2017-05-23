def addWords(looking_word, list_words):
    if looking_word in list_words:
        list_words.remove(looking_word)
    next_words = []
    for word in list_words:
        for i, letter in enumerate(word):
            looking_modified = looking_word[:i] + looking_word[i+1:]
            word_modified = word[:i] + word[i+1:]
            if looking_modified == word_modified:
                list_words.remove(word)
                next_words.append(word)
    return next_words
            

def word_ladder(begin_word, endword, list_words):
    to_visit = addWords(begin_word, list_words)
    dist = 0
    print 'To visit nodes', to_visit 
    while len(to_visit) != 0:
        word = to_visit.pop(0)
        print 'To visit nodes after pop', to_visit 
        print 'Checking word {} against endword {}'.format(word, endword)
        if word == endword:
            return dist
        to_visit = to_visit + addWords(word, list_words)
        print 'To visit nodes', to_visit 
        dist+=1
    return 0
        


print gerry_solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
