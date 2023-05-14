def letter(i, str):
    ch = str[i+1]
    i=i+1
    if ch in "abcdefghijklmnopqrstuvwxyz" :
        ch = str[i+1]
        i=i+1
        return ch, i
    else:
        print("Error")
        
def sign(i, str):
    ch = str[i+1]
    i=i+1
    if ch in "-+/*" :
        ch = str[i+1]
        i=i+1
        return ch, i
    else:
        print("Error")
        
def BZ(i, str):
    ch = str[i+1]
    if ch in "abcdefghijklmnopqrstuvwxyz":
        ch, i = letter(i, str)
        ch, i = sign(i, str)
        ch, i = letter(i, str)
    elif ch in "+-*/":
        ch, i = sign(i, str)
        ch, i = BZ(i, str)
    else:
        print("Error")
    return ch, i

def SZKV(i, str):
    ch=str[i+1]
    if ch == '[':
        ch, i = SZKV(i, str)
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        ch, i = BZ(i, str)
    elif ch in "+-*/":
        ch, i = sign(i, str)
    elif ch =='(':
        ch, i = SZKR(i, str)
    elif ch == "]":
        ch = str[i+1]
    else:
        print("Error")
    return ch, i+1

def SZKR(i, str):
    ch=str[i+1]
    if ch == "(":
        ch, i = SZKR(i, str)
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        ch, i = BZ(i, str)
    elif ch == ")":
        ch = str[i+1]
    else:
        print("Error")
    return ch, i+1

def SZF(i, str):
    ch = str[i+1]
    if ch == "{":
        ch, i = SZF(i, str)
    elif ch == "[":
        ch, i = SZKV(i, str)
    elif ch in "+-*/":
        ch, i = sign(i, str)
    elif ch == "(":
        ch, i = SZKR(i, str)    
    elif ch == "}":
        ch = str[i+1]
    else:
        print("Error")
    return ch, i+1

def PSZ(i, str):
    ch = str[i+1]
    if ch == "(":
        ch, i = SZKR(i, str)
    elif ch == "[":
        ch, i = SZKV(i, str)
    elif ch == "{":
        ch, i = SZF(i, str)
    elif ch in "+-*/":
        ch, i = sign(i, str)
        ch, i = PSZ(i, str)
    else:
        print("Error")
    return ch, i+1

str = input("Введите значение")
i=0
ch, i = PSZ(i, str)