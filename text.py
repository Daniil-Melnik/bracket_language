#str = "{(a+b-c)(a-c)}+(a+b)-[(k+t)(a+b)]"


#print("input: "+str+'\n')

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

print("\n\nСинтаксический анализатор грамматики, основанной на трёх видах скобок с применением букв и знаков операций.")
print("\n\nФормулировка правил: Правильная скобочная запись арифметических выражений с тремя видами скобок. \nВнутри фигурных скобок обязательно должны быть квадратные, но могут быть круглые, внутри квадратных должны быть круглые или бесскобочные выражения, внутри круглых только бесскобочные арифметические выражения.\nТакже, если один из операндов является скобкой, то и второй должен быть скобкой (не может быть буквой).\nМогут быть “лишние” скобки, но одна буква не может браться в скобки.\n\n")

str = input("Введите запись: ")


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
cond_7 = True # внутри фигурных обязательны квадратные
cond_8 = True # внутри фигурных бесскобочное выражение
        
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
    
#print(str_1)

if (len(arr_A)!=len(arr_B))or(len(arr_C)!=len(arr_D))or(len(arr_E)!=len(arr_F)):
    print("ОШИБКА: скобочная запись не является правильной")
    cond_1 = False
i=0
for i in range(0, len(str)):
    if (str[i] in arr_sign):
        if (((str[i-1]in ch)or(str[i-1]in['{','}','[',']','(',')']))and((str[i+1]in ch)or(str[i+1]in['{','}','[',']','(',')']))):
            i=+7
        else:
            cond_6=False
            print("ОШИБКА: расстановка знаков оераций некорректна", i)

for i in range(0, len(arr_E)):
    for j in range (arr_E[i]+1, arr_F[i]):
        if (str_1[j]=='E' and str_1[j-1]!='E')or(str_1[j]=='A')or(str_1[j]=='B')or(str_1[j]=='C')or(str_1[j]=='D'):
            cond_2 = False
            print("ОШИБКА: внутри круглых скобок есть скобочные записи или круглые нелишние")
            #print(j)
if (cond_1 and cond_2 and cond_6):
    for i in range(0, len(arr_E)):
        if (arr_F[i]-arr_E[i]==2):
            cond_5 = False
            print("ОШИБКА: есть однобуквенные записи внутри круглых скобок")
if (cond_1 and cond_2 and cond_5 and cond_6):
    for i in range(0, len(arr_C)):
        for j in range(arr_C[i]+1, arr_D[i]):
            if (str_1[j]=='C' and str_1[j-1]!='C')or(str_1[j]=='A'):
                cond_3=False
                print("ОШИБКА: внутри квадратных скобок есть фигурные или квадратные нелишние")

if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6):
    for i in range (0, len(arr_A)):
        for j in range(arr_A[i]+1, arr_B[i]):
            if (str_1[j]=='A' and str_1[j-1]!='A'):
                cond_4=False
                print("ОШИБКА: внутри фигурных скобок есть фигурные нелишние")
                
if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6 and cond_4):
    for i in range (0, len(arr_A)):
        t_c = False
        for j in range(arr_A[i]+1, arr_B[i]):
            if (str_1[j]=='C'):
                t_c=True
        if (t_c==False):
            cond_7=False
            print("ОШИБКА: внутри фигурных нет обязательных квадратных")
            
if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6 and cond_4 and cond_7):
    for i in range (0, len(arr_A)):
        t_c = 0
        for p in range(0, len(arr_C)):
            if(arr_C[p]>arr_A[i]):
                t_c+=arr_D[p]-arr_C[p]
                #print("квадратная ", t_c)
                
        for p in range(0, len(arr_E)):
            if(arr_E[p]>arr_A[i]):
                t_c+=arr_F[p]-arr_E[p]
                #print("круглая ", t_c)
                
        for p in range(0, len(str)):
            if (str[p]in arr_sign)and(str[p-1]in[')',']','}'])and(str[p+1]in ['(','[','{']):
                t_c+=1
                #print("знак ",t_c)
        #print(arr_B[i]-arr_A[i]+1)      
        if (t_c < arr_B[i]-arr_A[i]+1):
            print("ОШИБКА: внутри фигурных скобок есть бесскобочные выражения")
            cond_8 = False

                
if (cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6 and cond_7 and cond_8):
    print("Введённая скобочная запись соответствует заданной грамматике")

