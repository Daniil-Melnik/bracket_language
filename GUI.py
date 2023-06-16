from tkinter import *
root = Tk()

root.geometry("1800x800")
root.title("Синтаксический анализатор")
string = ""
index = 0

def Hello(event):
    
    global index
    global string
    string = ""
    index = 0
    string = enter_field.get()
    try:
        PSZ()
        label_result.config(text="Введённая скобочная запись соответствует заданной грамматике", font=("Courier", 18, "bold"), fg="green")
        label_result.place(x=350, y=420)

    except Exception as e:
        label_result.config(text=e, font=("Courier", 18, "bold"), fg="red")

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





    

btn = Button(root,                  #родительское окно
             text="Проверить",       #надпись на кнопке
             width=20,height=3,     #ширина и высота
             bg="white",fg="black", font=("Courier", 18, "bold")) #цвет фона и надписи

btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
btn.place(x="600", y="310")

inf_frame = Frame(root)
inf_frame.config(width=1500, background="white", height=200)
inf_frame.pack()
inf_frame.place(x="15", y="5")

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
enter_field.place(x=600, y=260)

label_enter = Label(root, text="Введите запись: ")
label_enter.configure(font=("Courier", 18, "bold"))
label_enter.pack()
label_enter.place(x=300, y=250)

label_result = Label(root, text="результат проверки")
label_result.configure(font=("Courier", 18, "bold"))
label_result.pack()
label_result.place(x=600, y=420)

label_true = Label(root, text="Правильная запись: {[(a-b)](a+b)}/[(a+b*c )]-(a-c)*(a+c)")
label_true.configure(font=("Courier", 18, "bold"))
label_true.pack()
label_true.place(x=400, y=470)

label_false = Label(root, text="Неправильная запись: {(a+b)*(a-b)}/[a+b/c]((c)-(b-c*d))")
label_false.configure(font=("Courier", 18, "bold"))
label_false.pack()
label_false.place(x=405, y=520)

root.mainloop()