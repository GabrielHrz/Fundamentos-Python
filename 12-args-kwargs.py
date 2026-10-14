def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return 0


print(big_function(1,2,3,4,5,6,7,8,num1=77,num2=100))