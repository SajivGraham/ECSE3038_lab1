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
