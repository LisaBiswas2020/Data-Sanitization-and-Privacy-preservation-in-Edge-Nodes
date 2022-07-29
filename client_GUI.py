import socket  
import tkinter as tk
from tkinter import font
from tkinter import ttk 
from tkinter import filedialog
import time
import threading
import os
from drive_store import data_to_drive
#from mesblock import messagechecker
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
import pathlib

from masking_img_api import image_masking_api,image_masking_api_pdf


from csv_secure_data import csv_secured_data_api
#from image_tester import image_checker
image_ext_list=[".PNG",".png",".jpeg",".jpg",".JPEG",".JPG"]
pdf_ext_list=[".PDF",".pdf"]
csv_ext_list=[".CSV",".csv"]

from data_encryption_images import decc_aes_key,decryptimg

from data_encryption_pdf import decryptpdf

from data_encryption_csv import decryptcsv

class GUI:
    
    def __init__(self, ip_address, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ip_address, port))

        self.Window = tk.Tk()
        self.Window.withdraw()

        self.login = tk.Toplevel()

        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=350)

        self.pls = tk.Label(self.login, 
                            text="ENTER CREDNTIALS", 
                            justify=tk.CENTER,
                            font="Helvetica 12 bold")

        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.userLabelName = tk.Label(self.login, text="Username: ", font="Helvetica 11")
        self.userLabelName.place(relheight=0.2, relx=0.1, rely=0.25)

        self.userEntryName = tk.Entry(self.login, font="Helvetica 12")
        self.userEntryName.place(relwidth=0.4 ,relheight=0.1, relx=0.35, rely=0.30)
        self.userEntryName.focus()

        self.roomLabelName = tk.Label(self.login, text="SECREATE COMMUNICATION ID: ", font="Helvetica 12")
        self.roomLabelName.place(relheight=0.2, relx=0.1, rely=0.40)

        self.roomEntryName = tk.Entry(self.login, font="Helvetica 11", show="*")
        self.roomEntryName.place(relwidth=0.4 ,relheight=0.1, relx=0.35, rely=0.45)
        
        self.go = tk.Button(self.login, 
                            text="CONTINUE", 
                            font="Helvetica 12 bold", 
                            command = lambda: self.goAhead(self.userEntryName.get(), self.roomEntryName.get()))
        
        self.go.place(relx=0.35, rely=0.62)

        self.Window.mainloop()


    def goAhead(self, username, room_id=0):
        self.name = username
        self.server.send(str.encode(username))
        time.sleep(0.1)
        self.server.send(str.encode(room_id))
        
        self.login.destroy()
        self.layout()

        rcv = threading.Thread(target=self.receive) 
        rcv.start()


    def layout(self):
        self.Window.deiconify()
        self.Window.title("SECURE DATA EXCHANGE")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")
        self.chatBoxHead = tk.Label(self.Window, 
                                    bg = "#17202A", 
                                    fg = "#EAECEE", 
                                    text = self.name , 
                                    font = "Helvetica 11 bold", 
                                    pady = 5)

        self.chatBoxHead.place(relwidth = 1)

        self.line = tk.Label(self.Window, width = 450, bg = "#ABB2B9") 
        
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012) 
        
        self.textCons = tk.Text(self.Window, 
                                width=20, 
                                height=2, 
                                bg="#17202A", 
                                fg="#EAECEE", 
                                font="Helvetica 11", 
                                padx=5, 
                                pady=5) 
        
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08) 
        
        self.labelBottom = tk.Label(self.Window, bg="#ABB2B9", height=80) 
        
        self.labelBottom.place(relwidth = 1, 
                                rely = 0.8) 
        
        self.entryMsg = tk.Entry(self.labelBottom, 
                                bg = "#2C3E50", 
                                fg = "#EAECEE", 
                                font = "Helvetica 11")
        self.entryMsg.place(relwidth = 0.74, 
                            relheight = 0.03, 
                            rely = 0.008, 
                            relx = 0.011) 
        self.entryMsg.focus()

        self.buttonMsg = tk.Button(self.labelBottom, 
                                text = "Send", 
                                font = "Helvetica 10 bold", 
                                width = 20, 
                                bg = "#ABB2B9", 
                                command = lambda : self.sendButton(self.entryMsg.get())) 
        self.buttonMsg.place(relx = 0.77, 
                            rely = 0.008, 
                            relheight = 0.03, 
                            relwidth = 0.22) 


        self.labelFile = tk.Label(self.Window, bg="#ABB2B9", height=70) 
        
        self.labelFile.place(relwidth = 1, 
                                rely = 0.9) 
        
        self.fileLocation = tk.Label(self.labelFile, 
                                text = "Choose file to send",
                                bg = "#2C3E50", 
                                fg = "#EAECEE", 
                                font = "Helvetica 11")
        self.fileLocation.place(relwidth = 0.65, 
                                relheight = 0.03, 
                                rely = 0.008, 
                                relx = 0.011) 

        self.browse = tk.Button(self.labelFile, 
                                text = "Browse", 
                                font = "Helvetica 10 bold", 
                                width = 13, 
                                bg = "#ABB2B9", 
                                command = self.browseFile)
        self.browse.place(relx = 0.67, 
                            rely = 0.008, 
                            relheight = 0.03, 
                            relwidth = 0.15) 

        self.sengFileBtn = tk.Button(self.labelFile, 
                                text = "Send", 
                                font = "Helvetica 10 bold", 
                                width = 13, 
                                bg = "#ABB2B9", 
                                command = self.sendFile)
        self.sengFileBtn.place(relx = 0.84, 
                            rely = 0.008, 
                            relheight = 0.03, 
                            relwidth = 0.15)
    

        self.textCons.config(cursor = "arrow")
        scrollbar = tk.Scrollbar(self.textCons) 
        scrollbar.place(relheight = 1, 
                        relx = 0.974)

        scrollbar.config(command = self.textCons.yview)
        self.textCons.config(state = tk.DISABLED)


    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", 
                                    title="Select a file",
                                    filetypes = (("Text files", 
                                                "*.txt*"), 
                                                ("all files", 
                                                "*.*")))
        self.fileLocation.configure(text="File Opened: "+ self.filename)


    def sendFile(self):


        print(self.filename)
      #  file_name = '/home/admin1/Desktop/46350aeb4ab47aafc91a5557c76405e6.pdf'
       # print(os.path.splitext(file_name))
        #out1=list(os.path.splitext(self.filename))
        #print(out1[-1])
        #out_ext=out1[-1]
