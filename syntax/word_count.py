# Implement a function which scans a string and returns a list of all unique
# words in the string and their number of occurrences, sorted by the number
# of occurrences in a descending order and order of appearanche in the
# document.
# The function is case insensitive and must strip out all characters which
# are not part of the English alphabet

# Example:
# input: document = "Word is the same as word, wORd but isn't the same as w0rd"
# output: [['word', 3], ['the', 2], ['same', 2], ['as', 2], ['this', 1],
#         ['is', 1], ['but', 1], ['isnt', 1], ['wrd', 1]]


# For this exercise, no Python external libraries should be used.
import re

def get_word_count(document):
    cWords = {}
    words = []
    
    for w in document.lower().split():
        # remove all non-words chars
        w = re.sub("[^a-z]", "", w)
        
        # Count unique words
        if w in cWords:
            cWords[w] += 1
        else:
            cWords[w] = 1
    
    # reformat the dict into a double array
    #for k,v in sorted(cWords.items(), key=lambda x: x[1], reverse=True):
    for k,v in sorted(cWords.items(), key=lambda x: x[1], reverse=True):
        words.append([k, v])
            
    print(words)
    
    return(words)


# The function must pass this test:
document = "This Word is the same as word, wORd but isn't the same as w0rd"

assert get_word_count(document) == [['word', 3], ['same', 2], ['as', 2], 
                                    ['the', 2], ['wrd', 1], ['this', 1], 
                                    ['is', 1], ['isnt', 1], ['but', 1]] 