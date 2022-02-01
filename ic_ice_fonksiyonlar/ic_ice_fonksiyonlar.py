import time
import math

def hesapla(func):
    def sure(a):
        bas=time.time()
        func(a)
        bit=time.time()
        x=bit-bas
        print(f"gecen süre={x}")
        
    return sure

@hesapla
def fak(a):
    print("faktoriyel:",math.factorial(a))
    return math.factorial(a)

@hesapla
def karekok(b):
    print("karekok:",math.sqrt(b))
    return math.sqrt(b)

fak(25)
karekok(25)


    
    