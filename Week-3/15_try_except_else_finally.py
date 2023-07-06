def exceptionhandling():
  try:
    num=10
    num1=20
    num3=10
    division=(num+num1)/num3
    print(division)
  except:
      print("there is a exception")
  else:
      print("there is no problem") 
  finally:
      print("you are in finally block")
exceptionhandling()
