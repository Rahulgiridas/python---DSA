def add(a,b):
    print(a+b)
def sub(m,n):
    if m==0:
        print("Error : Zero Division Error")
    else:
        print(m/n)

def add_n(*a):
    print(sum(a))

def mul_n(*b):
    res=1
    for i in b:
        res*=i
    print(res)
