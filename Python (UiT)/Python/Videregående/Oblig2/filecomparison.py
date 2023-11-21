def uniqueWords(inputFile, inputFile2):
    wordCounts = {} 
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close()
    
    for line in inputFile2:
        processLine(line.lower(), wordCounts)
    inputFile2.close()

    pairs = list(wordCounts.items())   

    items = [[count, word] for (word, count) in pairs] 
    items.sort(reverse = True) 
    
    print("Unique words in both files:")
    for count, word in items[ : 10]: 
        print(word, count, sep =  '\t')   
  
def processLine(line, wordCounts): 
    line = replacePunctuation(line) 
    words = line.split() 
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1 
        else:
            wordCounts[word] = 1 

def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line

def mutualWords(inputFile, inputFile2):
    wordCounts = {} 
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close()

    wordCounts2 = {}
    for line in inputFile2:
        processLine(line.lower(), wordCounts2)
    inputFile2.close()
    
    pairs = list(wordCounts.items()) 
    pairs2 = list(wordCounts2.items()) 

    items = [[count, word] for (word, count) in pairs] 

    wordCounts3 = wordCounts & wordCounts2

    for count, word in items[ : 10]: 
        print(word, count, sep =  '\t')   





def main():
    filename = input("Enter a filename: ").strip()
    secondFilename = input("Enter a filename: ").strip()
    inputFile = open(filename, "r") 
    inputFile2 = open(secondFilename, "r") 

    uniqueWords(inputFile, inputFile2)

main()




