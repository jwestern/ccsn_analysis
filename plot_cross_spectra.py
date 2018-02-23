from numpy import *
from matplotlib import *

rcParams['axes.labelsize']=13.0

fig1=plt.figure()
fig1.subplots_adjust(bottom=0.2)
#fig1.subplots_adjust(hspace=.5)

ax1=fig1.add_subplot(121)
ax2=fig1.add_subplot(122)

ax1.grid()

r='2.0_M1c'

#ax1.set_ylabel('Cross spectral densities')
ax1.set_ylabel(r'Strain $\times (D/$kpc)')
ax1.set_xlabel(r'$t-t_{bounce}$ (ms)')
ax1.set_title(r'GW strain at 1 kpc',size=13)
ax1.set_xlim(-0.02e3,0.1e3)
ax1.set_ylim(-6.67e-20,3.2e-20)
ax1.plot(t[r]*1e3,gwc[r]*4.01651423e-72*10)

ax2.grid()
#ax2.set_ylabel('Cross spectral densities')
ax1.set_xlabel(r'$t-t_{bounce}$ (ms)')
ax1.set_title(r'$\nu$ luminosities',size=13)
ax2.set_xlim(-0.02e3,0.1e3)
#ax2.set_ylim(1e87,1e104)
ax2.legend(loc=3)

