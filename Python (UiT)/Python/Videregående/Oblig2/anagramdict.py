def check_anagram(a, b):
    if a is None or b is None or len(a) != len(b):
        return "Words are not anagrams!"
        
    counts_a = {}
    counts_b = {}
    
    for x in a:
        if x not in counts_a.keys():
            counts_a[x] = 1
        else:
            counts_a[x] += 1
        
    for x in b:
        if x not in counts_b.keys():
            counts_b[x] = 1
        else:
            counts_b[x] += 1
        
    return "Words are anagrams!" if counts_a == counts_b else "Words are not anagrams!"

print(check_anagram(input(str("Input first word: ")), input(str("Input second word: "))))