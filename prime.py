def prime():
    p = int(input("enter number:"))
    i = 2
    for i in range(2, p):
        if p % i == 0:
            print(p,"is not a prime number:")
            exit(0)
        else:
            i = i + 1
    print(p,"is a prime number:")






        

prime()






    
        
