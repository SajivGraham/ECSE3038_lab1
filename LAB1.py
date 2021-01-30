def hello():
    print("ECSE3038 - Engineering IoT Systems")

def validatePassword(password):
    x=password
    y= len(x)
    z=0
    if y >= 8 and x.isalnum():
        for val in x:
            try:
                if isinstance(int(val), int):
                    z = z+1
            except:
                pass
        if z >=2 :
            return True
    return False

def sumUpToN(integer):
    number2 = 0
    intcheck = isinstance(integer, int)
    if intcheck == True and integer > 1:
            for i in range(1,integer+1):
                number2 = number2 + i
    else:
            number2 = -1
    return number2

print("\n")

hello()

print("\n")

print(validatePassword("testtest12"))

print("\n")

print(sumUpToN(2))

print("\n")


