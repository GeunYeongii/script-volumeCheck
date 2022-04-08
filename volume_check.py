import os,re,codecs
from this import d
import requests
from bs4 import BeautifulSoup

# write file
season = input("회차를 입력하세요 >> ")
url = f'https://fangj.github.io/friends/season/{season}.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

p = soup.find_all('p')

f = open(os.path.expanduser("friends-script.txt"),"w")
sum = 0
for i in p :
    if i.text.startswith('End') == 0 and i.text.startswith('[') == 0 and i.text.startswith('(') == 0 and i.text.startswith('Originally written by')==False:
        f.write(i.text.replace('\n',' '))
        f.write("\n")
        sum += len(i.text)
f.close()

if sum < 100 :
    br = soup.find_all(text=True)

    f = open(os.path.expanduser("friends-script.txt"),"w")
    sum = 0
    for i in br :
        if i.text.startswith('End') == 0 and i.text.startswith('[') == 0 and i.text.startswith('(') == 0 and i.text.startswith('Originally written by')==False:
            f.write(i.text.replace('\n',' '))
            f.write("\n")
            sum += len(i.text)
    f.close()
    


    


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
