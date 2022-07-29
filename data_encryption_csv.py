
from Crypto.Cipher import AES




def enc_image(input_data,key,iv,filepath):
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    enc_file = open(filepath+"encrypted_csv.enc", "wb")
    enc_file.write(enc_data)
    enc_file.close()

    
def dec_image(input_data,key,iv,filepath):
    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(input_data)

    output_file = open(filepath+"decrypted_csv.csv", "wb")
    output_file.write(plain_data)
    output_file.close()


# In[31]:



from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import *
import tkinter.messagebox
from PIL import Image,ImageTk
import hashlib
#import enc_script

def encryptcsv(image_path):

        enc_pass = "12345"

        enc_aes_key_fn(enc_pass)








        #LOAD THE IMAGE
        filename =image_path

        #GENERATE KEY & INITIALIZATION VECTOR
        hash=hashlib.sha256(enc_pass.encode()) 
        p = hash.digest()
        key = p
        iv = p.ljust(16)[:16]
        print("Encoding key is: ",key)

        input_file = open(filename,'rb')
        input_data = input_file.read()
        input_file.close()
        enc_image(input_data,key,iv,"")

       # tkinter.messagebox.showinfo("Encryption Alert","Encryption ended successfully. File stored as: encrypted.enc")

def decryptcsv(aes_key):
    
        enc_pass = aes_key

        filename ="client_encrypted_csv.enc"

        hash=hashlib.sha256(enc_pass.encode()) 
        p = hash.digest()
        key = p
       # print(key)
        iv = p.ljust(16)[:16]
        input_file = open(filename,'rb')
        input_data = input_file.read()
        input_file.close()
        dec_image(input_data,key,iv,filename)
        #tkinter.messagebox.showinfo("Decryption Alert","Decryption ended successfully File Stored as: output.pdf")




import rsa




#def saveKeys(em):
    #(publicKey, privateKey) = rsa.newkeys(1024)
#    with open('encrypted_aeskey.pem', 'wb') as p:
#        p.write(em.save_pkcs1('PEM'))
#    with open('keys/privateKey.pem', 'wb') as p:
#        p.write(privateKey.save_pkcs1('PEM'))




def loadKeys():
    with open('publcKey.pem', 'rb') as p:
        publicKeyl = rsa.PublicKey.load_pkcs1(p.read())
#    with open('keys/privateKey.pem', 'rb') as p:
#        privateKeyl = rsa.PrivateKey.load_pkcs1(p.read())
    return publicKeyl




def enc_aes_key_fn(aes_key):

                aes_key_public=aes_key


                # In[76]:


                em=rsa.encrypt(aes_key_public.encode(),loadKeys())


                print("encrypted key for the aes key ",em)


                #em=str(em)



                import pickle #credits to stack overflow user= blender

#a = {'hello': 'world'}

                with open('encrpted_aes_key.pkl', 'wb') as handle:
                    pickle.dump(em, handle, protocol=pickle.HIGHEST_PROTOCOL)

#with open('filename.pkl', 'rb') as handle:
#    b = pickle.load(handle)
#print (em == b)


                #saveKeys(str(em))

def decc_aes_key(enc_aes_key):

              #  enc_aes_key

                with open('privateKey.pem', 'rb') as p:
                    privateKeyl = rsa.PrivateKey.load_pkcs1(p.read())
                #return privateKeyl, publicKeyl


                dmaes=rsa.decrypt(enc_aes_key,privateKeyl).decode()


                print("the aes key is",dmaes)



                return dmaes



                # In[76]:





                #saveKeys(str(em))













