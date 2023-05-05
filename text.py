str = "{[(a-b)(a+b)]}/[(a+b*c)]-(a-z)*(a+c)"

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

arr_sign = []

k=0
str_1=[]

#print(str_1)

for i in str:
    str_1.append('*')

#print(str_1)

for i in range(0, len(str)):
    if (str[i] in ['{','}','[',']','(',')']):
        str_1[i] = dict[str[i]]
        
cond_1 = True
        
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

if (len(arr_A)!=len(arr_B))or(len(arr_C)!=len(arr_D))or(len(arr_E)!=len(arr_F)):
    print("Error, it is not a correct bracket sequence")
    cond_1 = False

if (cond_1):
    cond_2 = True
    for i in range(0, len(arr_A)):
        cond_fig_square = False
        for j in range(arr_A[i], arr_B[i]):
            if (str_1[j]=='C' or str_1[j]=='D'):
                cond_fig_square=True
                
        if (cond_fig_square==False):
            print("Error with figure-squre brackets")
            cond_2 = False

    for i in range(0, len(arr_A)):
        cond_fig_fig = True
        for j in range(arr_A[i]+1, arr_B[i]):
            if (str_1[j]=='A' or str_1[j]=='B'):
                cond_fig_fig=False
                
        if (cond_fig_fig==False):
            print("Error with figure-figure brackets")
            cond_2 = False
            
    for i in range(0, len(arr_A)):
        cond_fig_empty = True
        for j in range(arr_A[i]+1, arr_B[i]):
            if (str_1[j]=='A' or str_1[j]=='B'or str_1[j]=='C' or str_1[j]=='D' or str_1[j]=='E' or str_1[j]=='F'):
                cond_fig_empty=False
                
        if (cond_fig_empty==True):
            print("Error with figure-poor brackets")
            cond_2 = False
            
    for i in range(0, len(arr_C)):
        cond_square_circl = False
        for j in range(arr_C[i]+1, arr_D[i]):
            if (str_1[j]=='E' or str_1[j]=='F'):
                cond_square_circl=True
                
        if (cond_square_circl==False):
            print("Error with scuare-circl brackets")
            cond_2 = False
   
    for i in range(0, len(arr_C)):
            cond_square_square = False
            for j in range(arr_C[i]+1, arr_D[i]):
                if (str_1[j]=='C' or str_1[j]=='D'):
                    cond_square_square=True
                    
            if (cond_square_square==True):
                print("Error with scuare-square brackets")
                cond_2 = False
                
    for i in range(0, len(arr_C)):
            cond_square_fig = False
            for j in range(arr_C[i]+1, arr_D[i]):
                if (str_1[j]=='A' or str_1[j]=='B'):
                    cond_square_fig=True
                    
            if (cond_square_fig==True):
                print("Error with scuare-figure brackets")
                cond_2 = False

    for i in range(0, len(arr_E)):
            cond_circle_empty = False
            for j in range(arr_E[i]+1, arr_F[i]):
                if (str_1[j]=='A' or str_1[j]=='B'or str_1[j]=='C' or str_1[j]=='D' or str_1[j]=='E' or str_1[j]=='F'):
                    cond_circle_empty=True
                    
            if (cond_circle_empty==True):
                print("Error with circle-empty brackets")
                cond_2 = False
    if cond_2:
        cond_3=True
        for i in range(0, len(str)):
            if str[i] in ['+','-','*','/']:
                arr_sign.append(i)
        for i in range(0, len(arr_sign)):
            cond_term = False
            if ((str[arr_sign[i]+1] in ch) or (str[arr_sign[i]+1] in bracket_1))and((str[arr_sign[i]-1] in ch) or (str[arr_sign[i]-1] in bracket_2)):
                cond_term = True
            if (cond_term == False):
                print("Error vith term")
                cond_3=False