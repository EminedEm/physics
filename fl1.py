import numpy as np
import matplotlib.pyplot as plt
import math

m=32
pi=math.pi
g=9.8
def fp(alphat,thethat,mut):
    ft= (mut*m*g*math.cos(alphat)+m*g*math.sin(alphat))/(math.cos(thethat)-mut*math.sin(thethat))
    return ft
alpha=math.radians(24)
thetha=math.radians(24)
mu=0.5
print(fp(alpha,thetha,mu))

#if i change the thetha which is te angle of force pf
#thetha is 90 its not gonna move
thethavalues=np.linspace(0,pi/2,100)
fpvalues=[fp(alpha, thetha,mu) for thetha in thethavalues]
plt.figure(figsize=(20, 11))
plt.plot(thethavalues, fpvalues, color='blue', label='fp vs thetha')
plt.title('block on incline')
plt.xlabel('thetha (radians)')
plt.ylabel('fp (N)')
plt.legend()
plt.grid(True)
plt.show()
