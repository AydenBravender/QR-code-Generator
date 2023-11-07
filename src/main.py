import qrcode
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def Makeqrcode():
    image_txt = img_txt.get()
    image_dir = img_dir.get()
    image_name = img_name.get()
    image_size = img_size.get()
    cap.destroy()
    
    qr = qrcode.QRCode(version = image_size, box_size = 10, border = 5)
    qr.add_data(image_txt) #Adding the data to be encoded to the QRCode object
    qr.make(fit = True) #Making the entire QR Code space utilized
    img = qr.make_image() #Generating the QR Code
    try:
        fileDirec=image_dir+'\\'+image_name #Getting the directory where the file has to be save
        img.save(f'{fileDirec}.png') #Saving the QR Code
        #Showing the pop up message on saving the file
        messagebox.showinfo("File Manager", "QR Code is saved successfully!")
    except FileNotFoundError:
        print("Invalid file source, please try again")
        messagebox.showinfo("File Manager", "Invalid file source, please try again!")

cap = tk.Tk()

Header = cap.title('QR Generator')
my_canvas = tk.Canvas(cap, bg="black", height=430, width=600)
my_canvas.pack()

# adding the labels for the tkinter window
label_txt = tk.Label(cap, text='Enter text/URL: ')
label_txt.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 50, window=label_txt)

label_dir = tk.Label(cap, text='Where do you want the Qrcode to be saved?: ')
label_dir.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 130, window=label_dir)

label_name = tk.Label(cap, text='Enter name of Qr code: ')
label_name.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 200, window=label_name)

label_size = tk.Label(cap, text='Enter size of image: ')
label_size.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 260, window=label_size)


# creating input window
img_txt = tk.Entry(cap)
my_canvas.create_window(300, 100, height=30, width=400, window=img_txt)

# creating input window
img_dir = tk.Entry(cap)
my_canvas.create_window(300, 160, height=30, width=400, window=img_dir)

# creating input window
img_name = tk.Entry(cap)
my_canvas.create_window(300, 230, height=30, width=400, window=img_name)

# creating input window
img_size = tk.Entry(cap)
my_canvas.create_window(300, 300, height=30, width=400, window=img_size)


# the resize button
button = tk.Button(
    cap,
    text="Generate QR code",
    width=25,
    height=3,
    bg="white",
    fg="black",
    font=('helvetica', 10, 'bold'),
    command=Makeqrcode
    )

my_canvas.create_window(300, 350, height=40,width=150, window=button)

cap.mainloop()