
try:
    for i in range(5):
        if i == 3:
            raise TypeError
        else:
            print(i)
except :
    print(str(i) + "errpr")