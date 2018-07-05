import json
from itertools import chain

# Script to create Q-Value JSON file, initilazing with zeros

qval = {}
# X -> [-40,-30...120] U [140, 210 ... 490]
# Y -> [-300, -290 ... 160] U [180, 240 ... 420]
for x in chain(list(range(-40,180,5)), list(range(180,421,70))):
    for y in chain(list(range(-300,180,5)), list(range(180,421,60))):
        for x1 in chain(list(range(-40+150,180+150,15)),list(range(180+150,420+150,80))):
            for y1 in chain(list(range(-300,180,10)), list(range(180,421,60))):
                qval[str(x)+'_'+str(y)+'_'+str(x1)+"_"+ str(y1)] = [0,0]


fd = open('grid5.json', 'w')
json.dump(qval, fd)
fd.close()

