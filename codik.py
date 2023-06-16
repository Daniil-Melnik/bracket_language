def ending():
    global index, string
    if(string[index] in "+-*/"):
        sign()
        KSZ()
        ending()

def KSZ():
    global index, string
    if(string[index] == '{'):
        index += 1
        SZ()
        FSZ()
        if(not string[index] == '}'):   raise Exception(f"Error KSZ {index} {string[index]}")
        index += 1
    elif(string[index] == '('):
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error KSZ {index} {string[index]}")
        index += 1
    elif(string[index] == '['):
        index += 1
        KVSZ()
        if(not string[index] == ']'):   raise Exception(f"Error KSZ {index} {string[index]}")
        index += 1
    else:   raise Exception(f"Error KSZ {index} {string[index]}")

def DSZ():
    global index, string
    if(string[index] == '+-/*'):
        sign()
        if(not string[index]):  raise Exception(f"Error DSZ {index} {string[index]}")
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error DSZ {index} {string[index]}")
        index += 1
        DSZ()


def KVSZ():
    global index, string
    if(string[index].isalpha()):
        letter()
        sign()
        letter()
        KRSZ()
    elif(string[index] == '('):
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error KVSZ {index} {string[index]}")
        index += 1
        DSZ()
    else:   raise Exception(f"Error KVSZ {index} {string[index]}")

def KRSZ():
    global index, string
    if(string[index] in "+-/*"):
        sign()
        letter()
        KRSZ()

def FSZ():
    global index, string
    if(string[index] in '+-/*'):
        sign()
        KO()
        FSZ()

def KO():
    global index, string
    if(string[index] == '('):
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error KO {index} {string[index]}")
        index += 1
    elif(string[index] == '['):
        index += 1
        KVSZ()
        if(not string[index] == ']'):   raise Exception(f"Error KO {index} {string[index]}")
        index += 1
    else:   raise Exception(f"Error KO {index} {string[index]}")

def SZ():
    global index, string
    if(string[index] == '('):
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error SZ {index} {string[index]}")
        index += 1
        sign()
        SZ()
    elif(string[index] == '['):
        index += 1
        KVSZ()
        if(not string[index] == ']'):   raise Exception(f"Error SZ {index} {string[index]}")
        index += 1
    else:   raise Exception(f"Error SZ {index} {string[index]}")


def PSZ():
    global index, string
    if(string[index] == '{'):
        index += 1
        SZ()
        FSZ()
        if(not string[index] == '}'):   raise Exception(f"Error PSZ {index} {string[index]}")
        index += 1
        ending()
    elif(string[index] == '('):
        index += 1
        letter()
        sign()
        letter()
        KRSZ()
        if(not string[index] == ')'):   raise Exception(f"Error PSZ {index} {string[index]}")
        index += 1
        ending()
    elif(string[index] == '['):
        index += 1
        KVSZ()
        if(not string[index] == ']'):   raise Exception(f"Error PSZ {index} {string[index]}")
        index += 1
        ending()
    elif(string[index].isalpha()): 
        letter()
        KRSZ()
    else:   raise Exception(f"Error PSZ {index} {string[index]}")

def sign():
    global index, string
    if(not string[index] in "+/-*"):    raise Exception(f"Error sign {index} {string[index]}")
    index += 1

def letter():
    global index, string
    if(not string[index].isalpha()):    raise Exception(f"Error letter {index} {string[index]}")
    index += 1




index = 0
string = input("Введите выражение для проверки: ")
try:
    PSZ()
    print("Successful!")
except Exception as e:
    print(e)
