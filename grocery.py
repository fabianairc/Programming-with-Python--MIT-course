from collections import Counter

def grocery():
    
    contador= Counter()
    
    while True:
        Item=input().strip().lower()
        if Item== "":
            break
        contador[Item] += 1

    palabras_ordenadas=sorted(contador.items())
    
    
    for item, count in palabras_ordenadas:
        print (f"{count} {item.upper()}") 
    
    
grocery()