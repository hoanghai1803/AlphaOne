import json
from itertools import chain

# Script to create Q-Value JSON file, initilazing with zeros

qval = {}
# X -> [-120,-110...130] U [140, 210 ... 420]
# Y -> [-300, -290 ... 170] U [180, 240 ... 420]
# X1 -> [-60, -50,..., 260] U [280, 350, ..., 560]
# Y1 -> [-300, -280..., 160] U [180, 240,...,420]
for x in chain(list(range(-120,140,10)), list(range(140,421,70))):
    for y in chain(list(range(-300,180,10)), list(range(180,421,60))):
        for x1 in chain(list(range(-60,280,20)),list(range(280,561,70))):
            for y1 in chain(list(range(-300,180,20)), list(range(180,421,60))):
                qval[str(x)+'_'+str(y)+'_'+str(x1)+"_"+ str(y1)] = [0,0]
fd = open('grid5.json', 'w')
json.dump(qval, fd)
fd.close()

