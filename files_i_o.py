import os
def openfile():
    return(0)
def readfile():
    return(0)
def appendfile():
    return(0)
def writefile():
    return(0)
def createfile():
    return(0)
def textmode():
    return(0)
def binarymode():
    return(0)
def readfile2():
    return(0)
def readline():
    return(0)
def deletefile():
    return(0)

openfile(open("email.txt"))
readfile(open("email.txt", "r"))
appendfile(open("email.txt", "a"))
writefile(open("email.txt", "w"))
createfile(open("email.txt", "x"))
textmode(open("email.txt", "t"))
binarymode(open("email.txt", "b"))
print(readfile2(open("email.txt".read())))
print(readline(open("email.txt".readline())))
deletefile(os.remove("email.txt"))
