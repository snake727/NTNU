def isAnagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The inputs are anagrams!")
    else:
        print("The inputs are not anagrams!")


isAnagram(input(str("Input first word: ")), input(str("Input second word: ")))