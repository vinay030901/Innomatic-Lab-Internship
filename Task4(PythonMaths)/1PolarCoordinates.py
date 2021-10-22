import cmath
import math
j=complex(input())
p=j.imag
q=j.real
sqr=p*p+q*q
print(math.sqrt(sqr))
print(cmath.phase(j))
