sum=0
def factorial(x):
    if x<=1:
        return 1
    else: return x*factorial(x-1)


abs= lambda x, i: x**(2*i) / factorial(2*i)

def exp_x(x,n):
    global sum

    i=0
    while i<n:
        sum+= ((-1)**n) * abs(x,n)
        i+=1




toplam =0;
def commonrat(r, n):
    """ This function returns the sum from nth power of r to the 0th power of r by declining the n by 1 and since all the termss are positive they are all added directly"""
    global toplam
    if n==0:
        toplam+= 1
    else :
        toplam+= r**n
        commonrat(r,n-1)

