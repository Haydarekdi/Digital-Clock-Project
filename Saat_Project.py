from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Dijital Saat")
app_window.geometry("400x200")
app_window.resizable(0,0)
app_window.configure(bg="black")

label = Label(app_window,font=("Boulder",36,'bold'), bg="black", fg="white")
label.grid(row=0, column=1, padx=20, pady=20)

date_label = Label(app_window,font=("Boulder",36,'bold'), bg="black", fg="white")
date_label.grid(row=1, column=1, padx=20, pady=20)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    label.after(200,digital_clock)
    
digital_clock()    
    












app_window.mainloop()