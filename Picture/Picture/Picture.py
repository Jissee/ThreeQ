import matplotlib.pyplot as plot
import math
import numpy as nm
PI=3.1415926535897932384626433832795028841971693993751058209749445923
c=299792458
h=6.62607015e-34
E=2.71828
k=1.3806505e-23
def plank(w,T):
    aa=2*PI*c*c*h
    bb=(w*1e-9)**5
    cc=h*c/(w*(1e-9)*k*T)
    dd=E**cc-1
    return (aa/bb)*(1/(E**cc-1))/10**13

fig=plot.figure()
ax=fig.add_subplot()
ax.set_facecolor("#FFEBC6")

ax.text(1500, 8, r"$ S(\lambda) = \frac{2 \pi c^2 h}{ \lambda ^5} · \frac{1}{e^\frac{hc}{ \lambda kT} -1} $",fontsize=20)

plot.xlabel("Wavelength(nm)")
plot.ylabel("Power density (10¹³ watts/m³)")
plot.xlim(100,3000)
plot.ylim(0,11)
x=nm.linspace(100,3000,10000)
x0=nm.linspace(100,400,10000)
x1=nm.linspace(400,445,10000)
x2=nm.linspace(445,490,10000)
x3=nm.linspace(490,535,10000)
x4=nm.linspace(535,580,10000)
x5=nm.linspace(580,625,10000)
x6=nm.linspace(625,670,10000)
x7=nm.linspace(670,725,10000)
x8=nm.linspace(725,760,10000)
x9=nm.linspace(760,3000,10000)
plot.plot(x0,plank(x0,6000),color="#000000")
plot.plot(x1,plank(x1,6000),color="#000000")
plot.plot(x2,plank(x2,6000),color="#000000")
plot.plot(x3,plank(x3,6000),color="#000000")
plot.plot(x4,plank(x4,6000),color="#000000")
plot.plot(x5,plank(x5,6000),color="#000000")
plot.plot(x6,plank(x6,6000),color="#000000")
plot.plot(x7,plank(x7,6000),color="#000000")
plot.plot(x8,plank(x8,6000),color="#000000")
plot.plot(x9,plank(x9,6000),color="#000000")


plot.plot(x,plank(x,5000),color="#000000",linestyle="--")
plot.plot(x,plank(x,4000),color="#000000",linestyle="--")
plot.plot(x,plank(x,3000),color="#000000",linestyle=":")

plot.fill_between(x1,plank(x1,6000),color="#8B00FF")
plot.fill_between(x2,plank(x2,6000),color="#0000FF")
plot.fill_between(x3,plank(x3,6000),color="#00FFFF")
plot.fill_between(x4,plank(x4,6000),color="#00FF00")
plot.fill_between(x5,plank(x5,6000),color="#FFFF00")
plot.fill_between(x6,plank(x6,6000),color="#FF7F00")
plot.fill_between(x7,plank(x7,6000),color="#FF0000")
plot.fill_between(x8,plank(x8,6000),color="#FF0000")


plot.annotate('6000K',xy=(880,6),xytext=(880,6))
plot.annotate('5000K',xy=(920,3),xytext=(1200,4),arrowprops=dict(facecolor='black',shrink=5,width=1,headwidth=3))
plot.annotate('4000K',xy=(1250,0.9),xytext=(1500,1.8),arrowprops=dict(facecolor='black',shrink=5,width=1,headwidth=3))
plot.annotate('3000K',xy=(1600,0.3),xytext=(1800,1.2),arrowprops=dict(facecolor='black',shrink=5,width=1,headwidth=3))
plot.annotate('Visible',xy=(450,6.5),xytext=(450,6.5))
plot.annotate('Radiated Power Density',xy=(1000,10.5),xytext=(1000,10.5))
plot.annotate('Plank Law',xy=(1250,10),xytext=(1250,10))
plot.annotate('By SYH',xy=(2000,10),xytext=(2000,10))

plot.show()
