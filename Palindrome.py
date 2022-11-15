
''' Is first letter same as last? 
    If so, move in both directions. 
    Reached middle? It's a palindrome! '''


## given list of words, return which are palindromes 

words = ['radar', 'racecar', 'grumble']

def isPalindrome(words):

    for word in words:
        palindrome = True       # default boolean
        start = 0               # position of first letter (first index)
        end = len(word) - 1     # position of last letter (last index)

        while start < end:
            if word[start] != word[end]:    # are the letters at the start & end not equal?
                palindrome = False
                break
            start = start + 1   # move to next letters, closing in on middle
            end = end - 1
        
        if palindrome:          # return words that are palindroms
            return word


## given single word, return if it is a palindrome or not

def isPalindrome(word):

    end = -1                # end is the last index
    flag = 0                

    for i in word:          # iterate thru letters in word
        if i != word[end]:  # does the letter at index i match letter at index end? 
            flag = 1        # if so, 'raise' flag
        end = end -1        # otherwise, move to next letter
    
    if flag == 1:           # was flag raised? not palindrome
        return False 
    else:                   # if not, it is palindrome
        return True 


## OR ##

def isPalindrome(word):

    rev = ''.join(reversed(word))   # reverse word

    if (word == rev):       # do both versions match?
        return True
    return False