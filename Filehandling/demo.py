# f=open("text.txt",'w')
# f.write("everything")
# f.close()


# w(file write) and a(file append)
# f=open("text.txt",'w')
# l=["python\n","java\n","php\n","android\n"]
# f.writelines(l)
# f.close()

# f=open("text.txt",'a')
# f.write("something..")
# f.close

# f=open("text.txt",'r')
# data=f.read()
# print(data)

# f=open("text.txt",'r')
# while True:
#     data=f.readline()
#     print(data)
#     if not data:
#         break
# f.close()

# f=open("text.txt",'r')
# data=f.readlines()
# print(data)
# f.close()

# f=open("text.txt",'r')
# data=f.read
# if not data:
#     print("file empty")
# f.close()

# f=open("text.txt",'r')
# while True:
#     data=f.readline()
#     if 'a' in data:
#         print(data)
#     if not data:
#         break
# f.close()


# f=open("text.txt",'r')
# data=f.readlines()
# print(data)
# f.close()

#r+,w+ 


import pickle

st={
    "name":"parth",
    "email":"parth@gmail",
    "phone":"7622893779"

}

#pickling
with open("obj.pkl",'wb') as f:
    pickle.dump(st,f)
    print("success")

#unpickling
with open("obj.pkl",'rb')as f:
    data=pickle.load(f)
    print(data)