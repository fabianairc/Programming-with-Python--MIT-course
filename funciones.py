def main(): 
    name = input("w your name? ")
    hello(name)


def hello(to="world"):
    print("hello", to)
    
main()

#las funciones not ienenhosting, tienen que estar definidas arriba del llamado, a menos que defina todo dentro de main, que es buen a rpactica
#tener en cuenta el scope, las ariables solo estan dentro de la funcion donde se definieron