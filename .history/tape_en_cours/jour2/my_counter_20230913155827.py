import pprint

text='fsml fjm slf xmlqj gfmjq mlqks jdnfq ybsd pofza'
counter={}
for letter in text:
    if letter not in counter:
        counter[letter]=0 
    counter[letter]=counter[letter]+1
pprint.pprint(counter)