def main():
    
    x= int(input("w number "))
    if is_even(x):
        print("even")
    else:
        print("odd")
    
def is_even(n):
    if n%2 ==0:    # bool es true o false          
        return  True
    else: 
        return False
#return True if n % 2 == 0 else False
#return n % 2 == 0  porque sera True directamente si se cumple eso
main()
    
    
    
    
    
    
    
    
    
    