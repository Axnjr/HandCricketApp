from tkinter import *
import random

window = Tk()
label_1 = Label(window, text="HAND CRICKET", font=('Calibre Light', 96), padx=160, pady=50, bg='black', fg='#2a9df4')
label_1.pack()
window.geometry("1300x900")
window.title('YAKSHIT')
window.config(background='')
entry = Entry(window, font=('Calibre Light', 84), fg='black', bg='#2a9df4')
entry.place(x=925, y=455)
label_2 = Label(window, text='ENTER NUMBER:', font=('Calibre Light', 83), fg='black', bg='#2a9df4')
label_2.place(x=0, y=455)
# choice module
en = Entry(window, font=('Calibre Light', 85), fg='black', bg='#2a9df4')
en.place(x=855, y=270)
label_6 = Label(window, text="ENTER CHOICE", font=('Calibre Light', 84), fg='black', bg='#2a9df4')
label_6.place(x=0, y=270)


def click():
    def bat():
        new_window.destroy()
        window_1 = Tk()
        window_1.title('YAKSHIT')
        window_1.config(background='black')
        label_9 = Label(window_1, text="YOU", font=('Calibre Light', 84), fg='black', bg='#2a9df4')
        label_9.place(x=1040, y=250)
        label_10 = Label(window_1, text="HIM..", font=('Calibre Light', 84), fg='black', bg='#2a9df4')
        label_10.place(x=0, y=250)
        label_8 = Label(window_1, text=f" SCORE={0} ", font=('Calibre Light', 90), fg='black', bg='#2a9df4')
        label_8.pack()

        def bol():
            entry_11 = Entry(window_1, font=('Calibre Light', 90), fg='black', bg='#2a9df4', width=4)
            entry_11.place(x=1040, y=400)
            h = entry_11.get()
            entry_11.insert(0, f'{h}')
            j = random.randint(1, 20)
            entry_8 = Entry(window_1, font=('Calibre Light', 90), fg='black', bg='#2a9df4', width=4)
            entry_8.place(x=0, y=400)
            entry_8.insert(0, f'{j}')
            if h == j:
                hat()

        def hat():
            label_11 = Label(window_1, text="out", font=('Calibre Light', 490), fg='black', bg='#2a9df4', width=4)
            label_11.place(x=0, y=0)

        button_4 = Button(window_1, text="sub", font=('Calibre Light', 90), fg='black', bg='#2a9df4', command=bol)
        button_4.place(x=500, y=250)

    x = int(entry.get())
    y = str(en.get())
    choice = ''
    if y.lower() == "odd":
        choice = 'odd'
    if y.lower() == "even":
        choice = 'even'
    g = random.randint(1, 11)
    if g == 11:
        g = 20
    s = x + g
    c = s % 2
    window.destroy()
    new_window = Tk()
    new_window.geometry("1300x900")
    new_window.title('YAKSHIT')
    new_window.config(background='')
    state = ''
    if c == 0:
        state = 'even'
    if c == 1:
        state = 'odd'
    if choice == state:
        button_1 = Button(new_window, font=('Calibre Light', 1200), bg='white', activebackground='black')
        button_1.place(x=0, y=0)
        label_7 = Label(new_window, text='YOU WON', font=('Calibre Light', 197), fg='black', bg='red', pady=10)
        label_7.place(x=0, y=0)
        entry_3 = Entry(new_window, font=('Calibre Light', 90), fg='black', bg='red')
        entry_3.place(x=0, y=330)
        entry_3.insert(0, "        CHOOSE TO!....")
        button_2 = Button(new_window, text="BATTING", font=('Calibre Light', 70), fg='black', bg='red', command=bat)
        button_3 = Button(new_window, text="BOWLING", font=('Calibre Light', 70), fg='black', bg='red', command=bat)
        button_2.place(x=800, y=500)
        button_3.place(x=0, y=500)
    if choice != state:
        button_1 = Button(new_window, font=('Calibre Light', 1200), bg='white', activebackground='black', command=bat)
        button_1.place(x=0, y=0)
        label_5 = Label(new_window, text='I WON', font=('Calibre Light', 197), fg='black', bg='red', pady=10)
        label_5.place(x=200, y=0)
        entry_3 = Entry(new_window, font=('Calibre Light', 90), fg='black', bg='red')
        entry_3.place(x=0, y=330)
        lis = ['BATTING', 'BOWLING']
        p = random.choice(lis)
        entry_3.insert(0, f'I WILL CHOOSE TO!....')
        label_4 = Label(new_window, text=f"{p}", font=('Calibre Light', 70), fg='black', bg='red')
        label_4.place(x=400, y=500)


button = Button(window, text='SUBMIT', bg='black', fg='#2a9df4', font=('Calibre Light', 20), command=click)
button.place(x=1158, y=401)

window.mainloop()
