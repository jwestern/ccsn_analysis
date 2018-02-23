from numpy import *
from matplotlib import *

rcParams['axes.labelsize']=13.0

fig1=plt.figure()
fig1.subplots_adjust(bottom=0.2)
fig1.subplots_adjust(hspace=.6)

ax1=fig1.add_subplot(121)
ax2=fig1.add_subplot(122)

ax1.grid()

r='2.0_M1c'

#ax1.set_ylabel('Cross spectral densities')
ax1.set_ylabel(r'Strain')
ax1.set_xlabel(r'$t-t_{bounce}$ (ms)')
ax1.set_title(r'GW strain at 1 kpc',size=13)
ax1.set_xlim(-0.02e3,0.1e3)
ax1.set_ylim(-3e-20,3.2e-20)
ax1.plot(t[r]*1e3,gwc[r]*1.23936679e-49/3.086e21) #Note strain*1.23936679e-49 has units of cm, and doesn't depend on distance. Divide this result by [D]=cm to get the strain at distance D from the source.
						  #3.086e21 is 1 kpc in units of cm.

ax2.grid()
ax2.set_ylabel('(erg/s)')
ax2.set_xlabel(r'$t-t_{bounce}$ (ms)')
ax2.set_title(r'$\nu$ luminosities',size=13)
ax2.set_xlim(-0.035e3,0.1e3)
ax2.set_ylim(0.,115e51)
ax2.plot(t[r]*1e3,anuec[r],label=r'$\bar{\nu}_e$')
ax2.plot(t[r]*1e3, nuxc[r],label=r'$\nu_x$')
ax2.plot(t[r]*1e3, nuec[r]/5.,label=r'$\nu_e/5$')
ax2.legend(loc=2)

