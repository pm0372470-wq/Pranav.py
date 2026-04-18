word1 = "Engineering"
word2 = "Computing"

vowels = "AEIOUaeiou"

result1 = ""
for ch in word1:
    if ch not in vowels:
        result1 += ch

result2 = ""
for ch in word2:
    if ch not in vowels:
        result2 += ch

print("Engineering →", result1)
print("Computing →", result2)