from numpy import *
from scipy.interpolate import CubicSpline
import pickle

execfile('./pars.py')

all_data  = {}

for sigtype in sigtypes:
	all_data[sigtype]={}
	for axis in axes:
		all_data[sigtype][axis]={}


for sigtype in sigtypes:
	for axis in axes:
		for rot in rotrates:
			if axis == 'signal':
				all_data[sigtype][axis][rot] = loadtxt(sigtype+'_rot_'+rot+'.dat')[:,1]
			elif axis == 'time':
				all_data[sigtype][axis][rot] = loadtxt(sigtype+'_rot_'+rot+'.dat')[:,0]

#All the raw data being put into more tersely named variables

#signals
gw  ={}
anue={}
nux ={}
nue ={}
for rotrate in rotrates:
	gw[rotrate]   = all_data['gw2' ]['signal'][ rotrate]
	anue[rotrate] = all_data['anue']['signal'][ rotrate]
	nux[rotrate]  = all_data['nux' ]['signal'][ rotrate]
	nue[rotrate]  = all_data['nue' ]['signal'][ rotrate]

#times
gwt  ={}
anuet={}
nuxt ={}
nuet ={}
for rotrate in rotrates:
	gwt[rotrate]   = all_data['gw2']['time'][ rotrate] - bouncetimes[rotrate] #Transform time coordindate so that bounce time is at t=0
	anuet[rotrate] = all_data['anue']['time'][rotrate] - bouncetimes[rotrate]
	nuxt[rotrate]  = all_data['nux']['time'][ rotrate] - bouncetimes[rotrate]
	nuet[rotrate]  = all_data['nue']['time'][ rotrate] - bouncetimes[rotrate]

#Get shortest time steps, for later splines
#Start from [20:] because first times are wonky, might get 0 difference
dt = {}
inflatefactor = 5e3 #multiply dt by this, in case time series are way too long
for r in rotrates:
	dt[r] = amin([ amin( [amin(gwt[r][20:]-gwt[r][19:-1]), amin(anuet[r][20:]-anuet[r][19:-1])] ), amin(nuxt[r][20:]-nuxt[r][19:-1]) ])*inflatefactor

#Get min and max times, for later splines. Just use GW data for this, they're almost the same.
#Begin with 18th here, since initial times are wonky
mint = {}
maxt = {}
for r in rotrates:
	mint[r] = gwt[r][18]
	maxt[r] = gwt[r][-1]

#Get even time sequences. They will be the same for both nu and gw data, and are thus named appropriately
t = {}
for r in rotrates:
	t[r] = arange(mint[r],maxt[r],dt[r])

#Now define splines
gwspline   = {}
anuespline = {}
nuxspline  = {}
nuespline  = {}
for r in rotrates:
	gwspline[r]   = CubicSpline(  gwt[r][18:],  gw[r][18:])
	anuespline[r] = CubicSpline(anuet[r][18:],anue[r][18:])
	nuxspline[r]  = CubicSpline( nuxt[r][18:], nux[r][18:])
	nuespline[r]  = CubicSpline( nuet[r][18:], nue[r][18:])

#Get even signal sequences using the splines and the previously defined even time sequences. Append "c" to the name, meaning "clean".
gwc   = {}
anuec = {}
nuxc  = {}
nuec  = {}
for r in rotrates:
	gwc[r]   =   gwspline[r](t[r])
	anuec[r] = anuespline[r](t[r])
	nuxc[r]  =  nuxspline[r](t[r])
	nuec[r]  =  nuespline[r](t[r])

#Remove first part of the signal, up to WindowWidth prior to the bounce time. This keeps the data and spectrogram filesizes more manageable.
ww=WindowWidth*1e-3
for r in rotrates:
	tcoord   = abs(t[r]+ww).argmin()
	gwc[r]   =   gwc[r][tcoord:]
	anuec[r] = anuec[r][tcoord:]
	nuxc[r]  =  nuxc[r][tcoord:]
	nuec[r]  =  nuec[r][tcoord:]
	t[r]     =     t[r][tcoord:]

pickle.dump(t,    open(    't.dic','wb'))
pickle.dump(gwc,  open(  'gwc.dic','wb'))
pickle.dump(anuec,open('anuec.dic','wb'))
pickle.dump(nuxc, open( 'nuxc.dic','wb'))
pickle.dump(nuec, open( 'nuec.dic','wb'))
pickle.dump(dt,   open(   'dt.dic','wb'))
