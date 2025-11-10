#defualt argument 
def greet(name,msg="welecome bhai",**loc):
    print(name,msg)
    print(**loc)
    
    for k,v in loc.items():
        print(k,":",v)

greet(name = "vignesh",msg ="Good morning",loc ="hyd")
    

    