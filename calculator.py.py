import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("calculator")
window.geometry("400x600")

def buttonclick(value):
    x = display_var.get()
    display_var.set(x+value)

def calculate():
    try:
        y = eval(display_var.get())
        display_var.set(y)
    except Exception as e:
        display_var.set(e)


display_var = tk.StringVar()
display = ttk.Entry(window,textvariable=display_var,font=("Arial",20),justify="right")
display.grid(row=0,column=0,columnspan=4,sticky="ewns",padx=10,pady=10)

#create button
button_7 = ttk.Button(window,text="7",command=lambda: buttonclick("7"))
button_7.grid(row=1,column=0,padx=10,pady=10,sticky="ewns")

button_8 = ttk.Button(window,text="8",command=lambda: buttonclick("8"))
button_8.grid(row=1,column=1,padx=10,pady=10,sticky="ewns")

button_9 = ttk.Button(window,text="9",command=lambda: buttonclick("9"))
button_9.grid(row=1,column=2,padx=10,pady=10,sticky="ewns")

button_4 = ttk.Button(window,text="4",command=lambda: buttonclick("4"))
button_4.grid(row=2,column=0,padx=10,pady=10,sticky="ewns")

button_5 = ttk.Button(window,text="5",command=lambda: buttonclick("5"))
button_5.grid(row=2,column=1,padx=10,pady=10,sticky="ewns")

button_6 = ttk.Button(window,text="6",command=lambda: buttonclick("6"))
button_6.grid(row=2,column=2,padx=10,pady=10,sticky="ewns")

button_1 = ttk.Button(window,text="1",command=lambda: buttonclick("1"))
button_1.grid(row=3,column=0,padx=10,pady=10,sticky="ewns")

button_2 = ttk.Button(window,text="2",command=lambda: buttonclick("2"))
button_2.grid(row=3,column=1,padx=10,pady=10,sticky="ewns")

button_3 = ttk.Button(window,text="3",command=lambda: buttonclick("3"))
button_3.grid(row=3,column=2,padx=10,pady=10,sticky="ewns")

button_0 = ttk.Button(window,text="0",command=lambda: buttonclick("0"))
button_0.grid(row=4,column=0,padx=10,pady=10,sticky="ewns")

button_point = ttk.Button(window,text=".",command=lambda: buttonclick("."))
button_point.grid(row=4,column=1,padx=10,pady=10,sticky="ewns")

#to thw power button
button_tp = ttk.Button(window,text="**",command=lambda: buttonclick("**"))
button_tp.grid(row=4,column=2,padx=10,pady=10,sticky="ewns")

#button Clear
button_C = ttk.Button(window,text="C",command=lambda: display_var.set(""))
button_C.grid(row=5,column=0,padx=10,pady=10,sticky="ewns",columnspan=2)

# division button
button_division = ttk.Button(window,text="/",command=lambda: buttonclick("/"))
button_division.grid(row=1,column=3,padx=10,pady=10,sticky="ewns")

#multiplication button
button_multiplication= ttk.Button(window,text="*",command=lambda: buttonclick("*"))
button_multiplication.grid(row=2,column=3,padx=10,pady=10,sticky="ewns")

#subtraction button
button_subtraction= ttk.Button(window,text="-",command=lambda: buttonclick("-"))
button_subtraction.grid(row=3,column=3,padx=10,pady=10,sticky="ewns")

#addition button
button_addition= ttk.Button(window,text="+",command=lambda: buttonclick("+"))
button_addition.grid(row=4,column=3,padx=10,pady=10,sticky="ewns")

#equalto button 
button_equalto= ttk.Button(window,text="=",command= calculate)
button_equalto.grid(row=5,column=2,padx=10,pady=10,sticky="ewns",columnspan=2)


#creating grid
for i in range(6):
    window.rowconfigure(i,weight=1)
for j in range(4):
    window.columnconfigure(j,weight=1)


window.mainloop()