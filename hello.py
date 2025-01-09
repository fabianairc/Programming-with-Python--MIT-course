# print("hello, world")

try: 
    x=int(input("what`s x")) #para hacer input en integer
    print(f" x is {x}")
except ValueError:
    print("not an integer")
    
    #basicamente dice que pruebe hacer esto y caso que de ese error decir lo otro, sirve para handle los errores
    
    #NameError
    
while True:   
    try: 
        x=int(input("what`s x")) 
        
    except ValueError:
        print("not an integer")
        
    else:
        break
    
print(f" x is {x}")
    
    