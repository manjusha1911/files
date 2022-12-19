# f1=open("mlines.txt","w")
# lines=["welcome\n","python\n","progamming\n"]
# f1.writelines(lines)
# f1=open("mlines.txt","r")
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1.close()

# def factorial(n):
#     if n==0 or n==1:
#         return 0 or 1
#     else:
#         return n*factorial(n-1)
# n=int(input("enter the number:"))
# result=factorial(n)
# print(result)


import os
if os.path .exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("not exist")