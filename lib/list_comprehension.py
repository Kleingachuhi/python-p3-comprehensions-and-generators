#!/usr/bin/env python3
def return_evens(num_list):
    evens = []
    for n in num_list:
        if n % 2 == 0:
            evens.append(n)
    return evens

    pass

return_evens(range(10))
def make_exclamation(sentence_list):
    result = []  
    for sentence in sentence_list: 
        result.append(sentence + "!") 
    return result  

make_exclamation(["I like computers", "I require coffee", "Live long and prosper"])
