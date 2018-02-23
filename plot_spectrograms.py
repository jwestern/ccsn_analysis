from numpy import *
from matplotlib import *

execfile('./pars.py')
#execfile('./compute_spectrograms2.py')

gwspecf   = pickle.load(open(  'gwspecf.dic','rb'))
anuespecf = pickle.load(open('anuespecf.dic','rb'))
nuxspecf  = pickle.load(open( 'nuxspecf.dic','rb'))
nuespecf  = pickle.load(open( 'nuespecf.dic','rb'))

gwspect   = pickle.load(open(  'gwspect.dic','rb'))
anuespect = pickle.load(open('anuespect.dic','rb'))
nuxspect  = pickle.load(open( 'nuxspect.dic','rb'))
nuespect  = pickle.load(open( 'nuespect.dic','rb'))

gwspec    = pickle.load(open(  'gwspec.dic','rb'))
anuespec  = pickle.load(open('anuespec.dic','rb'))
nuxspec   = pickle.load(open( 'nuxspec.dic','rb'))
nuespec   = pickle.load(open( 'nuespec.dic','rb'))

share_colorscale_nu = 'yes'

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

upper_freq_limit = 1.75e3 #in Hz... Largest frequency to plot in the spectrograms

#Get array coordinate for lower and upper limits of frequency that are to be plotted

gw_lf_lim   = {}
gw_uf_lim   = {}
anue_lf_lim = {}
anue_uf_lim = {}
nux_lf_lim  = {}
nux_uf_lim  = {}
nue_lf_lim  = {}
nue_uf_lim  = {}
for r in rotrates:
	gw_lf_lim[r]   = 2
	gw_uf_lim[r]   = amin(  where(gwspecf[r]>upper_freq_limit))+1
	anue_lf_lim[r] = 2
	anue_uf_lim[r] = amin(where(anuespecf[r]>upper_freq_limit))+1
	nux_lf_lim[r]  = 2
	nux_uf_lim[r]  = amin( where(nuxspecf[r]>upper_freq_limit))+1
	nue_lf_lim[r]  = 2
	nue_uf_lim[r]  = amin( where(nuespecf[r]>upper_freq_limit))+1

#Get array coordinate of the bounce time
gwbouncet   = {}
anuebouncet = {}
nuxbouncet  = {}
nuebouncet  = {}
for r in rotrates:
	gwbouncet[r]   = abs(  gwspect[r]).argmin()
	anuebouncet[r] = abs(anuespect[r]).argmin()
	nuxbouncet[r]  = abs( nuxspect[r]).argmin()
	nuebouncet[r]  = abs( nuespect[r]).argmin()

#Get array coordinate of fraction of a window prior to bounce time
gwprebouncet   = {}
anueprebouncet = {}
nuxprebouncet  = {}
nueprebouncet  = {}
thatfraction = 0.4
for r in rotrates:
	gwprebouncet[r]   = abs(  gwspect[r]+thatfraction*WindowWidth*1e-3).argmin()
	anueprebouncet[r] = abs(anuespect[r]+thatfraction*WindowWidth*1e-3).argmin()
	nuxprebouncet[r]  = abs( nuxspect[r]+thatfraction*WindowWidth*1e-3).argmin()
	nueprebouncet[r]  = abs( nuespect[r]+thatfraction*WindowWidth*1e-3).argmin()

#Get max and min values of the spectrograms across all rotation cases, but separately for GW and nu, so that
#the plots will have a shared color scale across rotation cases and can be compared by eye.
gwmins   = []
anuemins = []
nuxmins  = []
nuemins  = []

gwmaxs   = []
anuemaxs = []
nuxmaxs  = []
nuemaxs  = []

