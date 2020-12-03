def multiply(*args):
    total = 1
    for arg in args:
        total*=arg
        print(total)


multiply(1,2,3)