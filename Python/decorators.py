def decor(function):
    def inner(name):
        if name=="ayush":
            print("ayush like palav")
        else:
            function(name)
    return inner
@decor
def food(name):
    print(name,"likes biryani")
food("ayush")

def smartdeco(function):
    def inner(a,b):
        if b==0:
            print("b cant be o")
        else:
            function(a,b)
    return inner
@smartdeco
def div(a,b):
    print(a//b)
div(2,0)
div(10,5)

    
        
