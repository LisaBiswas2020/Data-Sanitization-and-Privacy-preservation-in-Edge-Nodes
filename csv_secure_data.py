

import pandas as pd

from data_encryption_csv  import  encryptcsv

def csv_secured_data_api(file_path3):

			df = pd.DataFrame(pd.read_csv(file_path3,encoding="ISO-8859-1"))


			df=df.dropna()



			data2=df.copy()


			dist=(data2['Address'])
			distset=set(dist)
			dd=list(distset)
			d1="#####"
			dictOfWords = { dd[i] : d1 for i in range(0, len(dd) ) }
			data2['Address']=data2['Address'].map(dictOfWords)


			dist=(data2['Adhaar card number'])
			distset=set(dist)
			dd=list(distset)
			d1="*****"
			dictOfWords = { dd[i] : d1 for i in range(0, len(dd) ) }
			data2['Adhaar card number']=data2['Adhaar card number'].map(dictOfWords)


			data2.to_csv("masked_data.csv")


			encryptcsv("masked_data.csv")