# function to return the file extension
        file_extension = pathlib.Path(self.filename).suffix
        print("File Extension: ", file_extension)


       # print("file extention is ",out_ext)
        if  file_extension in image_ext_list:
            print("image sent for preprocessing")
            image_masking_api(self.filename)
            self.filename="encrypted_image.enc"
            

        elif  file_extension in pdf_ext_list:
            print("the documents is pdf")
            image_masking_api_pdf(self.filename)
            self.filename="encrypted_pdf.enc"
        elif file_extension in csv_ext_list:

            print("document is csv")
            csv_secured_data_api(self.filename)
            self.filename="encrypted_csv.enc"

        else:
            print("file is not image or pdf")

       # result_good_bad=image_checker(self.filename)
        #print(result_good_bad)

       # if  result_good_bad=="verified":                   

        self.server.send("FILE".encode())
        time.sleep(0.1)
#if result_good_bad=="verified":
        self.server.send(str("client_" + os.path.basename(self.filename)).encode())
        time.sleep(0.1)
        self.server.send(str(os.path.getsize(self.filename)).encode())
        time.sleep(0.1)

        file = open(self.filename, "rb")
        data = file.read(1024)
        while data:
            self.server.send(data)
            data = file.read(1024)
        self.textCons.config(state=tk.DISABLED)
        self.textCons.config(state = tk.NORMAL)
        self.textCons.insert(tk.END, "<You> "
                                     + str(os.path.basename(self.filename)) 
                                     + " Sent\n\n")
        self.textCons.config(state = tk.DISABLED) 
        self.textCons.see(tk.END)
      #  else:
      #      self.server.send(str(os.path.getsize(self.filename)).encode())
       #     time.sleep(0.1)
                    #self.server.send(str("")
                    #time.sleep(0.1)
                    #self.server.send(str(os.path.getsize(self.filename)).encode())
                    #time.sleep(0.1)
               #     self.textCons.config(state=tk.DISABLED)
               #     self.textCons.config(state = tk.NORMAL)
               ##     self.textCons.insert(tk.END, "<You> "
              #                                   + str(os.path.basename(self.filename)) 
               #                                  + " This message is blocked \n\n")
              #      self.textCons.config(state = tk.DISABLED) 
              #      self.textCons.see(tk.END)
             #       print("image have been blocked")

    def sendButton(self, msg):
        self.textCons.config(state = tk.DISABLED) 
        self.msg=msg 
        self.entryMsg.delete(0, tk.END) 
        snd= threading.Thread(target = self.sendMessage) 
        snd.start() 


    def receive(self):
        while True:
           # try:
                message = self.server.recv(1024).decode()

                if str(message) == "FILE":
                    file_name = self.server.recv(1024).decode()
                    lenOfFile = self.server.recv(1024).decode()
                    send_user = self.server.recv(1024).decode()

                    if os.path.exists(file_name):
                        os.remove(file_name)

                    total = 0
                    with open(file_name, 'wb') as file:
                        while str(total) != lenOfFile:
                            data = self.server.recv(1024)
                            total = total + len(data)     
                            file.write(data)
                    import pickle #credits to stack overflow user= blender

