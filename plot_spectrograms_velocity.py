from numpy import *
from matplotlib import *

execfile('./pars_velocity.py')
#execfile('./compute_spectrograms2.py')

xx            = pickle.load(open(           'xx.dic','rb'))*1e-5 #Convert to km
yy            = pickle.load(open(           'yy.dic','rb'))*1e-5 #Convert to km
rr            = pickle.load(open(           'rr.dic','rb'))*1e-5 #Convert to km
theta         = pickle.load(open(        'theta.dic','rb'))

velxspecf     = pickle.load(open(    'velxspecf_psd.dic','rb'))
velyspecf     = pickle.load(open(    'velyspecf_psd.dic','rb'))
velrspecf     = pickle.load(open(    'velrspecf_psd.dic','rb'))
velthetaspecf = pickle.load(open('velthetaspecf_psd.dic','rb'))

velxspect     = pickle.load(open(    'velxspect_psd.dic','rb'))
velyspect     = pickle.load(open(    'velyspect_psd.dic','rb'))
velrspect     = pickle.load(open(    'velrspect_psd.dic','rb'))
velthetaspect = pickle.load(open('velthetaspect_psd.dic','rb'))

velxspec      = pickle.load(open(     'velxspec_psd.dic','rb'))
velyspec      = pickle.load(open(     'velyspec_psd.dic','rb'))
velrspec      = pickle.load(open(     'velrspec_psd.dic','rb'))
velthetaspec  = pickle.load(open( 'velthetaspec_psd.dic','rb'))

share_colorscale = 'no'

numpoints = shape(velxspec['0.0'].keys())[0]

#Get list of array positions of the points that are to be plotted.
plotpoints = []

for i in range(numpoints):
	if rr[i]>=minr: #get r between minr and maxr
		if rr[i]<=maxr:
			if theta[i]>=mintheta: #get theta between mintheta and maxtheta
				if theta[i]<=maxtheta:
					plotpoints.append(i)

numcols  = len(plotpoints)
numrows  = len(plotv)
numplots = numcols*numrows

rcParams['axes.labelsize']=13.0

'''
fig = {}
ax = {}
for r in rotrates:
	fig[r] = plt.figure()
	fig[r].subplots_adjust(bottom=0.15)
	fig[r].subplots_adjust(hspace=0.25)
	fig[r].subplots_adjust(  left=0.15)

	ax[r]  = {}
	
	for nc in range(1,numcols+1):
		ax[r][nc]={}
		for nr in range(1,numrows+1):
			ax[r][nc][nr] = fig[r].add_subplot(numrows,numcols,(nr-1)*numcols                                              +nc)
#						                           ^^^ how many times to add a whole row (start with 0 times)   ^the column in the given row
'''

fig = plt.figure()
fig.subplots_adjust(bottom=0.15)
fig.subplots_adjust(hspace=0.25)
fig.subplots_adjust(  left=0.15)
ax={}
for nc in range(1,numcols+1):
	ax[nc]={}
	for nr in range(1,numrows+1):
		ax[nc][nr] = fig.add_subplot(numrows,numcols,(nr-1)*numcols                                              +nc)
#						                           ^^^ how many times to add a whole row (start with 0 times)   ^the column in the given row

Cmap='jet'

upper_freq_limit = 2e3 #in Hz... Largest frequency to plot in the spectrograms

#Get array coordinate for lower and upper limits of frequency that are to be plotted

velx_lf_lim     = {}
velx_uf_lim     = {}
vely_lf_lim     = {}
vely_uf_lim     = {}
velr_lf_lim     = {}
velr_uf_lim     = {}
veltheta_lf_lim = {}
veltheta_uf_lim = {}
for p in plotpoints:
	velx_lf_lim[p]     = 2
	velx_uf_lim[p]     = amin(    where(velxspecf[plotr][p]>upper_freq_limit))+1
	vely_lf_lim[p]     = 2
	vely_uf_lim[p]     = amin(    where(velyspecf[plotr][p]>upper_freq_limit))+1
	velr_lf_lim[p]     = 2
	velr_uf_lim[p]     = amin(    where(velrspecf[plotr][p]>upper_freq_limit))+1
	veltheta_lf_lim[p] = 2
	veltheta_uf_lim[p] = amin(where(velthetaspecf[plotr][p]>upper_freq_limit))+1

#Get array coordinate of the bounce time
velxbouncet     = {}
velybouncet     = {}
velrbouncet     = {}
velthetabouncet = {}
for r in [plotr]:
	velxbouncet[r]     = abs(    velxspect[r][plotpoints[0]]).argmin()
	velybouncet[r]     = abs(    velyspect[r][plotpoints[0]]).argmin()
	velrbouncet[r]     = abs(    velrspect[r][plotpoints[0]]).argmin()
	velthetabouncet[r] = abs(velthetaspect[r][plotpoints[0]]).argmin()

#Get array coordinate of fraction of a window prior to bounce time
velxprebouncet     = {}
velyprebouncet     = {}
velrprebouncet     = {}
velthetaprebouncet = {}
thatfraction = 0.4
for r in [plotr]:
	velxprebouncet[r]     = abs(    velxspect[r][plotpoints[0]]+thatfraction*WindowWidth*1e-3).argmin()
	velyprebouncet[r]     = abs(    velyspect[r][plotpoints[0]]+thatfraction*WindowWidth*1e-3).argmin()
	velrprebouncet[r]     = abs(    velrspect[r][plotpoints[0]]+thatfraction*WindowWidth*1e-3).argmin()
	velthetaprebouncet[r] = abs(velthetaspect[r][plotpoints[0]]+thatfraction*WindowWidth*1e-3).argmin()

