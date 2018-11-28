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
            retValue+=s[i]            # append current letter to return value

    return retValue                     # return value

print (isPalindrome("maham"))
print (removeLetter("farzhan azhmed","z"))

