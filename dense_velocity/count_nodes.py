from numpy import *
from matplotlib import *
import pickle
from scipy.interpolate import interp1d
from scipy.interpolate import interp2d
import math
import pdb

execfile('pars_velocity.py')

'''
print 'Calling get_rho_spline_in_r.py now...'
execfile('get_rho_spline_in_r.py')
print 'Returned from get_rho_spline_in_r.py...'
'''


r = rotrate_to_extract

rr       = pickle.load(open(            './'+datadir+'/rr.dic','rb'))*1e-5 #Convert to km

rr       = np.round(rr,9) #Round to 9 decimal places, so we can accurately count how many unique values there are

dt = 0.1 #time resolution for velocity field (ms)

ru = np.unique(rr)
ra = range(len(ru))


rpns_avgs_dic = pickle.load(open('./'+datadir+'/rpns_avgs_rot'+r+'_rpns_definition_rho_'+str(rpns_definition_rho/1e10)+'e10.dic','rb'))

rpns_spl_avg  = interp1d(rpns_avgs_dic['time'],rpns_avgs_dic['rpns_avgs'])


xmid = pickle.load(open('./'+datadir+'/xmid.dic','rb'))

xmidspl = {}

#Create 1d splines which output the median frequency within each mask

modes = xmid[r].keys()

for m in modes:

	xmidspl[m] = interp1d(xmid[r][m]['time'],xmid[r][m]['freq'],bounds_error=False,fill_value='extrapolate')

if mass_weighted=='yes':
	ERarray  = pickle.load(open( './'+datadir+'/ERarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
#	ETHarray = pickle.load(open('ETHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
#	if r!='0.0':
#		EPHarray = pickle.load(open('EPHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
else:
	ERarray  = pickle.load(open( './'+datadir+'/ERarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
#	ETHarray = pickle.load(open('ETHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
#	if r!='0.0':
#		EPHarray = pickle.load(open('EPHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))

#Make 2d splines out of them

tt = {}
ff = {}

for m in modes:
	ff[m] = xmid[r][m]['freq']
	tt[m] = xmid[r][m]['time'] #This time roughly begins when the mode turns on, ends when it turns off.

ERarrayspl  = {}
#ETHarrayspl = {}
#if r!='0.0':
#	EPHarrayspl = {}

###
### NOTE: the filtered velocity field becomes non-zero half of a window width ***before*** the mask is non-zero.
###
t = pickle.load(open('./'+datadir+'/t_filtered_tightenfactor'+str(tighten_factor)+'.dic','rb')) #This time is the properly spaced one, needed for 2d splines.
#t = pickle.load(open('spect_'+Mode+'.dic','rb')) #This time is the properly spaced one (output from original spectrogram computation), needed for 2d splines.
#t = t[r][:-1]
t = t[r]

for m in modes:

	ERarrayspl[m]  = {}
#	ETHarrayspl[m] = {}
#	if r!='0.0':
#		EPHarrayspl[m] = {}

	tshifted = t

	for l in poloidal_numbers:
		
		ERarrayspl[m][l]  = interp2d(ru, tshifted, ERarray[m][l])
#		ETHarrayspl[m][l] = interp2d(ru, tshifted, ETHarray[m][l])
#		if r!='0.0':
#			EPHarrayspl[m][l] = interp2d(ru, tshifted, EPHarray[m][l])
'''
#Get Rpns 

rpns = pickle.load(open('../Rpnsc.dic','rb'))
rpns = rpns[r]*1e-5
talt = pickle.load(open('../t_alt.dic','rb'))
talt = talt[r]*1e3

rpns_spl = interp1d(talt,rpns,fill_value='extrapolate')

#r spline for running past last value
'''
rspl = interp1d(range(len(ru)),ru,fill_value='extrapolate')

#Count nodes now. Get a 1-d array of integers (the node count), and a corresponding array of times and frequencies.

##
## A complication: Morozova et al. and Torres-Forne et al. both count nodes in the l=2 radial wavefunction. I was
## 		   expecting to count nodes in the l=0 radial wavefunction instead, and maybe it's more appropriate
##		   in our case since the energy in l=0 completely dwarfs the l=2 even for the rotating modes. But
##		   I think this will actually be determined by the behaviour of the modes in the non-rotating limit.
##

l=0 #Count l=0 modes. This may change depending on stuff.

nodes  = {}
tnodes = {}
fnodes = {}

for m in modes:

	#if m=='600':
	#	pdb.set_trace()

	tstart   = tt[m][ 0]
	tend     = tt[m][-1]

	times    = arange(tstart,tend,dt)

	timesi   = range(len(times))

	nodes[m]  = []
	tnodes[m] = []
	fnodes[m] = []

	for timei in timesi:

		time = times[timei]

		modenow    = ERarrayspl[m][l](ru,time)	#Do energy condition on the unsmoothed function	
		modenow_sm = gaussian_filter1d(ERarrayspl[m][l](ru,time),2,mode='constant',cval=0.0) #Do node count on smoothed function
		

		Etot    = sum(modenow**2.) #Total energy density in the mode. For checking energy threshold in while loop.
					   #Assumes that mass_weight = 0.5.
					   #### NOTE: we may want to integrate all R, TH, PH components and impose the energy
					   ####       condition on that instead.

		rnowi = 0 #initialize

		signold = int(round( np.sign(modenow_sm[rnowi]) )) #initialize, get first sign

		nodecount = 0 #initialize

		rnowi = 1 #update once before the loop

		rnow  = ru[rnowi] #radius one step into the array

		while rnow < rpns_spl_avg(time):

			signnew = int(round( np.sign(modenow_sm[rnowi]) )) #update signnew

			if signnew != signold: #If sign changed, count node.
				nodecount += 1

			signold = signnew #update signold

			rnowi += 1

			rnow=rspl(rnowi) #Using spline in case rnowi runs past end of ru array

			#Check whether energy threshold is exceeded with the updated rnow.
			#This assumes we've set mass_weight = 0.5 so that modenow**2 is the energy.
			#### NOTE: we may want to integrate all R, TH, PH components and impose the energy
			####       condition on that instead.

			if ( sum(modenow[:rnowi]**2.)/Etot > Ethreshold ):
				print 'Triggered energy threshold, rnow =', rnow
				rnow = rpns_spl_avg(time) + 1 #This should terminate the while loop.

		nodes[m].append(nodecount)
		tnodes[m].append(time)
		fnodes[m].append(xmidspl[m](time))














