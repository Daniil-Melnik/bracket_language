from tkinter import *
root = Tk()

root.geometry("1800x800")
root.title("Синтаксический анализатор")

def Hello(event):
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


    str = enter_field.get()


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
        label_result.config(text="ОШИБКА: скобочная запись не является правильной", font=("Courier", 18, "bold"), fg="red")
        label_result.place(x=550, y=400)
        cond_1 = False
    i=0
    for i in range(0, len(str)):
        if (str[i] in arr_sign):
            if (((str[i-1]in ch)or(str[i-1]in['{','}','[',']','(',')']))and((str[i+1]in ch)or(str[i+1]in['{','}','[',']','(',')']))):
                i=+7
            else:
                cond_6=False
                print("ОШИБКА: расстановка знаков оераций некорректна", i)
                label_result.config(text="ОШИБКА: расстановка знаков оераций некорректна", font=("Courier", 18, "bold"), fg="red")
                label_result.place(x=550, y=400)

    for i in range(0, len(arr_E)):
        for j in range (arr_E[i]+1, arr_F[i]):
            if (str_1[j]=='E' and str_1[j-1]!='E')or(str_1[j]=='A')or(str_1[j]=='B')or(str_1[j]=='C')or(str_1[j]=='D'):
                cond_2 = False
                print("ОШИБКА: внутри круглых скобок есть скобочные записи или круглые нелишние")
                label_result.config(text="ОШИБКА: внутри круглых скобок есть скобочные записи или круглые нелишние", font=("Courier", 18, "bold"), fg="red")
                label_result.place(x=420, y=400)
                #print(j)
    if (cond_1 and cond_2 and cond_6):
        for i in range(0, len(arr_E)):
            if (arr_F[i]-arr_E[i]==2):
                cond_5 = False
                print("ОШИБКА: есть однобуквенные записи внутри круглых скобок")
                label_result.config(text="ОШИБКА: есть однобуквенные записи внутри круглых скобок", font=("Courier", 18, "bold"), fg="red")
                label_result.place(x=550, y=400)
    if (cond_1 and cond_2 and cond_5 and cond_6):
        for i in range(0, len(arr_C)):
            for j in range(arr_C[i]+1, arr_D[i]):
                if (str_1[j]=='C' and str_1[j-1]!='C')or(str_1[j]=='A'):
                    cond_3=False
                    print("ОШИБКА: внутри квадратных скобок есть фигурные или квадратные нелишние")
                    label_result.config(text="ОШИБКА: внутри квадратных скобок есть фигурные или квадратные нелишние", font=("Courier", 18, "bold"), fg="red")
                    label_result.place(x=430, y=400)

    if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6):
        for i in range (0, len(arr_A)):
            for j in range(arr_A[i]+1, arr_B[i]):
                if (str_1[j]=='A' and str_1[j-1]!='A'):
                    cond_4=False
                    print("ОШИБКА: внутри фигурных скобок есть фигурные нелишние")
                    label_result.config(text="ОШИБКА: внутри фигурных скобок есть фигурные нелишние", font=("Courier", 18, "bold"), fg="red")
                    label_result.place(x=500, y=400)
                    
    if (cond_1 and cond_2 and cond_3 and cond_5 and cond_6 and cond_4):
        for i in range (0, len(arr_A)):
            t_c = False
            for j in range(arr_A[i]+1, arr_B[i]):
                if (str_1[j]=='C'):
                    t_c=True
            if (t_c==False):
                cond_7=False
                print("ОШИБКА: внутри фигурных нет обязательных квадратных")
                label_result.config(text="ОШИБКА: внутри фигурных нет обязательных квадратных", font=("Courier", 18, "bold"), fg="red")
                label_result.place(x=550, y=400)
                
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
                label_result.config(text="ОШИБКА: внутри фигурных скобок есть бесскобочные выражения", font=("Courier", 18, "bold"), fg="red")
                label_result.place(x=500, y=400)
                cond_8 = False

                    
    if (cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6 and cond_7 and cond_8):
        print("Введённая скобочная запись соответствует заданной грамматике")
        label_result.config(text="Введённая скобочная запись соответствует заданной грамматике", font=("Courier", 18, "bold"), fg="green")
        label_result.place(x=500, y=400)
    

btn = Button(root,                  #родительское окно
             text="Проверить",       #надпись на кнопке
             width=20,height=3,     #ширина и высота
             bg="white",fg="black", font=("Courier", 18, "bold")) #цвет фона и надписи

btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
btn.place(x="750", y="300")

inf_frame = Frame(root)
inf_frame.config(width=1500, background="white", height=200)
inf_frame.pack()
inf_frame.place(x="150", y="5")

inf_label_1 = Label(inf_frame, text="Синтаксический анализатор грамматики, основанной на трёх видах скобок с применением букв и знаков операций.")
inf_label_1.configure(font=("Courier", 18, "bold"), background="white")
inf_label_1.pack()
inf_label_1.place(x=0)

inf_label_2 = Label(inf_frame, text="Формулировка правил:")
inf_label_2.configure(font=("Courier", 18, "bold"), background="white")
inf_label_2.pack()
inf_label_2.place(x=0, y=25)

inf_label_3 = Label(inf_frame, text="1) Правильная скобочная запись арифметических выражений с тремя видами скобок.")
inf_label_3.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_3.pack()
inf_label_3.place(x=0, y=50)

inf_label_4 = Label(inf_frame, text="2) Внутри фигурных скобок обязательно должны быть квадратные, но могут быть круглые")
inf_label_4.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_4.pack()
inf_label_4.place(x=0, y=75)

inf_label_5 = Label(inf_frame, text="3) Внутри квадратных должны быть круглые или бесскобочные выражения")
inf_label_5.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_5.pack()
inf_label_5.place(x=0, y=100)

inf_label_6 = Label(inf_frame, text="4) Внутри круглых только бесскобочные арифметические выражения")
inf_label_6.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_6.pack()
inf_label_6.place(x=0, y=125)

inf_label_7 = Label(inf_frame, text="5) Если один из операндов является скобкой, то и второй должен быть скобкой (не может быть буквой)")
inf_label_7.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_7.pack()
inf_label_7.place(x=0, y=150)

inf_label_8 = Label(inf_frame, text="6) Могут быть “лишние” скобки, но одна буква не может браться в скобки")
inf_label_8.configure(font=("Courier", 14, "bold"), fg="#757575", background="white")
inf_label_8.pack()
inf_label_8.place(x=0, y=175)

enter_field = Entry(width=100)
enter_field.pack()
enter_field.place(x=600, y=250)

label_enter = Label(root, text="Введите запись: ")
label_enter.configure(font=("Courier", 18, "bold"))
label_enter.pack()
label_enter.place(x=300, y=250)

label_result = Label(root, text="результат проверки")
label_result.configure(font=("Courier", 18, "bold"))
label_result.pack()
label_result.place(x=775, y=400)

label_true = Label(root, text="Правильная запись: {[(a-b)](a+b)}/[(a+b*c )]-(a-c)*(a+c)")
label_true.configure(font=("Courier", 18, "bold"))
label_true.pack()
label_true.place(x=500, y=450)

label_false = Label(root, text="Неправильная запись: {(a+b)*(a-b)}/[a+b/c]((c)-(b-c*d))")
label_false.configure(font=("Courier", 18, "bold"))
label_false.pack()
label_false.place(x=505, y=500)

root.mainloop()