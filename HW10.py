import math as m
 
def f(h):
return (m.pi*h**2*(9-h))/3 - 30
 
def df(h):
return m.pi*h*(6-h)
 
def g(h):
return m.sqrt(90/(m.pi*(9-h)))
 
def gp(h):
return 0.5*m.sqrt(90/m.pi)*(9-h)**(-1.5)
 
def Bisection(f, bracket, tol):
xL, xU = bracket
while abs(xU-xL) > tol:
xR = (xL+xU)/2
if f(xL)*f(xR) < 0:
xU = xR
else:
xL = xR
return (xL+xU)/2
 
def FalsePosition(f, bracket, tol):
xL, xU = bracket
while True:
xR = xU - f(xU)*(xL-xU)/(f(xL)-f(xU))
if abs(f(xR)) < tol:
return xR
if f(xL)*f(xR) < 0:
xU = xR
else:
xL = xR
 
def FixedPoint(g, x_guess, tol):
err = tol + 1
while err > tol:
x_new = g(x_guess)
err = abs(x_new - x_guess)
x_guess = x_new
return x_guess
 
def NewtonRaphson(f, df, x_guess, tol):
err = tol + 1
while err > tol:
x_new = x_guess - f(x_guess)/df(x_guess)
err = abs(x_new - x_guess)
x_guess = x_new
return x_guess
 
xL, xU = 0, 6
 
for i in range(3):
xR = (xL+xU)/2
print("Bisection Iter", i+1, "=", xR)
if f(xL)*f(xR) < 0:
xU = xR
else:
xL = xR
 
print("Bisection =", Bisection(f, (0,6), 0.01))
print("False Position =", FalsePosition(f, (0,6), 0.01))
print("|g'(2)| =", abs(gp(2)))
print("Fixed Point =", FixedPoint(g, 2, 0.01))
print("Newton-Raphson =", NewtonRaphson(f, df, 2, 0.01))