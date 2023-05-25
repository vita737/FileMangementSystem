# Inserts character, Replace
orignal = "abdef"
new = "abcef"
chip = ''
i = -1
for x, y in zip(orignal, new):
    i+=1
    if x != y:
        if orignal[i] == new[i+1]: # Single insert
            chip = chip+'i'+str(i)+y
            new = new[:i] + y+ new[i:] # shift changes
        else:
            chip = chip+'r'+str(i)+y # Single replace
print(chip)