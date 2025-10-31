def factorise(n):
    factors=[]
    i=0
    while i<=n:
        i+=1
        if (n/i).is_integer():
            factors.append(i)
    return factors


def is_prime(n):
    if len(factorise(n))==2:
        return(1)
    else:
        return(0)
    
is_prime(4)