try:
    a = int(input("enter the number"))
    print(a)
except Exception as e:
    print(e)



finally:
    print(" i am a inside finally:")          