for r in rotrates:
	gwmins.append(     gwspec[r][   gw_lf_lim[r]:  gw_uf_lim[r],  gwprebouncet[r]: ].min() )
	anuemins.append( anuespec[r][ anue_lf_lim[r]:anue_uf_lim[r],anueprebouncet[r]: ].min() )
	nuxmins.append(   nuxspec[r][  nux_lf_lim[r]: nux_uf_lim[r], nuxprebouncet[r]: ].min() )
	nuemins.append(   nuespec[r][  nue_lf_lim[r]: nue_uf_lim[r], nueprebouncet[r]: ].min() )
	gwmaxs.append(     gwspec[r][   gw_lf_lim[r]:  gw_uf_lim[r],  gwprebouncet[r]: ].max() )
	anuemaxs.append( anuespec[r][ anue_lf_lim[r]:anue_uf_lim[r],anueprebouncet[r]: ].max() )
	nuxmaxs.append(   nuxspec[r][  nux_lf_lim[r]: nux_uf_lim[r], nuxprebouncet[r]: ].max() )
	nuemaxs.append(   nuespec[r][  nue_lf_lim[r]: nue_uf_lim[r], nueprebouncet[r]: ].max() )

gw_level_min   = amin(   gwmins ) 
anue_level_min = amin( anuemins )
nux_level_min  = amin(  nuxmins )
nue_level_min  = amin(  nuemins )

gw_level_max   = amax(   gwmaxs ) 
anue_level_max = amax( anuemaxs )
nux_level_max  = amax(  nuxmaxs )
nue_level_max  = amax(  nuemaxs )

#Create the colorscales now
gwLevels   = MaxNLocator(nbins=100).tick_values(log10(  gw_level_min), log10(  gw_level_max))

if share_colorscale_nu=='yes':
	anueLevels = MaxNLocator(nbins=100).tick_values(log10( amin([anue_level_min,nux_level_min,nue_level_min]) ), log10( amax([anue_level_max,nux_level_max,nue_level_max]) ))
	nuxLevels  = anueLevels
	nueLevels  = anueLevels
else:
	anueLevels = MaxNLocator(nbins=100).tick_values(log10(anue_level_min), log10(anue_level_max))
	nuxLevels  = MaxNLocator(nbins=100).tick_values(log10( nux_level_min), log10( nux_level_max))
	nueLevels  = MaxNLocator(nbins=100).tick_values(log10( nue_level_min), log10( nue_level_max))

#Now make plots
for nr in range(1,numrows+1):
	for nc in range(1,numcols+1):
		r = rotrates[nc-1]
		sig = sigtypes[nr-1]
		Title = titles[nr-1]+r': $\omega_{initial} = $'+r+' (rad/s)'
		ax[nc][nr].grid()
		if sig=='gw2':
			ax[nc][nr].contourf((gwspect[r][gwprebouncet[r]:])*1e3,gwspecf[r][gw_lf_lim[r]:gw_uf_lim[r]],log10(gwspec[r][gw_lf_lim[r]:gw_uf_lim[r],gwprebouncet[r]:]),levels=gwLevels,cmap=Cmap)
		elif sig=='anue':
			ax[nc][nr].contourf((anuespect[r][anueprebouncet[r]:])*1e3,anuespecf[r][anue_lf_lim[r]:anue_uf_lim[r]],log10(anuespec[r][anue_lf_lim[r]:anue_uf_lim[r],anueprebouncet[r]:]),levels=anueLevels,cmap=Cmap)
		elif sig=='nux':
			ax[nc][nr].contourf((nuxspect[r][nuxprebouncet[r]:])*1e3,nuxspecf[r][nux_lf_lim[r]:nux_uf_lim[r]],log10(nuxspec[r][nux_lf_lim[r]:nux_uf_lim[r],nuxprebouncet[r]:]),levels=nuxLevels,cmap=Cmap)
		elif sig=='nue':
			ax[nc][nr].contourf((nuespect[r][nueprebouncet[r]:])*1e3,nuespecf[r][nue_lf_lim[r]:nue_uf_lim[r]],log10(nuespec[r][nue_lf_lim[r]:nue_uf_lim[r],nueprebouncet[r]:]),levels=nueLevels,cmap=Cmap)
		ax[nc][nr].set_title(r'')
		if mod(nc-1,numcols)==0:
			ax[nc][nr].set_ylabel(r'$f$ (Hz)')
		if nr==numrows:
			ax[nc][nr].set_xlabel(r'$t-t_\mathrm{bounce}$ (ms)')
		ax[nc][nr].set_title(Title,size=13)

