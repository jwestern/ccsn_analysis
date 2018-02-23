from numpy import *
from scipy.interpolate import CubicSpline
import pickle

execfile('./pars_alt.py')

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
rho  ={}
Rpns ={}
Tpns ={}
for rotrate in rotrates:
	rho[rotrate]   = all_data['rhoc'  ]['signal'][rotrate]
	Rpns[rotrate]  = all_data['pnsrad']['signal'][rotrate]
	Tpns[rotrate]  = all_data['Mns']['signal'][rotrate]

#times
rhot  ={}
Rpnst ={}
Tpnst ={}
for rotrate in rotrates:
	rhot[rotrate]   = all_data['rhoc'  ]['time'][rotrate] - bouncetimes[rotrate] #Transform time coordindate so that bounce time is at t=0
	Rpnst[rotrate]  = all_data['pnsrad']['time'][rotrate] - bouncetimes[rotrate]
	Tpnst[rotrate]  = all_data['Mns']['time'][rotrate] - bouncetimes[rotrate]

#Get shortest time steps, for later splines
#Start from [20:] because first times are wonky, might get 0 difference
dt = {}
inflatefactor = 100. #multiply dt by this, in case time series are way too long
for r in rotrates:
	dt[r] = amin([ amin( [amin(rhot[r][20:]-rhot[r][19:-1]), amin(Rpnst[r][20:]-Rpnst[r][19:-1])] ), amin(Tpnst[r][20:]-Tpnst[r][19:-1]) ])*inflatefactor

#Get min and max times, for later splines. Just use rho data for this, they're almost the same.
#Begin with 18th here, since initial times are wonky
mint = {}
maxt = {}
for r in rotrates:
	mint[r] = rhot[r][18]
	maxt[r] = rhot[r][-1]

#Get even time sequences. They will be the same for both nu and gw data, and are thus named appropriately
t = {}
for r in rotrates:
	t[r] = arange(mint[r],maxt[r],dt[r])

#Now define splines
rhospline   = {}
Rpnsspline  = {}
Tpnsspline  = {}
for r in rotrates:
	rhospline[r]   = CubicSpline(  rhot[r][18:],  rho[r][18:])
	Rpnsspline[r]  = CubicSpline( Rpnst[r][18:], Rpns[r][18:])
	Tpnsspline[r]  = CubicSpline( Tpnst[r][18:], Tpns[r][18:])

#Get even signal sequences using the splines and the previously defined even time sequences. Append "c" to the name, meaning "clean".
rhoc   = {}
Rpnsc  = {}
Tpnsc  = {}
for r in rotrates:
	rhoc[r]   =   rhospline[r](t[r])
	Rpnsc[r]  =  Rpnsspline[r](t[r])
	Tpnsc[r]  =  Tpnsspline[r](t[r])

#Remove first part of the signal, up to WindowWidth prior to the bounce time. This keeps the data and spectrogram filesizes more manageable.
ww=WindowWidth*1e-3
for r in rotrates:
	tcoord    = abs(t[r]+ww).argmin()
	rhoc[r]   =   rhoc[r][tcoord:]
	Rpnsc[r]  =  Rpnsc[r][tcoord:]
	Tpnsc[r]  =  Tpnsc[r][tcoord:]
	t[r]      =     t[r][tcoord:]

pickle.dump(t,     open(     't_alt.dic','wb'))
pickle.dump(rhoc,  open(  'rhoc.dic','wb'))
pickle.dump(Rpnsc, open( 'Rpnsc.dic','wb'))
pickle.dump(Tpnsc, open( 'Tpnsc.dic','wb'))
pickle.dump(dt,    open(    'dt.dic','wb'))
