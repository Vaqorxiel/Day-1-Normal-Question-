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
      #try,except,while true is so OP!!
