from numpy import *
from matplotlib import *

execfile('./pars_alt.py')
#execfile('./compute_spectrograms2.py')

rhospecf   = pickle.load(open( 'rhospecf.dic','rb'))
Rpnsspecf  = pickle.load(open('Rpnsspecf.dic','rb'))
Tpnsspecf  = pickle.load(open('Tpnsspecf.dic','rb'))

rhospect   = pickle.load(open( 'rhospect.dic','rb'))
Rpnsspect  = pickle.load(open('Rpnsspect.dic','rb'))
Tpnsspect  = pickle.load(open('Tpnsspect.dic','rb'))

rhospec    = pickle.load(open( 'rhospec.dic','rb'))
Rpnsspec   = pickle.load(open('Rpnsspec.dic','rb'))
Tpnsspec   = pickle.load(open('Tpnsspec.dic','rb'))

#share_colorscale_nu = 'yes'

numcols  = len(rotrates)
numrows  = len(sigtypes)
numplots = numcols*numrows

rcParams['axes.labelsize']=13.0

fig1=plt.figure()
fig1.subplots_adjust(bottom=0.15)
fig1.subplots_adjust(hspace=.25)
fig1.subplots_adjust(left=0.15)

ax = {}
for nc in range(1,numcols+1):
	ax[nc]={}
	for nr in range(1,numrows+1):
		ax[nc][nr] = fig1.add_subplot(numrows,numcols,(nr-1)*numcols                                              +nc)
#						              ^^^ how many times to add a whole row (start with 0 times)   ^the column in the given row

Cmap='jet'

upper_freq_limit = 1e3 #in Hz... Largest frequency to plot in the spectrograms

#Get array coordinate for lower and upper limits of frequency that are to be plotted

rho_lf_lim   = {}
rho_uf_lim   = {}
Rpns_lf_lim = {}
Rpns_uf_lim = {}
Tpns_lf_lim  = {}
Tpns_uf_lim  = {}

for r in rotrates:
	rho_lf_lim[r]   = 2
	rho_uf_lim[r]   = amin(  where(rhospecf[r]>upper_freq_limit))+1
	Rpns_lf_lim[r]  = 2
	Rpns_uf_lim[r]  = amin( where(Rpnsspecf[r]>upper_freq_limit))+1
	Tpns_lf_lim[r]  = 2
	Tpns_uf_lim[r]  = amin( where(Tpnsspecf[r]>upper_freq_limit))+1

#Get array coordinate of the bounce time
rhobouncet   = {}
Rpnsbouncet  = {}
Tpnsbouncet  = {}

for r in rotrates:
	rhobouncet[r]   = abs(  rhospect[r]).argmin()
	Rpnsbouncet[r]  = abs( Rpnsspect[r]).argmin()
	Tpnsbouncet[r]  = abs( Tpnsspect[r]).argmin()

#Get array coordinate of fraction of a window prior to bounce time
rhoprebouncet   = {}
Rpnsprebouncet = {}
Tpnsprebouncet  = {}
thatfraction = 0.4
for r in rotrates:
	rhoprebouncet[r]   = abs( rhospect[r]+thatfraction*WindowWidth*1e-3).argmin()
	Rpnsprebouncet[r]  = abs(Rpnsspect[r]+thatfraction*WindowWidth*1e-3).argmin()
	Tpnsprebouncet[r]  = abs(Tpnsspect[r]+thatfraction*WindowWidth*1e-3).argmin()

#Get max and min values of the spectrograms across all rotation cases, but separately for different data, so that
#the plots will have a shared color scale across rotation cases and can be compared by eye.
rhomins   = []
Rpnsmins  = []
Tpnsmins  = []

rhomaxs   = []
Rpnsmaxs  = []
Tpnsmaxs  = []

