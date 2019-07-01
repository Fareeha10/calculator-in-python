def add(n1,n2): #function to calculate for addition
    addi=n1+n2
    print(add)
def subi(n1,n2): #function to calculate for subraction
    suba=n1-n2
    print(suba)
def div(n1,n2):  #function to calculate for multiplication
    divi=n1/n2
    print(divi)
def mul(n1,n2):  #function to calculate for division
    mulu=n1*n2
    print(mulu)
a=int(input("Enter 1st value:")) #Asking for 1st input
b=int(input("Enter 2nd value:" ))  #Asking for 2nd input
c=int(input("Select operation 1.add 2.sub 3.mul 4.div: 5.Quit:")) #options
if c==1:
    add(a,b)
elif c==2:
    subi(a,b)
elif c==3:
    mul(a,b)
elif c==4:
    div(a,b)
elif c==5:
    exit()
    
