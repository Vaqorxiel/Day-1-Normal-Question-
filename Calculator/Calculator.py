while True:
    calc=input("type math or quit:")
    
    if calc=='quit':
        print("calculator off")
        break
        
    try:
        result=eval(calc)
        print("answer:",result)
        
    except:
        print("thats not math Try 5+5 or type quit")
      #try and except and while tru is so OP
