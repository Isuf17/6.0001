# Problem Set 4B
# Name: Mohammed Isuf Ahmed
# Collaborators: None
# Time Spent: 3 hours
# Late Days Used: None

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_digit_shift(input_shift, decrypt):
    '''
    calculate the digit shift based on if decrypting or not
    decrypt: boolean, if decrypting or not
    Returns: digit_shift, the digit shift based on if decrypting or not
    '''
    if decrypt:
        digit_shift = 10 - (26-input_shift)%10
    else:
        digit_shift = input_shift
    return digit_shift

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text #Returns the input_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = self.valid_words.copy()
        return valid_words_copy #Returns a copy of the valid_words

    def make_shift_dict(self, input_shift, decrypt=False):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter and number.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift, as well as
        every number to one shifted down by the same amount. If 'a' is
        shifted down by 2, the result is 'c' and '0' shifted down by 2 is '2'.

        The dictionary should contain 62 keys of all the uppercase letters,
        all the lowercase letters, and all numbers mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet and every number (0 <= shift < 26)

        decrypt: if the shift dict will be used for decrypting. affects digit shift function

        Returns: a dictionary mapping letter/number (string) to
                 another letter/number (string).
        '''
        string1 = string.ascii_lowercase #Creates a string of the lowercase alphabet
        string2 = string.ascii_uppercase #Creates a string of the uppercase alphabet
        numbers = '1234567890' #A string of all the numbers
        lower = string.ascii_lowercase[input_shift:] + string.ascii_lowercase[0:input_shift] #A new string of the lowercase alphabet shifted by the input amount
        upper = string.ascii_uppercase[input_shift:] + string.ascii_uppercase[0:input_shift] #A new string of the uppercase alphabet shifted by the input amount
        
        if abs(input_shift) >= 10:
            s = input_shift%10
            x = numbers[s:] + numbers[0:s] #If input_shift is greater or equal to 10, we take the remainder of input_shift/10 to find the shift and use that   
        else:
            x = numbers[input_shift:] + numbers[0:input_shift] #A new string of the numbers shifted by the input amount
        
        numbers_dict = dict()
        i = 0
        while i < len(x):
            numbers_dict[numbers[i]] = x[i] #Creating a dictionary of the unshifted numbers paired with shifted numbers
            i += 1
        
        dict1 = dict()
        i = 0
        while i < len(lower):
            dict1[string1[i]] = lower[i] #Creating a dictionary of the unshifted lowercase letters paired with shifted lowercase letters
            i += 1
            
        dict2 = dict()
        i = 0
        while i < len(upper):
            dict2[string2[i]] = upper[i] #Created a dictionary of the unshifted uppercase letters paired with the shifted uppercase letters
            i += 1
            
        shift_dict = {**dict1, **dict2, **numbers_dict} #Adding all the dictionaries up to form 1 dictionary
        
        return shift_dict
        
    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with the shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down by some number of characters, determined by the shift
        value that shift_dict was built with.

        shift_dict: a dictionary with 62 keys, mapping
            lowercase and uppercase letters and numbers to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter/number shifted using
            the input shift_dict

        '''
        x = '' #An empty string for the encoded message
        i = 0
        while i < len(self.message_text):
            if self.message_text[i] in shift_dict:
                x += shift_dict[self.message_text[i]] #If the character is in the dictionary, add the shifted value to the string
                i += 1
            else:
                x += self.message_text[i] #Adds the objects that aren't letters or numbers to the encoded string
                i += 1
        return x

class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self, input_text) #Uses Messages initialization
        self.shift = input_shift 
        self.encryption_dict = self.make_shift_dict(input_shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: an integer, the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.shift = input_shift #Modify input_shift
        self.encryption_dict = self.make_shift_dict(input_shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict) #Reinitialize the data attributes after modifiying input_shift


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, input_text)

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (26 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt
        the message (a) and the decrypted message text using that shift value
        '''
        list1 = []
        list2= []
        list3 = []
        tuple1 =()
        for l in range(26):
            count = 0
            x = self.apply_shift(self.make_shift_dict(-l)) #Create a dictionary of shift_dict but going back insteaf of forwards
            a = x.split() #Turn x into a list
            b = self.get_valid_words() #Call get_valid_words to use
            for i in a:
                if is_word(b, i):
                    count += 1 #If i in a is in b, return true and add 1 to count so we know how many similar words there are
            list1.append(x) #Add the decoded message to list1
            list2.append(count) #Add the number of similar words to list2
            list3.append(l) #Add the shift value to list3
        c = max(list2) #Find the largest value of similar words
        i = 0
        while i < len(list2):
            if list2[i] != c:
                i += 1 #Iterate through list2 to find which index has the largest value. 
            else:
                tuple1 = tuple([(list3[i])]) + tuple([list1[i]]) #If i is the index with the largest value, add shift and decoded message with the same index to tuple1
                break
        return tuple1
            
        


def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
    # plaintext = PlaintextMessage('hello!', 2)
    # print('Expected Output: jgnnq!')
    # print('Actual Output:', plaintext.get_encrypted_message_text())
    
    '''
    Testing empty string to see if it remains empty
    '''
    plaintext1 = PlaintextMessage('', 5)
    print('Expected Output: ')
    print('Actual Output:', plaintext1.get_encrypted_message_text())
    
    '''
    Testing string and numbers to make sure letters and numbers can get shifted correctly
    '''
    
    plaintext2 = PlaintextMessage('abc 123', 16)
    print('Expected Output: qrs 789')
    print('Actual Output:', plaintext2.get_encrypted_message_text())
 

def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    encrypted = EncryptedMessage('jgnnq!')
#    print('Expected Output:', (2, 'hello!'))
#    print('Actual Output:', encrypted.decrypt_message())
    '''
    Testing all caps and shifted more than 10
    '''
    encrypted1 = EncryptedMessage('AYR')
    print('Expected Output:', (24, 'CAT'))
    print('Actual Output:', encrypted1.decrypt_message())
    '''
    Testing mixture of lowercase and caps, with numbers, shifted less than 1
    '''
    encrypted2 = EncryptedMessage('gPh 123')
    print('Expected Output:', (1, 'fOg 012'))
    print('Actual Output:', encrypted2.decrypt_message())

    

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story = EncryptedMessage(get_story_string())
    return story.decrypt_message()

if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    # test_plaintext_message()
    # test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    # best_shift, story = decode_story()
    # print("Best shift:", best_shift)
    # print("Decoded story: ", story)
    pass