def function(*args):
    print(type(args))
    for item in args:
        print(item)
lst=["shree","roy","sam"]
function(*lst)