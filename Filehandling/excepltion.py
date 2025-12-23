print("program started")
try:
    a=10
    b=a/0
    print(b)
except Exception as e:
    print(e)
else:
    print("something")

print("program ended")

