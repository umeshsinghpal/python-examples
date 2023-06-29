def exceptionhandling():
  try:
    a=10
    b=20
    c=10
    d=(a+b)/c
    print(d)
  except:
      print("there is a exception")
  else:
      print("there is no problem") 
  finally:
      print("you are in finally block")
exceptionhandling()