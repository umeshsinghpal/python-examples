def function(**kwargs):
    for key,value in kwargs.items():
      print(key,value)
dict={"Hi":"sourav","Hello":"vibhu","welcome":"vaibhav"}
function(**dict)
