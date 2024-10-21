from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.geometry("700x300")
root['bg'] = '#f28c1f'
root.resizable(0, 0)

# Label - Title
label = Label(root, text="   ENCRYPTION AND DECRYPTION     ", font=("Times New Roman", 20, 'bold'),
              foreground="#000", width=45, border=5, background="#73ed42")
label.place(x=0, y=0, height=40)

# Function to encrypt the file
def encrypt_file():
    file1 = filedialog.askopenfilename(filetypes=[('Files', '*.jpg;*.png;*.jpeg;*.mp3;*.mp4')])
    if file1:
        key = entry1.get()
        if key.isdigit():  # Ensure key is a digit
            key = int(key)
        else:
            print("Please enter a valid numeric key.")
            return

        with open(file1, 'rb') as fi:
            data = bytearray(fi.read())
        
        # Encrypt data
        for index in range(len(data)):
            data[index] ^= key  # XOR operation for encryption
        
        with open(file1, 'wb') as fi1:
            fi1.write(data)

        print(f"File encrypted: {os.path.basename(file1)} with key: {key}")

# Function to decrypt the file
def decrypt_file():
    file1 = filedialog.askopenfilename(filetypes=[('Files', '*.jpg;*.png;*.jpeg;*.mp3;*.mp4')])
    if file1:
        key = entry1.get()
        if key.isdigit():  # Ensure key is a digit
            key = int(key)
        else:
            print("Please enter a valid numeric key.")
            return

        with open(file1, 'rb') as fi:
            data = bytearray(fi.read())
        
        # Decrypt data
        for index in range(len(data)):
            data[index] ^= key  # XOR operation for decryption
        
        with open(file1, 'wb') as fi1:
            fi1.write(data)

        print(f"File decrypted: {os.path.basename(file1)} with key: {key}")

# Label for input
t_label = Label(root, text="Enter / Set Password to your file:", font=("Times New Roman", 17, 'bold'),
                foreground="#000", width=32, border=10, background="#41c2c4")
t_label.place(x=90, y=80, height=35)

# Input values
entry1 = Entry(root, width=30, font=("Times New Roman", 17), background="#d1cbb2")
entry1.place(x=150, y=155, height=40)

# Encrypt Button
b1 = Button(root, text="ENCRYPT", font=("Times New Roman", 12, 'bold'), fg="#fff", background="#41c2c4",
            width=10, cursor="hand2", relief="groove", command=encrypt_file)
b1.place(x=100, y=230, height=30)

# Decrypt Button
b2 = Button(root, text="DECRYPT", font=("Times New Roman", 12, 'bold'), fg="#fff", background="#41c2c4",
            width=10, cursor="hand2", relief="groove", command=decrypt_file)
b2.place(x=450, y=230, height=30)

root.mainloop()
