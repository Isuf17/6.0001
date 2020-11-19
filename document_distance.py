# Problem Set 3
# Name: Mohammed Isuf Ahmed
# Collaborators: Juan Rached Viso
# Time Spent: 3 hours
# Late Days Used: (only if you are using any)

import string

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other


### Problem 1: Prep Data ###
# Make a *small* change to separate the data by whitespace rather than just tabs
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        list of strings holding the file contents where
            each string was separated by a newline character (\t) in the file
    """
    inFile = open(filename, 'r')
    line = inFile.read()
    inFile.close()
    line = line.strip().lower()
    for char in string.punctuation:
        line = line.replace(char, "")
    return line.split()

### Problem 2: Find Ngrams ###
def find_ngrams(single_words, n):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
        n:            length of 'n-gram' window
    Returns:
        list of n-grams from input text list, or an empty list if n is not a valid value
    """
    list_values = ' '
    list = []
    if n <= 0 or n > len(single_words):
        return []
    '''
    This ensures that if n is invalid, an empty list is returned.
    '''
    for i in range(len(single_words) -n + 1):
        '''
        This bound on i ensures we don't index too far into single_words
        '''
        list_values = single_words[i:i+n]
        list_values = ' '.join(list_values)
        '''
        The join function removes punctuation and replaces with something of my choice
        In this case I want to remove all the commas that separate different elements
        in a list. We then add this string with no commas to the list to create our n-gram.
        '''
        list.append(list_values)
    return list


### Problem 3: Word Frequency ###
def compute_frequencies(words):
    """
    Args:
        words: list of words (or n-grams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word (or n-gram) in words and the corresponding int
        is the frequency of the word (or n-gram) in words
    """
    frequency = {}
    
    for i in words:
        count = 0
        for j in words:
            if i == j:
                count += 1
                '''
                This counts the number of times a word
                shows up, and then adds that number up
                and associates it with that word in the 
                frequency dictionary
                '''
            frequency[i] = count
    return frequency

