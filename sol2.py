#pip install requests
import requests

class xdata:
    def __init__(self, index, data):
        self.data = data
        self.index = index

url = 'https://cm2023.obss.io/3d1099a4-98f0-4078-9648-78ab59e1223f?lang=EN'
r = requests.get(url)
content = r.text

linkPos = 0
linkStartIndex = 0
links = []
while linkPos != -1:
    linkPos = content[linkStartIndex:].find("https://cm2023.obss.io/")
    print(linkStartIndex + linkPos)

    link = content[linkStartIndex + linkPos : linkStartIndex + linkPos + min(content[linkStartIndex + linkPos:].find("\""), content[linkStartIndex + linkPos:].find("\'"))]
    links.append(link)
    linkStartIndex += linkPos + 1

nextPos = 0
startIndex = 0
dataText = [0 for i in range(186)]
print(content[4388:4446])
while nextPos != -1:
    nextPos = content[startIndex:].find("x-data-index")
    
    startBracketPos = startIndex + nextPos
    endBracketpos = startIndex + nextPos
    if nextPos != -1:
        decrement = 1
        increment = 1
        while content[startIndex + nextPos - decrement] != '<':
            decrement+=1
        while content[startIndex + nextPos + increment] != '>':
            increment+=1
        startBracketPos = startIndex + nextPos - decrement
        endBracketpos = startIndex + nextPos + increment
        
        index = content[startIndex + nextPos + 14 : startIndex + nextPos + 14 + content[startIndex + nextPos + 14:].find("\"")]
        print("index is: " + index) 

        dataPos = content[startBracketPos:endBracketpos].find("x-data-value")
        if dataPos != -1:
            data = content[startBracketPos + dataPos + 14 : startBracketPos + dataPos + 14 + content[startBracketPos + dataPos + 14:].find("\"")]
            print("data is: " + data) 
            dataText[int(index)] = data
    
    print(startBracketPos)
    print(endBracketpos)
    startIndex = endBracketpos + 1

for text in dataText:
    print(text, sep="", end="")