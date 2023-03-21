
def squareRoot(a, n):
    x0 = a
    for i in range(n):
        xN = ((a/x0)+x0)/2
        x0 = xN
    return x0
def piApprox(n):
    AB = 1; CA = 1; base0 = 1
    v0 = squareRoot(AB**2-((base0/2)**2), 100)
    pi0 = 6*base0*(v0/2)
    base = 0; v = 0 #else error "Variable referenced before assignment"
    for i in range(n):
        base = squareRoot((base0/2)**2+(1-v0)**2, 100)
        v = squareRoot(1 - (base/2)**2, 100)
        base0 = base
        v0 = v
    r = 6*(2**n)*base*(v/2)
    return r
def piApprox2(n):
    #a1 je aktualni a
    a1 = (1/2)*(1/8)
    s = (1/3)*a1 #s1
    for i in range(2, n):
        a = a1*((2*i-3)/(2*i))*(1/4)
        a1=a
        s = s + (1/(2*i+1))*a1 #sn
        #print(s)
    return (12*(-((squareRoot(3,1000))/8)+(1/2)-s))

