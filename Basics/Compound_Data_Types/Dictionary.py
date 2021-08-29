"""
Dictionary  - another type of compound data type.
Dictionaries are mutable like lists

 Python dictionary stores pair of data
 1. Key
 2. Value

 indexing is quite similar to lists
 but in dictionary, indexing are made with keys (keys can be int and str ; unlike lists which uses only int )
        and the value associated with that key is returned
"""

myDict = {}         # Empty dictionary
grades = {'Ana': 'B', 'John':'A+', 'Denise':"A", "katy": 'A'}
print(len(grades))

print(grades['Ana'])            # returns 'B' which is the value associated with the key, 'Ana'
print(grades["Denise"])
print('\n')


#                       Dictionary Operations / functions
# adding an entry
grades["Slyvan"] = "B"
print(grades)


# test if a key is in dictionary
print("Daniel" in grades)           # returns False
print("John" in grades)            # returns True if "john" is found in the dict

# delete an entry
print(grades)
del(grades["Denise"])
print(grades)

print('\n')


#                           More on dictionary
"""
    Keys:
        - must be unique
        - immutable
    Values:
        - can be any type(mutable and immutable)
        - can be duplicates
        - dict values can be lists and even other dictionaries
"""
d = {4:{1:0}, (1,3):"twelve", 'const':[3.14, 2.7, 8.44]}
print(d[(1,3)])


#                       More functions
"""
    .keys() used on dictionaries returns an iterable that acts like a tuple of all keys 
    .values() used on dictionaries returns an iterable that acts like a tuple of all values 

NB:  No order is guaranteed
"""
keys = grades.keys()
print(keys)
print(type(keys))               #    returns 'dict_keys'

Vals = grades.values()
print(Vals)

print('\n')



#                           Applications of dictionaries
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]                                   #  A song lyric

def lyrics_to_freq(lyrics):
    """
    takes in a list of words
    returns a dictionary with the words and the number of times they occur
            {str:int}
    """
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1               # Updating dictionary
        else:
            my_dict[word] = 1                 # A dict can be mutated
    return my_dict


beatles = lyrics_to_freq(she_loves_you)
# print(beatles)


def most_common_words(freqs):
    """
    input: freqs - a dictionary {str:int, str:int, str:int, str:int, str:int,}
    :returns : a tuple of a list and the highest freq
    """
    values = freqs.values()
    best = max(values)           # largest number/value
    words = []                      # empty list
    for k in freqs:                     # can iterate over keys in a dictionary
        if freqs[k] == best:
            words.append(k)
    return (words, best)


# print(most_common_words(beatles))



def words_often(freqs, MinTime):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= MinTime:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

# print(words_often(beatles, 6))

# Accessing values in a dictionary using indexes or dictionary method, get()

"""
    When we retrieve a value from a dictionary using the key as in dict[fruit] and the key isn't present, 
    we get an error. If we use a get() method instead, we can specify what value should be returned if the key isn't present. 
    In other words, the getMethod allows us to specify a default value when the key that we're looking for isn't in 
    the dictionary. 
"""

foods = {"vegetable":"cabbage", "fruit":"orange", "liquid":"water"}
# print(foods["solid"])   # error
print(foods.get("solid", " "))

# So what we're asking Python to do is try to retrieve the value associated with the key, but if the
# key's not defined return an empty string instead.