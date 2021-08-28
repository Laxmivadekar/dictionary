import tkinter
from tkinter import*


root=tkinter.Tk()
root.title("Login page")
root.geometry("600x300")
root.configure(bg="red")
def validate():
    username1=text_username.get()
    password1=text_password.get()
    if username1=="shailaja" and password1=="bujji":
        Message.showinfo(username1,"logged successfully")
    else:
        Message.showinfo(username1,"try again")

username=Label(root,text="User Name",fg="white",bg="black",font="bold,15")
username.place(x=100,y=60)
password=Label(root,text="password",fg="white",bg="black",font="bold,15")
password.place(x=100,y=90)
text_username=Entry()
text_username.place(x=200,y=60)
text_password=Entry()
text_password.place(x=200,y=90)
submit=Button(root,text="submit",command=validate)
submit.place(x=200,y=140)

root.mainloop()