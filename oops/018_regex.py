import re


# st= "Sun rises Sun in in east"

# # k=re.match("Sun",st)
# k=re.search("Sun",st)
# # k=re.findall("in",st)
# print(k)

# st="topss1"
# k=re.search("^[a-z0-9]{5,10}$",st)
# print(k)


# st=re.findall(r"abc\B","abclhkjl sks dsb")
# print(st)

#alphabets only
# username=(input("enter a username"))
# k=re.match("^[a-zA-Z]+$",username)
# print(k)
# if k is None:
#     print("invalid format")
# else:
#     print(username)


# numbers only
# phone=input("enter a number")
# k=re.match("^[0-9]{10}+$",phone)
# print(k)
# if k is None:
#     print("invalid format")
# else:
#     print(phone)

# email parth@gmai.com
# email=input("enter a email")
# k=re.match("^[a-zA-z0-9_-]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$",email)
# print(k)
# if k is None:
#     print("invalid format")
# else:
#     print(email)


#passwords
password = input("Enter password: ")

k=re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W]).{8,}$",password )
print(k)

if k is None:
    print("invalid format")
else:
    print(password)
