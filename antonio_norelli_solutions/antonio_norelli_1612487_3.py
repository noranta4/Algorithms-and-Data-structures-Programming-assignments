__author__ = 'Antonio Norelli'

#I build a dictionary with the sorted strings (EX. hte -> eht) as keys
#every key is associated to a list with all the anagrams in the input_string of the key
#I scan the dictonary and I append every item of every list to the result

#COST n = number of strings, m = average lenght of a string
#build the dictionary: O(n*m*log(m)) (sort letters of every string in alphabetical order)
#value of a key is computable in O(1) because dict is implemented in python as hash table
#assemble the result: O(n*log(n)) if alphabetical order is necessary (sort dict O(n*log(n)), scan dict O(n))
#                     O(n) if alphabetical order is not necessary
#total = O(n*m*log(m)) if alphabetical order is not necessary
#        O(MAX(n*m*log(m), n*log(n))) if alphabetical order is necessary

#................................................................................................................

#SAMPLE INPUT

input_strings = ['ab', 'ciao', 'the', 'iaoc', 'caio', 'ot', 'hte', 'ba', 'ab', 'go']

#PROGRAM

def sort_by_anagrams(list_of_strings):
    dict_of_anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in dict_of_anagrams:
            dict_of_anagrams[sorted_string].append(string)
        else:
            dict_of_anagrams[sorted_string] = [string]
    result = []
    for anagram in sorted(dict_of_anagrams): #if alphabetical order is not necessary delete this and next sorted call
        for string in sorted(dict_of_anagrams[anagram]):
            result.append(string)
    return result

print sort_by_anagrams(input_strings)









