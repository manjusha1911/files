f1=open("mlines.txt","w")
lines=["welcome\n","python\n","progamming\n"]
f1.writelines(lines)
f1=open("mlines.txt","r")
print(f1.readlines())
f1.close()