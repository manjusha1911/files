# f = open("demofile.txt", "r")
# print(f.read())



# f = open("demofile.txt", "w")
# f.write("Hello! Welcome to demofile.txtThis file is for testing purposes.Good Luck!")
# f.close( )


# f=open("demofile.txt","r")
# print(f.readline())



import os
if os.path.exists("people2.txt"):
  os.remove("people2.txt9i")
else:
  print("The file does not exist")