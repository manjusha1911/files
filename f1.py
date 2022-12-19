f1=open("hello.txt","w")
f1.write("welcome to python files")
f1.close
f1=open("hello.txt","r")
print(f1.read(5))
print(f1.read(4))
print(f1.read(3))
print(f1.read())
