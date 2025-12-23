def test():
    try:
        a=int(input("enter a number :"))
        print(a)
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("allways exutable")
k=test()
print(k)