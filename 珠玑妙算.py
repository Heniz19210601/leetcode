//ÖéçáÃîËã
solution = 'RGBY'
guess = 'GGRR'
exist = 0
correct = 0
g = []
for i in range(len(guess)):        
    if guess[i] == solution[i]:
        correct = correct + 1
        g = guess.strip(guess[i])
for i in range(len(g)):
    if g[i] in solution:
        exist = exist + 1
exist = exist - correct
print(correct,exist)