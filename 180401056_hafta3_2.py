from sympy import Symbol,sqrt,pi,Integral,exp

x = Symbol('x')

p = exp(-(x-10)**2/2)/sqrt(2*pi)

print(Integral(p,(x,11,12)).doit().evalf())