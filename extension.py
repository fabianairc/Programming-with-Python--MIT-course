def main():
    
    value=input(" extension ").lower()
    
    def match_case(caso):
        match True:
            case _ if caso.endswith(".jpg") :
                return f"/image/{caso}"
            case _ if caso.endswith(".png"):
                return f"/image/{caso}"
            case _:
                return "wtf"
           
        
    print(match_case(value))   
 
main()