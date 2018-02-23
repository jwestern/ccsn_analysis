from numpy import *
from matplotlib import *

execfile('./pars.py')
'''
gw_anue_cspec_real  = pickle.load(open( 'gw_anue_cspec_real.dic','rb'))
gw_anue_cspec_imag  = pickle.load(open( 'gw_anue_cspec_imag.dic','rb'))
gw_nux_cspec_real   = pickle.load(open(  'gw_nux_cspec_real.dic','rb'))
gw_nux_cspec_imag   = pickle.load(open(  'gw_nux_cspec_imag.dic','rb'))
gw_nue_cspec_real   = pickle.load(open(  'gw_nue_cspec_real.dic','rb'))
gw_nue_cspec_imag   = pickle.load(open(  'gw_nue_cspec_imag.dic','rb'))
anue_nux_cspec_real = pickle.load(open('anue_nux_cspec_real.dic','rb'))
anue_nux_cspec_imag = pickle.load(open('anue_nux_cspec_imag.dic','rb'))
anue_nue_cspec_real = pickle.load(open('anue_nue_cspec_real.dic','rb'))
anue_nue_cspec_imag = pickle.load(open('anue_nue_cspec_imag.dic','rb'))
nue_nux_cspec_real  = pickle.load(open( 'nue_nux_cspec_real.dic','rb'))
nue_nux_cspec_imag  = pickle.load(open( 'nue_nux_cspec_imag.dic','rb'))
'''
times               = pickle.load(open(        'times_cspec.dic','rb'))
freqs               = pickle.load(open(        'freqs_cspec.dic','rb'))

gwspecint           = pickle.load(open(  'gwspecint.dic','rb'))
anuespecint         = pickle.load(open('anuespecint.dic','rb'))
nuxspecint          = pickle.load(open( 'nuxspecint.dic','rb'))
nuespecint          = pickle.load(open( 'nuespecint.dic','rb'))

#Cut the integrated spectra timeseries to match (it's only a couple of points, it shouldn't matter)
for r in rotrates:
	lt = len(times[r])
	gwspecint[r]   =   gwspecint[r][:lt]
	anuespecint[r] = anuespecint[r][:lt]
	nuxspecint[r]  =  nuxspecint[r][:lt]
	nuespecint[r]  =  nuespecint[r][:lt]

#Compute the magnitude squared of these
gw_anue_cspec  = {}
gw_nux_cspec   = {}
gw_nue_cspec   = {}
anue_nux_cspec = {}
anue_nue_cspec = {}
nue_nux_cspec  = {}

plot_cospectrum   = 'no'
plot_quadspectrum = 'no'
plot_fullspectrum = 'yes'

