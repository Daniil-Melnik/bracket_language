str = "{[(a+b)]-[a+b]+(a+m)}/[(a+m-d+t)]"

print("input: "+str+'\n')

dict={
    "{" : "A",
    "}" : "B",
    "[" : "C",
    "]" : "D",
    "(" : "E",
    ")" : "F"
}

ch = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

bracket_1 = ['{','[','(']
bracket_2 = ['}',']',')']

arr_A=[]
arr_B=[]
arr_C=[]
arr_D=[]
arr_E=[]
arr_F=[]

arr_sign = ['-', '*', '/', '+']

k=0
str_1=[]

#print(str_1)

for i in str:
    str_1.append('*')

#print(str_1)

for i in range(0, len(str)):
    if (str[i] in ['{','}','[',']','(',')']):
        str_1[i] = dict[str[i]]
        
cond_1 = True # все скобки на месте
cond_2 = True # внутри круглых норма
cond_3 = True # внутри квадратных норма
cond_4 = True # внутри фигурных норма
cond_5 = True # нет однобуквенных в круглых
cond_6 = True # проблема с расстановкой букв и знаков
        
for i in range(0, len(str_1)):
    if str_1[i]=='A':
        arr_A.append(i)
    elif str_1[i]=="B":
        arr_B.append(i)
    elif str_1[i]=="C":
        arr_C.append(i)
    elif str_1[i]=="D":
        arr_D.append(i)
    elif str_1[i]=="E":
        arr_E.append(i)
    elif str_1[i]=="F":
        arr_F.append(i)
    
print(str_1)

if (len(arr_A)!=len(arr_B))or(len(arr_C)!=len(arr_D))or(len(arr_E)!=len(arr_F)):
    print("Error, it is not a correct bracket sequence")
    cond_1 = False
i=0
for i in range(0, len(str)):
    if (str[i] in arr_sign):
        if (((str[i-1]in ch)or(str[i-1]in['{','}','[',']','(',')']))and((str[i+1]in ch)or(str[i+1]in['{','}','[',']','(',')']))):
            i=+7
        else:
            cond_6=False
            print("проблема со знаками", i)

for i in range(0, len(arr_E)):
    for j in range (arr_E[i]+1, arr_F[i]):
        if (str_1[j]=='E' and str_1[j-1]!='E')or(str_1[j]=='A')or(str_1[j]=='B')or(str_1[j]=='C')or(str_1[j]=='D'):
            cond_2 = False
            print("внутри круглых скобок есть скобочные записи или круглые нелишние")
            print(j)
if (cond_1 and cond_2 and cond_6):
    for i in range(0, len(arr_E)):
        if (arr_F[i]-arr_E[i]==2):
            cond_5 = False
            print("есть однобуквенные записи внутри круглых скобок")
if (cond_1 and cond_2 and cond_5 and cond_6):
    for i in range(0, len(arr_C)):
        for j in range(arr_C[i]+1, arr_D[i]):
            if (str_1[j]=='C' and str_1[j-1]!='C')or(str_1[j]=='A'):
                cond_3=False
                print("внутри квадратных скобок есть фигурные или квадратные нелишние")

if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6):
    for i in range (0, len(arr_A)):
        for j in range(arr_A[i]+1, arr_B[i]):
            if (str_1[j]=='A' and str_1[j-1]!='A'):
                cond_4=False
                print("внутри фигурных скобок есть фигурные нелишние")

                
if (cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6):
    print("the bracket entry corresponds to the given grammar")

