def multiplication_table(m, n):
    S=""
    for i in range(1,10):
        for j in range(m,n+1):
            S=(S+str(j)+"x"+str(i)+"="+str(i*j)+"\t")
        S=S+"\n"
    print (S)

def pyramid(h):
    for i in range(h):
        print(" "*(h-i)+"*"*(i)*2+"*")
    