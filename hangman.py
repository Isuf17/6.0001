# Problem Set 2, hangman.py
# Name: Mohammed Isuf Ahmed
# Collaborators: None
# Time spent: 1 hour

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''

    count = 0
    for i in letters_guessed:
        for j in secret_word:
            if i == j:
                count += 1
    if len(secret_word) == count:
        return True
    else:
        return False
    

def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    '''
    i = 0
    s = ''
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            s = s + secret_word[i]
            i += 1
        else:
            s = s + '*'
            i += 1
    return s


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in alphabet:
            alphabet = alphabet.replace(letters_guessed[i], '')
    return alphabet
        
    
def reveal_letter(secret_word, alphabet):
    letters_remaining = []
    for i in secret_word:
        for j in alphabet:
            if i == j:
                letters_remaining.append(i)
    '''
    This creates a list of the characters in secret_word that
    haven't been guessed'
    '''
    choose_from = [] 
    for k in letters_remaining: 
        if k not in choose_from: 
            choose_from.append(k)
    return choose_from
    '''
    This creates a list without duplicates
    '''
    
    
    
    
def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '^'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol ^, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to Hangman!')    
    print('I am thinking of a word that is',len(secret_word),'letters long.')    
    letters_guessed=[]    
    guess=10    
    while not has_player_won(secret_word, letters_guessed) and guess > 0:        
        '''
        This while loop ensures that the game keeps repeating until the
        condition that all the characters in letters_guessed are the 
        same as the letters in secret word is met. There are other conditions
        in this loop that can also break out of the loop.
        '''        
        print('---------------')        
        print('You currently have',guess,'guesses left.')        
        print('Available letters: ' + get_available_letters(letters_guessed))        
        x = input('Please guess a letter: ')        
        x = x.lower()        
        if not x.isalpha() or len(x)!= 1:
            if with_help and x =='^':                
                if guess > 3:                    
                    choose_from = reveal_letter(secret_word, get_available_letters(letters_guessed))                    
                    new = random.randint(0, len(choose_from)-1)                    
                    revealed_letter = choose_from[new]                    
                    guess -= 3                    
                    print('Letter revealed:', revealed_letter)                    
                    letters_guessed.append(revealed_letter)                    
                    print(get_word_progress(secret_word, letters_guessed))  
                    '''
                    This removes 3 guesses if ^ is input to give a hint and then we go back to the top of the loop
                    '''
                    continue                    
                else:                    
                    print('Oops! Not enough guesses left: ',get_word_progress(secret_word, letters_guessed))
                    '''
                    If there are less than 3 guesses, the player is warned and allowed to try again
                    '''
                    continue                
            print('Oops! That is not a valid letter. Please input a letter from the alphabet:',get_word_progress(secret_word, letters_guessed) )                        
            continue            
        if x in letters_guessed:            
            print('Oops! You have already guessed that letter:', get_word_progress(secret_word, letters_guessed) )            
            continue            
        letters_guessed.append(x)
        
        '''
        This adds the letters guessed to a list of letters already guessed, so
        we can check if letters are being guessed more than once.        
        '''           
        if x in secret_word:            
            print('Good guess:', get_word_progress(secret_word, letters_guessed))
            
            '''
            The letter guessed is correct, the current progress is printed and we
            go back to the top of the loop with this new information present.
            '''            
        else:           
            if x in ['a', 'e', 'i', 'o', 'u']:           
                guess -= 2            
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))           
            else:               
                guess -= 1                
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))            
            '''
            The letter guessed is wrong, we lose a guess or two and the loop is repeated.
            '''                       
    if has_player_won(secret_word, letters_guessed):               
        z = len(secret_word)                
        t = []                 
        for l in secret_word:                    
            if l not in t:                         
                t.append(l)                       
            y = guess*len(t)  
            '''
            This calculates the score based on the conditions set in the PSET
            '''
        print('---------------')
        print('Congratulations, you won!')
        print('Your total score for this game:', 2*y+3*z )
    if guess <= 0:
        print('---------------')
        print('Sorry, you ran out of guesses. The correct word was', secret_word + '.')
                    
            
        
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
        secret_word = choose_word(wordlist)
        with_help = False
        hangman('secret_word',with_help)
 
    # After you complete with_help functionality, change with_help to True
    # and try entering "^" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