for r in rotrates:
	rhomins.append(   rhospec[r][  rho_lf_lim[r]: rho_uf_lim[r],  rhoprebouncet[r]: ].min() )
	Rpnsmins.append( Rpnsspec[r][ Rpns_lf_lim[r]:Rpns_uf_lim[r], Rpnsprebouncet[r]: ].min() )
	Tpnsmins.append( Tpnsspec[r][ Tpns_lf_lim[r]:Tpns_uf_lim[r], Tpnsprebouncet[r]: ].min() )
	rhomaxs.append(   rhospec[r][  rho_lf_lim[r]: rho_uf_lim[r],  rhoprebouncet[r]: ].max() )
	Rpnsmaxs.append( Rpnsspec[r][ Rpns_lf_lim[r]:Rpns_uf_lim[r], Rpnsprebouncet[r]: ].max() )
	Tpnsmaxs.append( Tpnsspec[r][ Tpns_lf_lim[r]:Tpns_uf_lim[r], Tpnsprebouncet[r]: ].max() )

rho_level_min   = amin(  rhomins ) 
Rpns_level_min  = amin( Rpnsmins )
Tpns_level_min  = amin( Tpnsmins )

rho_level_max   = amax(  rhomaxs ) 
Rpns_level_max  = amax( Rpnsmaxs )
Tpns_level_max  = amax( Tpnsmaxs )

#Create the colorscales now
rhoLevels   = MaxNLocator(nbins=100).tick_values(log10(  rho_level_min), log10(  rho_level_max))

#if share_colorscale_nu=='yes':
#	anueLevels = MaxNLocator(nbins=100).tick_values(log10( amin([anue_level_min,nux_level_min,nue_level_min]) ), log10( amax([anue_level_max,nux_level_max,nue_level_max]) ))
#	nuxLevels  = anueLevels
#	nueLevels  = anueLevels
#else:
RpnsLevels = MaxNLocator(nbins=100).tick_values(log10(Rpns_level_min), log10(Rpns_level_max))
TpnsLevels = MaxNLocator(nbins=100).tick_values(log10(Tpns_level_min), log10(Tpns_level_max))

#Now make plots
for nr in range(1,numrows+1):
	for nc in range(1,numcols+1):
		r = rotrates[nc-1]
		sig = sigtypes[nr-1]
		Title = titles[nr-1]+r': $\omega_{initial} = $'+r+' (rad/s)'
		ax[nc][nr].grid()
		if sig=='rhoc':
			ax[nc][nr].contourf((rhospect[r][rhoprebouncet[r]:])*1e3,rhospecf[r][rho_lf_lim[r]:rho_uf_lim[r]],log10(rhospec[r][rho_lf_lim[r]:rho_uf_lim[r],rhoprebouncet[r]:]),levels=rhoLevels,cmap=Cmap)
		elif sig=='pnsrad':
			ax[nc][nr].contourf((Rpnsspect[r][Rpnsprebouncet[r]:])*1e3,Rpnsspecf[r][Rpns_lf_lim[r]:Rpns_uf_lim[r]],log10(Rpnsspec[r][Rpns_lf_lim[r]:Rpns_uf_lim[r],Rpnsprebouncet[r]:]),levels=RpnsLevels,cmap=Cmap)
		elif sig=='Mns':
			ax[nc][nr].contourf((Tpnsspect[r][Tpnsprebouncet[r]:])*1e3,Tpnsspecf[r][Tpns_lf_lim[r]:Tpns_uf_lim[r]],log10(Tpnsspec[r][Tpns_lf_lim[r]:Tpns_uf_lim[r],Tpnsprebouncet[r]:]),levels=TpnsLevels,cmap=Cmap)
		ax[nc][nr].set_title(r'')
		if mod(nc-1,numcols)==0:
			ax[nc][nr].set_ylabel(r'$f$ (Hz)')
		if nr==numrows:
			ax[nc][nr].set_xlabel(r'$t-t_\mathrm{bounce}$ (ms)')
		ax[nc][nr].set_title(Title,size=13)

