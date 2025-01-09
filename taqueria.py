def price_taqueria():

    menu={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
        
    while True:
        order=input("What you want? ")
        
        if order.lower() == "exit":
            break
        
        if order in menu:
            print(" the price of {} is ${:.2f}".format(order, menu[order]))
        else:
            print("item error")
        
price_taqueria()