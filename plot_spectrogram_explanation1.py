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
#ax1.set_ylabel(r'Strain $\times (D/$kpc)')
ax1.set_xlabel(r'time')
#ax1.set_title(r'GW strain at 1 kpc',size=13)
ax1.set_xlim(-0.02e3,0.1e3)
ax1.set_ylim(-3,3.2)
#ax1.plot(t[r]*1e3,gwc[r]*4.01651423e-72*10*1e20) #plot signal
ax1.plot(t[r]*1e3,exp(-(t[r]*1e3-40)**2./(2.*5.**2)),'k') #plot window
ax1.plot(t[r]*1e3,gwc[r]*4.01651423e-72*10*1e20*exp(-(t[r]*1e3-40)**2./(2.*5.**2))) #plot windowed signal

ax2.contourf((gwspect[r][gwprebouncet[r]:])*1e3,gwspecf[r][gw_lf_lim[r]:gw_uf_lim[r]],log10(gwspec[r][gw_lf_lim[r]:gw_uf_lim[r],gwprebouncet[r]:]),levels=gwLevels,cmap=Cmap)
ax2.set_xlabel(r'time')
ax2.set_ylabel(r'frequency')
ax2.plot([39,39],[50,1250],'k')
ax2.plot([41,41],[50,1250],'k')

ax2.set_ylim(57.146514519790777,1250)

