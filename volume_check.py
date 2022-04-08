import os,re,codecs
from this import d

# read file
f = open(os.path.expanduser("friends-script.txt"))
script = f.read()

exceptList = ['All','ALL','Written by','']
characters = []
for line in script.split('\n') :
    name = line.split(':')[0]
    if line.startswith('[') == False and line.startswith('(') == False and name not in exceptList :
        if name not in characters :
            characters.append(name)
    
volume = {}

# get Lines and volume
for character in characters :
    sum = 0
    nameSize = len(character)
    Lines = re.findall(r'%s:.+' % character,script)
    for line in Lines:
        #print(line)
        sum += len(line) - nameSize - 3
    volume[character] = sum
    

for k,v in list(volume.items()) :
    if v==0 :
        del volume[k]

# sort in descending order
rank = sorted(volume.items(),reverse=True,key=lambda item: item[1])

# Rank print 
for i, v in enumerate(rank):
    print("{}. {} [{}]".format(i+1,v[0].capitalize(),v[1]))