### Problem 4: Similarity ###
def get_similarity_score(dict1, dict2, dissimilarity = False):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words or n-grams for one text
        dict2: frequency dictionary of words or n-grams for another text
        dissimilarity: Boolean, optional parameter. Default to False.
          If this is True, return the dissimilarity score, 100*(DIFF/ALL), instead.
    Returns:
        int, a percentage between 0 and 100, inclusive
        representing how similar the texts are to each other

        The difference in text frequencies = DIFF sums words
        from these three scenarios:
        * If a word or n-gram occurs in dict1 and dict2 then
          get the difference in frequencies
        * If a word or n-gram occurs only in dict1 then take the
          frequency from dict1
        * If a word or n-gram occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 100*(1-(DIFF/ALL)) rounded to the nearest whole number if dissimilarity
          is False, otherwise returns 100*(DIFF/ALL)
    """
    DIFF = 0
    x = dict1.copy()
    y = dict2.copy()
    '''
    Make copies of the dictionary that we can modify and use later
    '''
    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                del x[key1]
                del y[key2]
                '''
                Remove the similar keys from each dictionary in the copies
                and then add the difference in frequency to DIFF
                '''
                DIFF += abs(dict1[key1] - dict2[key2])
    DIFF += sum(x.values())    
    DIFF += sum(y.values())
    ALL = sum(list(dict1.values())) + sum(list(dict2.values()))
    '''
    Adds the frequency of non similar words from both dictionaries
    to ALL
    '''
    if not dissimilarity:
        return round(100*(1-(DIFF/ALL)))
        '''
        Returns the equation desired depending on
        dissimilarity
        '''
    else:
        return 100*(DIFF/ALL)


### Problem 5: Most Frequent Word(s) ###
def compute_most_frequent(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    fre_dict = {}
    x = dict1.copy()
    y = dict2.copy()
    '''
    Create copies of the dictionaries that can be modified
    '''
    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                del x[key1]
                del y[key2]
                fre_dict[key1] = dict1[key1] + dict2[key2]
                '''
                We delete keys that appear both in dict1 and dict2
                from x and y and we add these keys and value sums to fre_dict
                '''
    for key in x:
        fre_dict[key] = x[key]
    for key in y:
        fre_dict[key] = y[key]
    '''
    Will add the non similar keys between x and y into fre_dict 
    with their values
    '''
    list1 = []
    x = max(fre_dict.values())
    '''
    x is the key with the largest value
    '''
    for key in fre_dict:
        if fre_dict[key] == x:
            list1.append(key)
            '''
            Adds any keys with the same value to x
            to list1
            '''
    return list1
    
### Problem 6: Finding closest artist ###
def find_closest_artist(artist_to_songfiles, mystery_lyrics, ngrams = 1):
    """
    Args:
        artist_to_songfiles:
            dictionary that maps string:list of strings
            where each string key is an artist name
            and the corresponding list is a list of filenames (including the extension),
            each holding lyrics to a song by that artist
        mystery_lyrics: list of single word strings
            Can be more than one or two words (can also be an empty list)
            assume each string is made of lowercase characters
        ngrams: int, optional parameter. Default set to False.
            If it is greater than 1, n-grams of text in files
            and n-grams of mystery_lyrics should be used in analysis, with n
            set to the value of the parameter ngrams
    Returns:
        list of artists (in alphabetical order) that best match the mystery lyrics
        (i.e. list of artists that share the highest average similarity score (to the nearest whole number))

    The best match is defined as the artist(s) whose songs have the highest average
    similarity score (after rounding) with the mystery lyrics
    If there is only one such artist, then this function should return a singleton list
    containing only that artist.
    However, if all artists have an average similarity score of zero with respect to the
    mystery_lyrics, then this function should return an empty list. When no artists
    are included in the artist_to_songfiles, this function returns an empty list.
    """
    if artist_to_songfiles == {}:
        return []
    '''
    This returns an empty list if artist_to_songfiles 
    is empty
    '''
    
    '''
    The following method is for ngrams, which only slighly differs from using words
    It is only used if ngrams != 0
    The code for use ngrams and words is nearly exact apart from
    using ngrams of mystery_lyrics and ngrams of songs' lyrics instead of just a list
    of the words
    I will just explain the code them for non ngrams
    '''
    if ngrams != 1:
            dict1 = {}
            a = compute_frequencies(find_ngrams(mystery_lyrics, ngrams))
            for key in artist_to_songfiles:
                count = 0
                dict1[key] = 0
                for file in artist_to_songfiles[key]:
                    words = compute_frequencies(find_ngrams(load_file(file), ngrams))
                    similarity = get_similarity_score(words, a)
                    dict1[key] += similarity
                    count += 1
                dict1[key] = round(dict1[key]/count)
            list1 = list(dict1.keys())
            list2 = list(dict1.values())
            list3 = []
            b = max(list2)
            if b == 0:
                return []
            for i in range(len(list1)):
                if list2[i] == b:
                    list3.append(list1[i])
            return list3
    
    dict1 = {}
    a = compute_frequencies(mystery_lyrics)
    '''
    Set a equal to the frequencies of the words in mystery_lyrics
    '''
    for key in artist_to_songfiles:
        count = 0
        dict1[key] = 0
        '''
        The count and score associated with a new artist needs to be set 
        to 0 after every artist.
        '''
        for file in artist_to_songfiles[key]:
            '''
            For each list of song lyrics associated with each artist, we find
            the frequency of the words in one song, find its similarity with mystery lyrics
            and then add that score to the score already in associated with that arist in dict1
            We then add 1 to count for every song
            '''
            words = compute_frequencies(load_file(file))
            similarity = get_similarity_score(words, a)
            dict1[key] += similarity
            count += 1
        dict1[key] = round(dict1[key]/count)
        '''
        This division finds the average similarity across a number of songs from an artist
        '''
    list1 = list(dict1.keys())
    list2 = list(dict1.values())
    list3 = []
    b = max(list2)
    if b == 0:
        return []
        '''
        If there's no similarity between the mystery_lyrics and artists lyrics
        we return an empty list
        '''
    for i in range(len(list1)):
        if list2[i] == b:
            list3.append(list1[i])
            '''
            This creates a list of all the artists with highest score if they've drawn,
            or a list with just one artist that had the highest score
            '''
    return list3
    

    

if __name__ == "__main__":
    
    #Uncomment the following lines to test your implementation
    # Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # world, friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # print(world) ## should print ['hello', 'world', 'hello']
    # print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Find Ngrams
    # world_ngrams, friend_ngrams = find_ngrams(world, 2), find_ngrams(friend, 2)
    # longer_ngrams = find_ngrams(world+world, 3)
    # print(world_ngrams) ## should print ['hello world', 'world hello']
    # print(friend_ngrams) ## should print ['hello friends']
    # print(longer_ngrams) ## should print ['hello world hello', 'world hello hello', 'hello hello world', 'hello world hello']

    ## Tests Problem 2: Get frequency
    # world_word_freq, world_ngram_freq = compute_frequencies(world), compute_frequencies(world_ngrams)
    # friend_word_freq, friend_ngram_freq = compute_frequencies(friend), compute_frequencies(friend_ngrams)
    # print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    # print(world_ngram_freq) ## should print {'hello world': 1, 'world hello': 1}
    # print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    # print(friend_ngram_freq) ## should print {'hello friends': 1}

    ## Tests Problem 3: Similarity
    # word_similarity = get_similarity_score(world_word_freq, friend_word_freq)
    # ngram_similarity = get_similarity_score(world_ngram_freq, friend_ngram_freq)
    # print(word_similarity) ## should print 40
    # print(ngram_similarity) ## should print 0

    ## Tests Problem 4: Most Frequent Word(s)
    # freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    # most_frequent = compute_most_frequent(freq1, freq2)
    # print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find closest matching artist
    # test_directory = "tests/student_tests/"
    # artist_to_songfiles_map = {
    # "artist_1": [test_directory + "artist_1/song_1.txt", test_directory + "artist_1/song_2.txt", test_directory + "artist_1/song_3.txt"],
    # "artist_2": [test_directory + "artist_2/song_1.txt", test_directory + "artist_2/song_2.txt", test_directory + "artist_2/song_3.txt"],
    # }
    # mystery_lyrics = load_file(test_directory + "mystery_lyrics/mystery_1.txt") # change which number mystery lyrics (1-5)
    # print(find_closest_artist(artist_to_songfiles_map, mystery_lyrics)) # should print ['artist_1']
    pass