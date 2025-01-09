#tipos de dato: string, int, dimbolos % significa resto y no percenmt

#Ask for name
print ("Hello World")
name = input("w your name").strip().title()
name= name.strip() #remueve los white spaces que pueda poner en elinpuy ( hay muchas funciones aplicables a los inpuit)
#name= name.capitalize() # colo hace  amyuscula la primera letra
#name= name.title()  #capitaliza todas las primeras eltras de las palabras

name.split(" ")# divide entre el primer norme yel segundo tomandoc omo medio el " " espacio
#name= name.strip().title() 
print ("hi,", name, "como estas")
print(f"hello {name}")