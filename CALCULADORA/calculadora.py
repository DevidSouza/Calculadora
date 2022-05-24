from tkinter import *
from tkinter import ttk

cor1 = '#01315e' # azul escuro
cor2 = '#1d2833' # preto
cor3 = '#eafcfb' # branco
cor4 = '#1b59b7' # azul claro

jan = Tk()
jan.title('Calculadora Blue')
jan.geometry('319x372')
jan.configure(bg=cor1)
jan.resizable(width=False, height=False)
# ALTERA ÍCONE
# PRIMEIRA MANEIRA (aceita apenas arquivos com extensão .ico):
jan.iconbitmap(default='icons/calc3.ico')
# SEGUNDA MANEIRA (aceita apenas arquivos com extensão .png):
#jan.iconphoto(False, PhotoImage(file='icons/calc.png'))

caracteres = ''
# EXIBE NÚMEROS
def exibe_num(txt, n):
    global caracteres
    numeros = '1234567890'
    if n in numeros:
        caracteres = caracteres + n
        txt.set(caracteres)
    else:
        try:
            if caracteres[-1] in numeros:
                caracteres = caracteres + n
                txt.set(caracteres)
        except IndexError:
            try:
                if res != '':
                    caracteres = str(res) + n
                    txt.set(caracteres)
            except NameError:
                pass


# LIMPA TELA
def limpa(txt):
    global res
    global caracteres
    caracteres = ''
    res = ''
    txt.set(''.strip())

# CALCULA A OPERAÇÃO

def calcular(txt):
    teste = ''
    global res
    global caracteres
    try:
        if '%' in caracteres:
            caracteres = caracteres.replace('%', '/100*')
            if caracteres[0] == '0':
                caracteres = '0/1'
                teste = '0/1'
            #if caracteres[-1] == '%':

        if 'x' in caracteres:
            caracteres = caracteres.replace('x', '*')
        if ',' in caracteres:
            caracteres = caracteres.replace(',', '.')
        try:
            teste = str(eval(caracteres))
        except ZeroDivisionError:
            teste = '0'
        try:
            if teste[-1] == '0' and teste[-2] == '.':
                res = eval(caracteres)
                res = str(res)
                res = res[:-2]
                txt.set(res + ' =')
            else:
                res = eval(caracteres)
                txt.set(str(res) + ' =')
            caracteres = ''
        except IndexError:
            caracteres = 'Impossível dividir por 0'
            res = caracteres
            txt.set(res)
            res = ''
            caracteres = ''
    except SyntaxError:
        pass

# variável que pega o valor repassado no segundo argumento da função "exibe_num"
texto = StringVar()

# CRIANDO FRAMES
framecima = Frame(jan, width=318, height=90, bg=cor1)
framecima.grid(row=0, column=0)


framebaixo = Frame(jan, width=318, height=340, bg=cor1)
framebaixo.grid(row=1, column=0)


# CRIANDO TELA ONDE APARECERÁ AS OPERAÇÕES (LABEL)
mostra_num = Label(framecima, textvariable=texto, width=18, height=4, padx=5, fg=cor3, bg=cor1, font=('ArialBlack 22'), relief=FLAT, anchor='e')
mostra_num.place(x=0, y=0)

#CRIANDO BOTÕES
b1 = Button(framebaixo, text='C', width=21, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: limpa(texto))
b1.place(x=1, y=3)

b2 = Button(framebaixo, text='%', width=11, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '%'))
b2.place(x=153, y=3)

b3 = Button(framebaixo, text='/', width=11, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '/'))
b3.place(x=235, y=3)

b4 = Button(framebaixo, text='7', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '7'))
b4.place(x=1, y=59)

b5 = Button(framebaixo, text='8', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '8'))
b5.place(x=77, y=59)

b6 = Button(framebaixo, text='9', width=12, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '9'))
b6.place(x=153, y=59)

b7 = Button(framebaixo, text='x', width=11, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, 'x'))
b7.place(x=235, y=59)

b8 = Button(framebaixo, text='6', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '6'))
b8.place(x=1, y=115)

b9 = Button(framebaixo, text='5', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '5'))
b9.place(x=77, y=115)

b10 = Button(framebaixo, text='4', width=12, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '4'))
b10.place(x=153, y=115)

b11 = Button(framebaixo, text='-', width=11, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '-'))
b11.place(x=235, y=115)

b12 = Button(framebaixo, text='3', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '3'))
b12.place(x=1, y=171)

b13 = Button(framebaixo, text='2', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '2'))
b13.place(x=77, y=171)

b14 = Button(framebaixo, text='1', width=12, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '1'))
b14.place(x=153, y=171)

b15 = Button(framebaixo, text='+', width=11, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '+'))
b15.place(x=235, y=171)

b16 = Button(framebaixo, text='0', width=10, height=3, bg=cor1, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, '0'))
b16.place(x=1, y=227)

b17 = Button(framebaixo, text=',', width=10, height=3, bg=cor4, fg=cor3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: exibe_num(texto, ','))
b17.place(x=77, y=227)

b18 = Button(framebaixo, text='=', width=22, height=3, bg=cor4, fg=cor3, padx=3, font=('ArialBlack 9 bold'), relief='raised', overrelief=RIDGE, command=lambda: calcular(texto))
b18.place(x=153, y=227)

jan.mainloop()
