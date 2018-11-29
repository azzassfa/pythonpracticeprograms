def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

#1) Write code to check a String is palindrome or not? (solution)
def isPalindrome(s):
    isPal="true"                        # initialize flag value

    for i in range(len(s)):             # iterate through the string
        if s[i]!=s[len(s)-i-1]:         # check if first letter is not equals to the last letter and so on
            isPal="false"               # set flag to false

    return isPal                        # return flag

#2) Write a method which will remove any given character from a String? (solution)
def removeLetter(s, letter):
    retValue=""                         # initialize blank return value

    for i in (range(len(s))):           # iterate through the string
        if s[i]!=letter:                # if the current letter is not LetterToRemove
            retValue+=s[i]              # append current letter to return value

    return retValue                     # return value

#3) Print all permutation of String both iterative and Recursive way? (solution)
def stringPermutationsRecursive(p,s):
    if s=="":
        print(p)
    else:
        for i in range(len(s)):
            stringPermutationsRecursive(p + s[i], s[0:i] + s[i + 1: len(s)])

#4) Write a function to find out longest palindrome in a given string? (solution)
def longestPalindrome(s):               # Start function
    retValue=""                         # set return value
    for i in range(len(s)):             # start first loop for whole string length
        for j in range(len(s),i,-1):    # start second loop from end of string to i
            if isPalindrome(s[i:j])=="true":    # check if letter i to j is a palindrome
                if len(s[i:j])>len(retValue):   # if palindrome found and is bigger than retValue then replace retValue
                    retValue=s[i:j]
    if retValue=="":                            # if a palindrome was not found set error message
        retValue="No palindrome in string"
    return retValue                             # return value

def firstNonRepeatCharacter(s):
    retValue=""                                 # set default return value
    found=0                                     # set found flag to ZERO
    for i in range(len(s)):                     # start first loop for whole string length
        for j in range(i+1,len(s)):             # start second loop from i+1 to string length
            if s[i]==s[j]:                      # if s[i] and s[j] match set found flag and exit loop
                found=1
                break
        if found==0:                            # if the iteration was completed without the character being found
            retValue=s[i]                       # set return value and exit for
            break
        else:
            found=0                             # else set found flag to 0 for next iteration
    return retValue                             # return value


print (isPalindrome("maham"))
print (removeLetter("farzhan azhmed","z"))
stringPermutationsRecursive("","abc")
print (longestPalindrome("asaaaa"))
print (firstNonRepeatCharacter("the quick brown fox jumps over the lazy dog"))