for r in rotrates:
	if plot_cospectrum == 'yes':
		gw_anue_cspec[r]  = 10.**( log10(  gw_anue_cspec_real[r]**2.  ) - log10(   gwspecint[r]) - log10(anuespecint[r] ) )
		gw_nux_cspec[r]   = 10.**( log10(   gw_nux_cspec_real[r]**2.  ) - log10(   gwspecint[r]) - log10( nuxspecint[r] ) )
		gw_nue_cspec[r]   = 10.**( log10(   gw_nue_cspec_real[r]**2.  ) - log10(   gwspecint[r]) - log10( nuespecint[r] ) )
		anue_nux_cspec[r] = 10.**( log10( anue_nux_cspec_real[r]**2.  ) - log10( anuespecint[r]) - log10( nuxspecint[r] ) )
		anue_nue_cspec[r] = 10.**( log10( anue_nue_cspec_real[r]**2.  ) - log10( anuespecint[r]) - log10( nuespecint[r] ) )
		nue_nux_cspec[r]  = 10.**( log10(  nue_nux_cspec_real[r]**2.  ) - log10(  nuespecint[r]) - log10( nuxspecint[r] ) )
	elif plot_quadspectrum == 'yes':
		gw_anue_cspec[r]  = 10.**( log10(  gw_anue_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10(anuespecint[r] ) )
		gw_nux_cspec[r]   = 10.**( log10(   gw_nux_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10( nuxspecint[r] ) )
		gw_nue_cspec[r]   = 10.**( log10(   gw_nue_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10( nuespecint[r] ) )
		anue_nux_cspec[r] = 10.**( log10( anue_nux_cspec_imag[r]**2.  ) - log10( anuespecint[r]) - log10( nuxspecint[r] ) )
		anue_nue_cspec[r] = 10.**( log10( anue_nue_cspec_imag[r]**2.  ) - log10( anuespecint[r]) - log10( nuespecint[r] ) )
		nue_nux_cspec[r]  = 10.**( log10(  nue_nux_cspec_imag[r]**2.  ) - log10(  nuespecint[r]) - log10( nuxspecint[r] ) )
	elif plot_fullspectrum == 'yes':
		gw_anue_cspec[r]  = 10.**( log10(  gw_anue_cspec_real[r]**2. +  gw_anue_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10(anuespecint[r] ) )
		gw_nux_cspec[r]   = 10.**( log10(   gw_nux_cspec_real[r]**2. +   gw_nux_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10( nuxspecint[r] ) )
		gw_nue_cspec[r]   = 10.**( log10(   gw_nue_cspec_real[r]**2. +   gw_nue_cspec_imag[r]**2.  ) - log10(   gwspecint[r]) - log10( nuespecint[r] ) )
		anue_nux_cspec[r] = 10.**( log10( anue_nux_cspec_real[r]**2. + anue_nux_cspec_imag[r]**2.  ) - log10( anuespecint[r]) - log10( nuxspecint[r] ) )
		anue_nue_cspec[r] = 10.**( log10( anue_nue_cspec_real[r]**2. + anue_nue_cspec_imag[r]**2.  ) - log10( anuespecint[r]) - log10( nuespecint[r] ) )
		nue_nux_cspec[r]  = 10.**( log10(  nue_nux_cspec_real[r]**2. +  nue_nux_cspec_imag[r]**2.  ) - log10(  nuespecint[r]) - log10( nuxspecint[r] ) )

share_colorscales = 'yes'

cspec_sigtypes = ['anue_nux','anue_nue','nue_nux'] #['gw_anue','gw_nux','gw_nue','anue_nux','anue_nue','nue_nux']
cspec_titles   = [r'$\bar{\nu}_e$-$\nu_x$',r'$\bar{\nu}_e$-$\nu_e$',r'$\nu_e$-$\nu_x$'] #[r'GW-$\bar{\nu}_e$',r'GW-$\nu_x$',r'GW-$\nu_e$'] #,r'$\bar{\nu}_e$-$\nu_x$',r'$\bar{\nu}_e$-$\nu_e$',r'$\nu_e$-$\nu_x$']

numcols  = len(rotrates)
numrows  = len(cspec_sigtypes)
numplots = numcols*numrows

rcParams['axes.labelsize']=13.0

fig1=plt.figure()
fig1.subplots_adjust(bottom=0.15)
fig1.subplots_adjust(left=0.2)
fig1.subplots_adjust(hspace=.25)
#fig1.suptitle('Spectrograms')

ax = {}
for nc in range(1,numcols+1):
	ax[nc]={}
	for nr in range(1,numrows+1):
		ax[nc][nr] = fig1.add_subplot(numrows,numcols,(nr-1)*numcols                                              +nc)
#						              ^^^ how many times to add a whole row (start with 0 times)   ^the column in the given row

Cmap='jet'

upper_freq_limit = 1.25e3 #in Hz... Largest frequency to plot in the spectrograms

#Get array coordinate for lower and upper limits of frequency that are to be plotted
gw_anue_lf_lim  = {}
gw_anue_uf_lim  = {}
gw_nux_lf_lim   = {}
gw_nux_uf_lim   = {}
gw_nue_lf_lim   = {}
gw_nue_uf_lim   = {}

anue_nux_lf_lim = {}
anue_nux_uf_lim = {}
anue_nue_lf_lim = {}
anue_nue_uf_lim = {}

nue_nux_lf_lim  = {}
nue_nux_uf_lim  = {}

for r in rotrates:
	gw_anue_lf_lim[r]   = 2
	gw_anue_uf_lim[r]   = amin(  where(freqs[r]>upper_freq_limit))+1
	gw_nux_lf_lim[r]    = 2
	gw_nux_uf_lim[r]    = gw_anue_uf_lim[r]
	gw_nue_lf_lim[r]    = 2
	gw_nue_uf_lim[r]    = gw_anue_uf_lim[r]
	anue_nux_lf_lim[r]  = 2
	anue_nux_uf_lim[r]  = gw_anue_uf_lim[r]
	anue_nue_lf_lim[r]  = 2
	anue_nue_uf_lim[r]  = gw_anue_uf_lim[r]
	nue_nux_lf_lim[r]   = 2
	nue_nux_uf_lim[r]   = gw_anue_uf_lim[r]
	

#Get array coordinate of the bounce time
bouncet   = {}
for r in rotrates:
	bouncet[r]   = abs(times[r]).argmin()

#Get array coordinate of fraction of a window prior to bounce time
prebouncet   = {}
thatfraction = 0.4
for r in rotrates:
	prebouncet[r]   = abs(times[r]+thatfraction*WindowWidth*1e-3).argmin()

#Get max and min values of the spectrograms across all rotation cases
gw_anue_mins  = []
gw_nux_mins   = []
gw_nue_mins   = []
anue_nux_mins = []
anue_nue_mins = []
nue_nux_mins  = []

gw_anue_maxs  = []
gw_nux_maxs   = []
gw_nue_maxs   = []
anue_nux_maxs = []
anue_nue_maxs = []
nue_nux_maxs  = []

for r in rotrates:
	gw_anue_mins.append(   gw_anue_cspec[r][  gw_anue_lf_lim[r]: gw_anue_uf_lim[r],  prebouncet[r]: ].min() )
	gw_nux_mins.append(     gw_nux_cspec[r][   gw_nux_lf_lim[r]:  gw_nux_uf_lim[r],  prebouncet[r]: ].min() )
	gw_nue_mins.append(     gw_nue_cspec[r][   gw_nue_lf_lim[r]:  gw_nue_uf_lim[r],  prebouncet[r]: ].min() )
	anue_nux_mins.append( anue_nux_cspec[r][ anue_nux_lf_lim[r]:anue_nux_uf_lim[r],  prebouncet[r]: ].min() )
	anue_nue_mins.append( anue_nue_cspec[r][ anue_nue_lf_lim[r]:anue_nue_uf_lim[r],  prebouncet[r]: ].min() )
	nue_nux_mins.append(   nue_nux_cspec[r][  nue_nux_lf_lim[r]: nue_nux_uf_lim[r],  prebouncet[r]: ].min() )

	gw_anue_maxs.append(   gw_anue_cspec[r][  gw_anue_lf_lim[r]: gw_anue_uf_lim[r],  prebouncet[r]: ].max() )
	gw_nux_maxs.append(     gw_nux_cspec[r][   gw_nux_lf_lim[r]:  gw_nux_uf_lim[r],  prebouncet[r]: ].max() )
	gw_nue_maxs.append(     gw_nue_cspec[r][   gw_nue_lf_lim[r]:  gw_nue_uf_lim[r],  prebouncet[r]: ].max() )
	anue_nux_maxs.append( anue_nux_cspec[r][ anue_nux_lf_lim[r]:anue_nux_uf_lim[r],  prebouncet[r]: ].max() )
	anue_nue_maxs.append( anue_nue_cspec[r][ anue_nue_lf_lim[r]:anue_nue_uf_lim[r],  prebouncet[r]: ].max() )
	nue_nux_maxs.append(   nue_nux_cspec[r][  nue_nux_lf_lim[r]: nue_nux_uf_lim[r],  prebouncet[r]: ].max() )


gw_anue_level_min  = amin(  gw_anue_mins )
gw_nux_level_min   = amin(   gw_nux_mins )
gw_nue_level_min   = amin(   gw_nue_mins )
anue_nux_level_min = amin( anue_nux_mins )
anue_nue_level_min = amin( anue_nue_mins )
nue_nux_level_min  = amin(  nue_nux_mins )

gw_anue_level_max  = amax(  gw_anue_maxs )
gw_nux_level_max   = amax(   gw_nux_maxs )
gw_nue_level_max   = amax(   gw_nue_maxs )
anue_nux_level_max = amax( anue_nux_maxs )
anue_nue_level_max = amax( anue_nue_maxs )
nue_nux_level_max  = amax(  nue_nux_maxs )


#Create the colorscales now
if share_colorscale_nu=='yes':
    gw_anue_Levels  = MaxNLocator(nbins=100).tick_values(log10( amin([gw_anue_level_min,gw_nux_level_min,gw_nux_level_min]) ), log10( amax([gw_anue_level_max,gw_nux_level_max,gw_nux_level_max]) ))
    gw_nux_Levels   = gw_anue_Levels
    gw_nue_Levels   = gw_anue_Levels
    anue_nux_Levels = MaxNLocator(nbins=100).tick_values(log10( amin([anue_nux_level_min,anue_nue_level_min,nue_nux_level_min]) ), log10( amax([anue_nux_level_max,anue_nue_level_max,nue_nux_level_max]) ))
    anue_nue_Levels = anue_nux_Levels
    nue_nux_Levels  = anue_nux_Levels
else:
	gw_anue_Levels     = MaxNLocator(nbins=100).tick_values(log10(  gw_anue_level_min), log10(  gw_anue_level_max))
	gw_nux_Levels      = MaxNLocator(nbins=100).tick_values(log10(   gw_nux_level_min), log10(   gw_nux_level_max))
	gw_nue_Levels      = MaxNLocator(nbins=100).tick_values(log10(   gw_nue_level_min), log10(   gw_nue_level_max))
	anue_nux_Levels    = MaxNLocator(nbins=100).tick_values(log10( anue_nux_level_min), log10( anue_nux_level_max))
	anue_nue_Levels    = MaxNLocator(nbins=100).tick_values(log10( anue_nue_level_min), log10( anue_nue_level_max))
	nue_nux_Levels     = MaxNLocator(nbins=100).tick_values(log10(  nue_nux_level_min), log10(  nue_nux_level_max))


#cspec_sigtypes = ['gw_anue','gw_nux','gw_nue','anue_nux','anue_nue','nue_nux']

#Now make plots
for nr in range(1,numrows+1):
	for nc in range(1,numcols+1):
		r = rotrates[nc-1]
		sig = cspec_sigtypes[nr-1]
		Title = cspec_titles[nr-1]+r': $\omega_{initial} = $'+r+' (rad/s)'
		pbt = prebouncet[r]
		ax[nc][nr].grid()

		if sig=='gw_anue':
			lf =  gw_anue_lf_lim[r]
			uf =  gw_anue_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10( gw_anue_cspec[r][lf:uf,pbt:]),levels= gw_anue_Levels,cmap=Cmap)
		elif sig=='gw_nux':
			lf =   gw_nux_lf_lim[r]
			uf =   gw_nux_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10(  gw_nux_cspec[r][lf:uf,pbt:]),levels=  gw_nux_Levels,cmap=Cmap)
		elif sig=='gw_nue':
			lf =   gw_nue_lf_lim[r]
			uf =   gw_nue_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10(  gw_nue_cspec[r][lf:uf,pbt:]),levels=  gw_nue_Levels,cmap=Cmap)
		elif sig=='anue_nux':
			lf = anue_nux_lf_lim[r]
			uf = anue_nux_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10(anue_nux_cspec[r][lf:uf,pbt:]),levels=anue_nux_Levels,cmap=Cmap)
		elif sig=='anue_nue':
			lf = anue_nue_lf_lim[r]
			uf = anue_nue_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10(anue_nue_cspec[r][lf:uf,pbt:]),levels=anue_nue_Levels,cmap=Cmap)
		elif sig=='nue_nux':
			lf =  nue_nux_lf_lim[r]
			uf =  nue_nux_uf_lim[r]
			ax[nc][nr].contourf((times[r][pbt:])*1e3,freqs[r][lf:uf],log10( nue_nux_cspec[r][lf:uf,pbt:]),levels= nue_nux_Levels,cmap=Cmap)

		ax[nc][nr].set_title(r'')
		if mod(nc-1,numcols)==0:
			ax[nc][nr].set_ylabel(r'$f$ (Hz)')
		if nr==numrows:
			ax[nc][nr].set_xlabel(r'$t-t_\mathrm{bounce}$ (ms)')
		ax[nc][nr].set_title(Title,size=13)

