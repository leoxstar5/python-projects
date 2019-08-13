from tkinter import *
root = Tk()
#----------root dimentions----------
width=300
height=150
s_width  =  root.winfo_screenwidth()
s_height  =  root.winfo_screenheight()
xpos = (s_width/2)-(width/2)
ypos = (s_height/2)-(height/2)

root.configure( bg='#088985')	# set dimentions of window
root.resizable(width=False, height=False)
root.geometry("%dx%d+%d+%d" % (width, height ,xpos ,ypos))	

#----------functions for widgets----------
bool = False
def c_to_f():
    C = float(var_e_1.get())
    F = C * 9/5 + 32
    
    label_1['text'] = str(F)+'°F'
    label_1.grid(row=1, column=1)
    globals()['bool'] = True    #True to indicate °C
    
def f_to_c():
    F = float(var_e_1.get())
    C = (F - 32) * 5/9
    
    label_2['text'] = str(C)+'°C'
    label_2.grid(row=2, column=1)
    
    globals()['bool'] = False   #False to indicate °F
    
def identify_c_or_f ():
    globals()['bool']
    if bool:
        label_3['text'] = 'You entered: '+var_e_1.get()+'°C'
        label_2['text'] = ''
        
    else:
        label_3['text'] = 'You entered: '+var_e_1.get()+'°F'
        label_1['text'] = ''    
        
#--------------------
#variables
var_e_1 = StringVar()	 
#_______widgets______
entry_of_degree = Entry(root, textvariable=var_e_1)
entry_of_degree.grid(row=0, column=0)

label_3 = Label(root)   # this displays what degree type the user entered via a command.
label_3.grid(row=0, column=1)

button_c_to_f = Button(root, text='convert to °F  ->>', bg='white', command=lambda:[c_to_f(), identify_c_or_f()])
button_c_to_f.grid(row=1, column=0)
label_2 = Label(root)

button_c_to_f = Button(root, text='convert to °C  ->>', bg='white', command=lambda:[f_to_c(), identify_c_or_f()])
button_c_to_f.grid(row=2, column=0)
label_1 = Label(root)

root.mainloop()
