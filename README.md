This script is used to communicate between the edge nodes and server and transfer file using masking and encrypted channel. 

#set up 
Open a gmail account and in https://developers.google.com/oauthplayground/ authenticate the drive upload the files.

![image](https://user-images.githubusercontent.com/71204623/182034276-5313b93e-90b2-49ff-9fdb-15693ec8bcdb.png)

Once authentication token is recieved add the code to drive_store.py file,  now we will be able to upload the files in drive location.
From base machine run the erver.py file using Anaconda promt and from your VM run client_GUI.py file.
Now the the comminucation will be setup with the base machine and client machine. Here we are assuming that base machine is your server and VM machine is our edge node.

![image](https://user-images.githubusercontent.com/71204623/182034499-ba8d7c85-2cb8-4aa8-b0c8-6ebd4bf423e8.png)

We can send our file from edge nodes to server during upload it will be encrypted and masked.Once it reaches the destination location meesage will appear the fle transfer is complete. And later we check the drive to the uploaded file.

![image](https://user-images.githubusercontent.com/71204623/182034571-219c2492-c002-4078-b967-0145bf65b6f9.png)
![image](https://user-images.githubusercontent.com/71204623/182034619-6a3e3653-0b10-4c17-995f-99017f5bfef6.png)
