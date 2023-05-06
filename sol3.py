import base64
import requests
from Crypto.Cipher import AES
import re

url = input("Please enter the url for the file: ").strip()
AESkey = bytes(input("Please enter the key for decryption: ").strip(), encoding='utf-8')
IV = bytes([0] * 16)
request = requests.get(url) 

encoded_string = request.text
decoded_string = base64.b64decode(bytes(encoded_string, encoding='utf-8'))# + b'==')

cipher = AES.new(AESkey, AES.MODE_CBC, IV)
decryptedText = str(cipher.decrypt(bytes(decoded_string)))


pages = []

startPos = 0
breakPos = 0

while breakPos != -1:
    breakPos = decryptedText[startPos:].find("~@~")
    breakPosAdded = breakPos + startPos

    if breakPos != -1:
        pages.append(str(decryptedText[startPos: breakPosAdded]))
    else:
        pages.append(str(decryptedText[startPos:]))
    
    startPos = breakPosAdded + 3

file = {i : [] for i in range(len(pages))}

for index, page in enumerate(pages):
    page = str(page)
    lines = []
    startPos = 0
    breakPos = 0
    
    while breakPos != -1:
        breakPos = page[startPos:].find("\\n")
        breakPosAdded = breakPos + startPos

        if breakPos != -1:
            lineToCheck = str(page[startPos: breakPosAdded].strip())
            if lineToCheck != "":
                lines.append(lineToCheck)
        else:
            lineToCheck = str(page[startPos:].strip())
            if lineToCheck != "":
                lines.append(lineToCheck)
        
        startPos = breakPosAdded + 2
    
    file[index] = lines

results = []
for page, lines in file.items():
    for line in lines:
        line = str(line)
        regex = "^F[a-zA-Z]*I[0-9]+N[^a-zA-Z0-9]{0,5}D[\\t\\s]+[0-9]x[0-9]$"
        pattern = re.search(regex, line)

        if pattern is not None:
            pattern = pattern.group(0)
            indexOfX = str(pattern).find("x")
            lineNum = int(str(pattern)[indexOfX+1:])
            
            pageNum = re.search("\s[0-9]+", str(pattern)[:indexOfX])
            pageNum = int(pageNum.group(0)[1:])
            res = file[pageNum - 1][lineNum - 1]

            for char in res:
                if char.isalpha():
                    res = res.replace(char, "")
            results.append(res)

for res in results:
    print(res, end="")
        
        