#Get max and min values of the spectrograms across all rotation cases, but separately for GW and nu, so that
#the plots will have a shared color scale across rotation cases and can be compared by eye.
velxmins     = []
velymins     = []
velrmins     = []
velthetamins = []

velxmaxs     = []
velymaxs     = []
velrmaxs     = []
velthetamaxs = []

for p in plotpoints:
	velxmins.append(        velxspec[plotr][p][    velx_lf_lim[p]:     velx_uf_lim[p],     velxprebouncet[plotr]: ].min() )
	velymins.append(        velyspec[plotr][p][    vely_lf_lim[p]:     vely_uf_lim[p],     velyprebouncet[plotr]: ].min() )
	velrmins.append(        velrspec[plotr][p][    velr_lf_lim[p]:     velr_uf_lim[p],     velrprebouncet[plotr]: ].min() )
	velthetamins.append(velthetaspec[plotr][p][veltheta_lf_lim[p]: veltheta_uf_lim[p], velthetaprebouncet[plotr]: ].min() )
	velxmaxs.append(        velxspec[plotr][p][    velx_lf_lim[p]:     velx_uf_lim[p],     velxprebouncet[plotr]: ].max() )
	velymaxs.append(        velyspec[plotr][p][    vely_lf_lim[p]:     vely_uf_lim[p],     velyprebouncet[plotr]: ].max() )
	velrmaxs.append(        velrspec[plotr][p][    velr_lf_lim[p]:     velr_uf_lim[p],     velrprebouncet[plotr]: ].max() )
	velthetamaxs.append(velthetaspec[plotr][p][veltheta_lf_lim[p]: veltheta_uf_lim[p], velthetaprebouncet[plotr]: ].max() )

velx_level_min     = amin(     velxmins ) 
vely_level_min     = amin(     velymins )
velr_level_min     = amin(     velrmins )
veltheta_level_min = amin( velthetamins )

velx_level_max     = amax(     velxmaxs ) 
vely_level_max     = amax(     velymaxs )
velr_level_max     = amax(     velrmaxs )
veltheta_level_max = amax( velthetamaxs )

#Create the colorscales now
if share_colorscale=='yes':
	velxLevels = MaxNLocator(nbins=100).tick_values(log10( amin([velx_level_min,vely_level_min,velr_level_min,veltheta_level_min]) ), log10( amax([velx_level_max,vely_level_max,velr_level_max,veltheta_level_max]) ))
	velyLevels     = velxLevels
	velrLevels     = velxLevels
	velthetaLevels = velxLevels
else:
	velxLevels     = MaxNLocator(nbins=100).tick_values(log10(     velx_level_min), log10(     velx_level_max))
	velyLevels     = MaxNLocator(nbins=100).tick_values(log10(     vely_level_min), log10(     vely_level_max))
	velrLevels     = MaxNLocator(nbins=100).tick_values(log10(     velr_level_min), log10(     velr_level_max))
	velthetaLevels = MaxNLocator(nbins=100).tick_values(log10( veltheta_level_min), log10( veltheta_level_max))

#Now make plots
for nr in range(1,numrows+1):
	for nc in range(1,numcols+1):
		#r        = rotrates[nc-1]
		p        = plotpoints[nc-1]
		sig      = plotv[nr-1]
		Title    = titles[nr-1]+' '+r'$\theta =$'+"{:.2f}".format(theta[p])+' '+r'$r =$'+"{:.0f}".format(rr[p])
		ax[nc][nr].grid()
		if   sig==    'velx':
			ax[nc][nr].contourf((velxspect[plotr][p][velxprebouncet[plotr]:])*1e3,velxspecf[plotr][p][velx_lf_lim[p]:velx_uf_lim[p]],log10(velxspec[plotr][p][velx_lf_lim[p]:velx_uf_lim[p],velxprebouncet[plotr]:]),levels=velxLevels,cmap=Cmap)
		elif sig==    'vely':
			ax[nc][nr].contourf((velyspect[plotr][p][velyprebouncet[plotr]:])*1e3,velyspecf[plotr][p][vely_lf_lim[p]:vely_uf_lim[p]],log10(velyspec[plotr][p][vely_lf_lim[p]:vely_uf_lim[p],velyprebouncet[plotr]:]),levels=velyLevels,cmap=Cmap)
		elif sig==    'velr':
			ax[nc][nr].contourf((velrspect[plotr][p][velrprebouncet[plotr]:])*1e3,velrspecf[plotr][p][velr_lf_lim[p]:velr_uf_lim[p]],log10(velrspec[plotr][p][velr_lf_lim[p]:velr_uf_lim[p],velrprebouncet[plotr]:]),levels=velrLevels,cmap=Cmap)
		elif sig=='veltheta':
			ax[nc][nr].contourf((velthetaspect[plotr][p][velthetaprebouncet[plotr]:])*1e3,velthetaspecf[plotr][p][veltheta_lf_lim[p]:veltheta_uf_lim[p]],log10(velthetaspec[plotr][p][veltheta_lf_lim[p]:veltheta_uf_lim[p],velthetaprebouncet[plotr]:]),levels=velthetaLevels,cmap=Cmap)
		#ax[nc][nr].set_title(r'')
		if mod(nc-1,numcols)==0:
			ax[nc][nr].set_ylabel(r'$f$ (Hz)')
		if nr==numrows:
			ax[nc][nr].set_xlabel(r'$t-t_\mathrm{bounce}$ (ms)')
		#if nr==1:
		ax[nc][nr].set_title(Title,size=13)

Suptitle = r'$\omega_{initial} = '+plotr+'$ (rad/s)'
fig.suptitle(Suptitle)

