import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog


def generate():
    qr = qrcode.QRCode(version = 3,
                   box_size = 8,
                   border = 1.5) 
    qr.add_data(tex.get())
    qr.make()
    img = qr.make_image()
   
    img.save(tex.get()+'.jpg')
    messagebox.showinfo("CONGRATES","GENERATED")
    
def show():

    image_path = tex.get()+'.jpg'
    img = Image.open(image_path) 
    img_tk = ImageTk.PhotoImage(img)
    messagebox.showinfo("QR code","LOADING")

    label_img.config(image=img_tk)
    label_img.image = img_tk

win=Tk()
win.title("QR GENERATOR")
win.geometry("700x700")
win.config(bg='skyblue')

headingframe=Frame(win,bg="azure",bd=5)
headingframe.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headinglabel=Label(headingframe,text='QR CODE GENERATOR BY ROHTASH',bg='blue', font=('Times',18))
headinglabel.place(relx=0,rely=0, relwidth=1, relheight=1)

text = Label(win, text="TEXT:",bg='blue',font=('times',15))
text.place(relx=0.10,rely=0.20)

tex=Entry(win,font=('times',15))
tex.place(relx=0.19,rely=0.20)

generate1=Button(win,bg='blue',text="GENERATE",command=generate)
generate1.place(relx=0.20,rely=0.25)

show1=Button(win,bg='blue',text="SHOW",command=show)
show1.place(relx=0.40,rely=0.25)

label_img = Label(win)
label_img.place(relx=0.20,rely=0.35)

win.mainloop()