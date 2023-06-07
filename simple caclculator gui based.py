from tkinter import *
root = Tk()
root.title("simple calculator")
#root.geometry("300x400")
e =Entry(root,width = 40,borderwidth =5)
st =""
ans =""
e.grid(column =0,row =0,columnspan =6 ,padx =10,pady =10,sticky = 'nsew')

def click0():
    global st
    st+='0'
    e.delete(0,END)
    e.insert(0,st)


def click1():
    global st
    st+='1'
    e.delete(0,END)
    e.insert(0,st)

def click2():
    global st
    st+='2'
    e.delete(0,END)
    e.insert(0,st)

def click3():
    global st
    st+='3'
    e.delete(0,END)
    e.insert(0,st)

def click4():
    global st
    st+='4'
    e.delete(0,END)
    e.insert(0,st)

def click5():
    global st
    st+='5'
    e.delete(0,END)
    e.insert(0,st)

def click6():
    global st
    st+='6'
    e.delete(0,END)
    e.insert(0,st)

def click7():
    global st
    st+='7'
    e.delete(0,END)
    e.insert(0,st)

def click8():
    global st
    st+='8'
    e.delete(0,END)
    e.insert(0,st)

def click9():
    global st
    st+='9'
    e.delete(0,END)
    e.insert(0,st)

def clickp():
    global st
    st+='+'
    e.delete(0,END)
    e.insert(0,st)

def clickm():
    global st
    st+='-'
    e.delete(0,END)
    e.insert(0,st)

def clicke():
    global st
    global ans
    try:
        e.delete(0,END)
        e.insert(0,str(eval(st)))
    except Exception  as s:
        st =""
        e.delete(0,END)
        e.insert(0,"ERROR INVALID")
    else:
        e.delete(0,END)
        e.insert(0,eval(st))
        ans = str(eval(st))
        st =""


def clickmu():
    global st
    st+='*'
    e.delete(0,END)
    e.insert(0,st)

def clickd():
    global st
    st+='/'
    e.delete(0,END)
    e.insert(0,st)

def clickmo():
    global st
    st+='%'
    e.delete(0,END)
    e.insert(0,st)

def clickr():
    global st
    if(st!=''):
        st = st[0:-1]
        e.delete(0,END)
        e.insert(0,st)

def clicka():
    global ans
    global st
    st = ans
    e.delete(0,END)
    e.insert(0,"ANS")

def clickac():
    global st
    st =''
    e.delete(0,END)

def quit():
    root.quit()

button1 = Button(root,text ="1",padx=30,pady=30,highlightthickness =0,command = click1)
button1.grid(row=1,column=0)
button2 = Button(root,text ="2",padx=30,pady=30,highlightthickness =0,command = click2)
button2.grid(row=1,column=1)
button3 = Button(root,text ="3",padx=30,pady=30,highlightthickness =0,command = click3)
button3.grid(row=1,column=2)
button4 = Button(root,text ="4",padx=30,pady=30,highlightthickness =0,command = click4)
button4.grid(row=2,column=0)
button5 = Button(root,text ="5",padx=30,pady=30,highlightthickness =0,command = click5)
button5.grid(row=2,column=1)
button6 = Button(root,text ="6",padx=30,pady=30,highlightthickness =0,command = click6)
button6.grid(row=2,column=2)
button7 = Button(root,text ="7",padx=30,pady=30,highlightthickness =0,command = click7)
button7.grid(row=3,column=0)
button8 = Button(root,text ="8",padx=30,pady=30,highlightthickness =0,command = click8)
button8.grid(row=3,column=1)
button9 = Button(root,text ="9",padx=30,pady=30,highlightthickness =0,command = click9)
button9.grid(row=3,column=2)
buttonp = Button(root,text='+',padx = 10,pady =30,highlightthickness =0,command = clickp)
buttonp.grid(row = 1,column = 3)
buttonm = Button(root,text='- ',padx = 10,pady =30,highlightthickness =0,command = clickm)
buttonm.grid(row = 2,column = 3)
buttone = Button(root,text='=',padx = 10,pady =30,highlightthickness =0,command = clicke)
buttone.grid(row = 3,column = 3)
buttonmu = Button(root,text='*',padx = 10,pady =30,highlightthickness =0,command = clickmu)
buttonmu.grid(row = 1,column = 4)
buttond = Button(root,text='/',padx = 10,pady =30,highlightthickness =0,command = clickd)
buttond.grid(row = 2,column = 4)
buttonmo = Button(root,text='%',padx = 10,pady =30,highlightthickness =0,command = clickmo)
buttonmo.grid(row = 3,column = 4)
buttonr = Button(root,text='⬅',padx = 10,pady =30,highlightthickness =0,command = clickr)
buttonr.grid(row = 3,column = 5)
buttona = Button(root,text='ANS',padx = 10,pady =30,highlightthickness =0,command = clicka)
buttona.grid(row = 2,column = 5)
buttonac = Button(root,text='AC',padx = 10,pady =30,highlightthickness =0,command = clickac)
buttonac.grid(row = 1,column = 5)
buttonaq = Button(root,text='QUIT',padx = 45,pady =10,highlightthickness =0,command = quit)
buttonaq.grid(row = 4,column = 3,columnspan=3)
button0 = Button(root,text ="0",padx=105,pady=10,highlightthickness =0,command = click0)
button0.grid(row=4,column=0,columnspan=3)

root.mainloop()