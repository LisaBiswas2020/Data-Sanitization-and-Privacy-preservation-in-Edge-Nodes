import json
import requests
headers = {"Authorization": "Bearer ya29.A0AVA9y1uUMadpxB5DOZTCiqEryAoslYmzOmJ3-gGrve0gTdma0cJTSdaTtnL0r_GCQDf4unnGzM7Y0FAPqp82w7tT5cJWD_FMH2603F6U9Vs37ZqSX807iSEf_EKTGx1vi2Vm3bGYPPm_zWPpeKcEj7O1LnavYUNnWUtBVEFTQVRBU0ZRRl91NjFWTXhZM2VrSGV6NnBBM25TOTlPeG5qZw0163"}



def data_to_drive(input_file, out_file):


					para = {
					    "name": out_file}
					files = {
					    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
					    'file': open( input_file, "rb")
					}
					r = requests.post(
					    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
					    headers=headers,
					    files=files
					)
					print(r.text)
data_to_drive('client_encrypted_image.encdecrypted_image.png', "client_encrypted_image.encdecrypted_image.png")