#a = {'hello': 'world'}

                   # with open('filename.pkl', 'wb') as handle:
                     #   pickle.dump(em, handle, protocol=pickle.HIGHEST_PROTOCOL)

                    with open('client_encrpted_aes_key.pkl', 'rb') as handle:
                        b = pickle.load(handle)
                    print (b)


                    aes_key_for_data=decc_aes_key(b)
                    #print()
                    #file123.close()

                    if file_name=="client_encrypted_image.enc":


                                      decryptimg(aes_key_for_data)
                                      target_filename="client_encrypted_image.encdecrypted_image.png"
                                      data_to_drive("client_encrypted_image.encdecrypted_image.png", target_filename)

                    elif file_name=="client_encrypted_pdf.enc":


                                      decryptpdf(aes_key_for_data)
                                      target_filename="client_encrypted_pdf.encdecrypted_pdf.pdf"
                                      data_to_drive("client_encrypted_pdf.encdecrypted_pdf.pdf", target_filename)


                    elif file_name=="client_encrypted_csv.enc":


                                      decryptcsv(aes_key_for_data)
                                      target_filename="client_encrypted_csv.encdecrypted_csv.csv"
                                      data_to_drive("client_encrypted_csv.encdecrypted_csv.csv", target_filename)


                    else:

                        print("data is not for masking")

                    
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state = tk.NORMAL)
                    self.textCons.insert(tk.END, "<" + str(send_user) + "> " + file_name + " Received\n\n")
                    self.textCons.config(state = tk.DISABLED) 
                    self.textCons.see(tk.END)


                else:
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state = tk.NORMAL)
                    self.textCons.insert(tk.END, 
                                    message+"\n\n") 

                    self.textCons.config(state = tk.DISABLED) 
                    self.textCons.see(tk.END)

          #  except: 
               # print("An error occured!") 
               # self.server.close() 
               # break

    def sendMessage(self):
        self.textCons.config(state=tk.DISABLED) 
        while True:  
            print(self.msg)
            message_checking=self.msg
            message_that_checked=message_checking

            self.server.send(message_that_checked.encode())
            self.textCons.config(state = tk.NORMAL)
            self.textCons.insert(tk.END, 
                            "<You> " + self.msg + "\n\n") 

            self.textCons.config(state = tk.DISABLED) 
            self.textCons.see(tk.END)
            break



if __name__ == "__main__":
    ip_address = "192.168.1.65"
    port = 12345
    g = GUI(ip_address, port)
