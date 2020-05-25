
import math as m

def f(x):
    return m.pow(x,2)

n = 1000 # Antall trapeser
xstart = 0 # Startverdi for trapesmetoden
xstop = 10 # Stopp verdi for trapesmetoden

dx = (xstop - xstart)/n # Delta x
x = dx # Setter verdien av x lik x1

y = (f(xstop) + f(xstart)/2) # Leggersammen det første og siste trapeset

for i in range(xstart,n-1): # For loop som går gjennom og legger sammen alle trapesene
    y += f(x)
    x +=dx # Øker x med verdien av dx for å få neste x-verdi

y = dx * y

print("Utført arbeid beregnet ved trapenmetoden er: ",round(y,3),"J")