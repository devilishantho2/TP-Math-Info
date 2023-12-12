##TP INFO 3

def f(x):
    return 2*(x[0]**2)+(x[1]**2)-x[0]*x[1]-3*x[0]-x[1]+4

def df(x):
    return (4*x[0]-x[1]-3,2*x[1]-x[0]-1)

Hf = [[4,-1],[-1,2]]

i = int(input("Combien d'itérations? : "))

##GPF
x0 = (0,0)
alpha = 0.5

for k in range(i):
    ndf = df(x0)
    w = (-ndf[0],-ndf[1])
    x0 = (x0[0]+alpha*w[0],x0[1]+alpha*w[1])
    
    
print(f(x0))

##GPO
x0 = (0,0)

for k in range(i):
    ndf = df(x0)
    w = (-ndf[0],-ndf[1])
    a = 4*(w[0]**2)+2*(w[1]**2)-2*w[1]*w[0]
    b = 4*x0[0]*w[0]-x0[1]*w[0]-3*w[0]+2*x0[1]*w[1]-x0[0]*w[1]-w[1]
    alpha = -b/a
    x0 = (x0[0]+alpha*w[0],x0[1]+alpha*w[1])
    
print(f(x0))

