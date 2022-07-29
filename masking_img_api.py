
from PIL import Image

import math
from PIL import Image, ImageDraw

from pdf2image import convert_from_path


import img2pdf
from PIL import Image
import os

from data_encryption_images import encryptimg
from data_encryption_pdf import encryptpdf

def image_masking_api(file_path1):



						im = Image.open(file_path1)

						# Size of the image in pixels (size of original image)
						# (This is not mandatory)
						#width, height = im.size
						#print(width, height)


						# In[ ]:





						# In[17]:


						newsize = (2500,2500)
						im1 = im.resize(newsize)
						# Shows the image in image viewer
						#im1.show()


						# In[18]:


						im1.save("resized_image_medical.png")

						im2=im1


						# In[19]:


						# importing image object from PIL
						
						  
						#w, h = 1780, 775

						#1074,1769,640,1709
						shape = [(1877,329),(2180,576)]
						  
						# creating new Image object
						img =im2
						  
						# create rectangle image
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")
						#img.show()1450,1833,1016,1773,,,,,932,1369,498,1309
						shape = [(777,757),(2193,830)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")
						shape = [(775,832),(2191,905)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")

						shape = [(775,892),(2191,965)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")

						shape = [(777,958),(2193,1031)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")

						shape = [(781,1029),(2197,1102)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")



						shape = [(774,1099),(2190,1172)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")

						im1.save("masked_image.png")



						encryptimg("masked_image.png") 

						











						print("this code is working")

def image_masking_api_pdf(file_path2):
						print("operation on pdf is started")


						pages = convert_from_path(file_path2,500)

						i=0

						for page in pages:
						    page.save('img_convertedpdf.png', 'PNG')
						    


						# In[16]:


						# Importing Image class from PIL module
						from PIL import Image

						im = Image.open(r"img_convertedpdf.png")

						# Size of the image in pixels (size of original image)
						# (This is not mandatory)
						width, height = im.size
						print(width, height)


						# In[ ]:





						# In[17]:


						newsize = (2500,2500)
						im1 = im.resize(newsize)

						#newsize = (2500,2500)
						#im1 = im.resize(newsize)
						# Shows the image in image viewer
						#im1.show()


						# In[18]:


						im1.save("resized_image_medicalpdf.png")

						im2=im1


						# In[19]:


						# importing image object from PIL
						
						  
						#w, h = 1780, 775

						#1074,1769,640,1709
						shape = [(696,888),(2215,976)]
						  
						# creating new Image object
						img =im2
						  
						# create rectangle image696,888,2215,976,,,,,,657,995,2176,1083,,,,,,,,1928,771,2239,864
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")
						#img.show()1450,1833,1016,1773,,,,,932,1369,498,1309
						shape = [(657,995),(2176,1083)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")
						shape = [(1928,771),(2239,864)]
						img1 = ImageDraw.Draw(img)  
						img1.rectangle(shape, fill ="#ffff33", outline ="red")


						im1.save("masked_pdf_document.png")


						# storing image path
						#img_path = "resized_image_medical.png"
						  
						# storing pdf path
						pdf_path = "masked_pdf_documents.pdf"

						imagepdf = Image.open("masked_pdf_document.png")
						  
						# converting into chunks using img2pdf
						pdf_bytes = img2pdf.convert(imagepdf.filename)
						  
						# opening or creating pdf file
						file = open(pdf_path, "wb")
						  
						# writing pdf files with chunks
						file.write(pdf_bytes)
						  
						# closing image file
						#imagepdf.close()
						  
						# closing pdf file
						#file.close()
						  
						# output
						print("Successfully made pdf file")

						encryptpdf("masked_pdf_documents.pdf")

						










						print("this code is working")
