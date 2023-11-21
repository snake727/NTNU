import re

inputGenes = input("Input a sequence you wish to analyze: ")
pattern = re.compile(r'ATG((?:[ACTG]{3})+?)(?:TAG|TAA|TGA)')
results = pattern.findall(inputGenes)

print(results)