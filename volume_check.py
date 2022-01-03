import os,re,codecs

# read file
os.chdir(r'C:\Users\cky0935')
f = codecs.open('friends116.txt','r',encoding = 'utf-8')
script = f.read()

# split characters name
characters = list(map(str,input().split(' ')))
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
    
# sort in descending order
rank = sorted(volume.items(),reverse=True,key=lambda item: item[1])

# Rank print 
for i, v in enumerate(rank):
    print("{}. {}[{}]".format(i+1,v[0],v[1]))
