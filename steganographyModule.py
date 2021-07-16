from tkinter import filedialog
from tkinter import *
 
contentStartPos = 500

lenStartPos = 100
lenByteLen = 200

extensionStartPos = 300
extensionByteLen = 100

#한글자당 8개
#길이저장은 /8한거 저장.  실제로 64개 비트 보려면 8이라고 저장


def bin2(num):
    bbb = bin(num)
    return str(bbb)[2:].rjust(8,'0')



def desBin(original, convert,startPos, hideLen):
    myBin = ''
    lens = len(original)
    for i in range(startPos,lens):
        #if original[i] == 255:
        #    continue

        if convert[i]!=original[i]:
            myBin+='1'
        else:
            myBin+='0'
        hideLen -= 1
        if(hideLen==0):
            break

    length = 8#이건 고정
    myBytes = ['0b'+myBin[i:i+length] for i in range(0, len(myBin), length)]
    
    return myBytes    


def bytesToStr(myBytes):    
    hArrBytes = bytearray([int(str(x),2) for x in myBytes])

    hStr = hArrBytes.decode('utf-8')
    hStr = hStr[:hStr.find('\x00')]
    return hStr


    

def desFile(originalImageName, newImageName, solveFileName):
   
    original = nameToImg(originalImageName)
    convert = nameToImg(newImageName)
    
    myBin = ''
    lens = len(original)

    
    #####
    hideLen = 64

    hLenBytes = desBin(original,convert,lenStartPos,lenByteLen)
    hLenStr = bytesToStr(hLenBytes)
    print(hLenStr)

    hideLen = int(hLenStr)*8

    extensionBytes = desBin(original,convert,extensionStartPos,extensionByteLen)
    extensionName = bytesToStr(extensionBytes)
    print(extensionName)

    myBytes = desBin(original,convert,contentStartPos,hideLen)


    
    

    #print(myBytes)
    #print(int(myBytes[0],2))

    myBytesArray = bytes([int(x,2) for x in myBytes])
    #print(111)
    #f = open('stegano0322.jpg','wb')

    #extensionName = 'jpg'

    #저장용
    f = open(solveFileName+'.' + extensionName,'wb')    
    f.write(myBytesArray)
    f.close()

    return myBytesArray
        


skipN = 0
'''
def nextOri(data, pos):
    global skipN
    while(True):
        pos += 1
        if data[pos] != 255:
            return pos
'''



def rightRev(bar):
    if bar%2 == 0:
        bar += 1
    else:
        bar -= 1
    return bar


def hideBin(myImg, myHide, startPos):
    originalPos = startPos-1
    for hideInt in myHide:
        hBin = bin2(hideInt)
        #print(hBin)
        for bb in hBin:
            #originalPos = nextOri(myImg,originalPos)
            originalPos += 1
            if bb == '1':
                myImg[originalPos] = rightRev(myImg[originalPos])



def nameToImg(hName):
    if type(hName) is str:
        f = open(hName,'rb')
        myImg = f.read()    # bytes
        f.close()
        return myImg
    else:
        return hName
    
def hideFile(originalImageName, hideFileName, newImageName):

    myImg = nameToImg(originalImageName)
    myHide = nameToImg(hideFileName)


    #print(data)
    imgLen = len(myImg)
    hideLen = len(myHide)

    #myImg[0] = myHide[0]

    #print("E")
    #myImg = int.from_bytes(myImg,'big',signed=False)
    #print(type(myImg))
    myImg = bytearray(myImg)
    #print(type(myImg))

    im = myImg[100]

    extensionName = hideFileName.split('.')[-1]
    if hideFileName.find('.') == -1:
        extensionName = ''
    print(extensionName)
    print(extensionName.encode())

    ####### 

    #myImg[10] = 60

    '''
    print(imgLen)
    print(im)
    bbb = bin(im)
    print(bbb)
    ddd = int(bbb,2)
    print(ddd)
    '''
    
    hideBin(myImg,myHide,contentStartPos)
    hideLen = len(myHide)
    hideLen = str(hideLen)
    #hideLen = '8000010'


    hideBin(myImg,hideLen.encode(),lenStartPos)

    hideBin(myImg,extensionName.encode(),extensionStartPos)
    


    


    #print(type(myImg))
    #print(type(myImg[0]))
    f = open(newImageName,'wb')
    f.write(myImg)
    f.close()



    


