from numpy import *
from matplotlib import *
import pickle
from scipy.interpolate import interp1d
from scipy.interpolate import interp2d
import math

execfile('./pars_velocity.py')

r = rotrate_to_extract

rr       = pickle.load(open(            './'+datadir+'/rr.dic','rb'))*1e-5 #Convert to km

rr       = np.round(rr,9) #Round to 9 decimal places, so we can accurately count how many unique values there are

dt = 0.1 #time resolution for velocity field (ms)

ru = np.unique(rr)
ra = range(len(ru))

xmid = pickle.load(open('./'+datadir+'/xmid.dic','rb'))

xmidspl = {}

#Create 1d splines which output the median frequency within each mask

modes = xmid[r].keys()

for m in modes:

	xmidspl[m] = interp1d(xmid[r][m]['time'],xmid[r][m]['freq'],bounds_error=False,fill_value='extrapolate')


#Read in sph harm wavefunctions

if mass_weighted=='yes':
	ER  = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_radius_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
	ETH = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_theta_rot' +r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
	if r!='0.0':
		EPH = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_phi_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','rb'))
else:
	ER  = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_radius_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
	ETH = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_theta_rot' +r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
	if r!='0.0':
		EPH = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_phi_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))


#Turn them into arrays

timesi = ER.keys()

ERarray  = {}
ETHarray = {}
if r!='0.0':
	EPHarray = {}

for m in modes:
	
	ERarray[m]  = {}
	ETHarray[m] = {}
	if r!='0.0':
		EPHarray[m] = {}

	for l in poloidal_numbers:
								#time index  mode name   poloidal number
		ERarray[m][l]  = np.zeros((len(timesi),len( ER[ timesi[0] ][     m    ][    l     ])))
		ETHarray[m][l] = np.zeros((len(timesi),len(ETH[ timesi[0] ][m][l])))
		if r!='0.0':
			EPHarray[m][l] = np.zeros((len(timesi),len(EPH[ timesi[0] ][m][l])))



#Fill the arrays with the wavefunctions

for m in modes:
	for l in poloidal_numbers:
		for ti in timesi:
			ERarray[m][l][ti,:]  = ER[ti][m][l]
			ETHarray[m][l][ti,:] = ETH[ti][m][l]
			if r!='0.0':
				EPHarray[m][l][ti,:] = EPH[ti][m][l]

if mass_weighted=='yes':
	pickle.dump( ERarray,open( './'+datadir+'/ERarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
	pickle.dump(ETHarray,open('./'+datadir+'/ETHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
	if r!='0.0':
		pickle.dump( EPHarray,open('./'+datadir+'/EPHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
else:
	pickle.dump( ERarray,open( './'+datadir+'/ERarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
	pickle.dump(ETHarray,open('./'+datadir+'/ETHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
	if r!='0.0':
		pickle.dump( EPHarray,open('./'+datadir+'/EPHarray_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))


#Make 2d splines out of them

tt = {}
ff = {}

for m in modes:
	ff[m] = xmid[r][m]['freq']
	tt[m] = xmid[r][m]['time'] #This time roughly begins when the mode turns on, ends when it turns off.

'''
ERarrayspl  = {}
ETHarrayspl = {}
if r!='0.0':
	EPHarrayspl = {}

t = pickle.load(open('t_filtered_tightenfactor'+str(tighten_factor)+'.dic','rb')) #This time is the properly spaced one, needed for 2d splines.
#t = pickle.load(open('spect_'+Mode+'.dic','rb')) #This time is the properly spaced one (output from original spectrogram computation), needed for 2d splines.
#t = t[r][:-1]
t = t[r]



for m in modes:

	ERarrayspl[m]  = {}
	ETHarrayspl[m] = {}
	if r!='0.0':
		EPHarrayspl[m] = {}

	tshifted = t

	for l in poloidal_numbers:
		
		ERarrayspl[m][l]  = interp2d(ru, tshifted, ERarray[m][l])
		ETHarrayspl[m][l] = interp2d(ru, tshifted, ETHarray[m][l])
		if r!='0.0':
			EPHarrayspl[m][l] = interp2d(ru, tshifted, EPHarray[m][l])


#Extract the eigenmodes via subsampling over the entire interval of time that the masked mode is active

EigenmodesR  = {}
EigenmodesTH = {}
if r!='0.0':
	EigenmodesPH = {}

for m in modes:

	tstart = tt[m][0] #starting time for this mode

	tend   = tt[m][-1] #ending time for this mode

	fstart = xmidspl[m](tstart) #starting median frequency for this mode

	fend   = xmidspl[m](tend) #ending median frequency for this mode

	Tstart = 1e3/fstart #starting period of oscillation for this mode

	if half_periods=='yes':
		nshifts = int(math.ceil(round(0.5*Tstart/dt)))
	else:
		nshifts = int(math.ceil(round(Tstart/dt))) #number of shifts to do, a snapshot of the eigenmode per shift

	EigenmodesR[m]  = {}
	EigenmodesTH[m] = {}
	if r!='0.0':
		EigenmodesPH[m] = {}

	for l in poloidal_numbers:

		EigenmodesR[m][l]  = {}
		EigenmodesTH[m][l] = {}
		if r!='0.0':
			EigenmodesPH[m][l] = {}

		for nt in range(nshifts):

			print 'Doing mode '+m+', l = '+str(l)+', shift '+str(nt)+' of '+str(nshifts)+'.'

			EigenmodesR[m][l][nt]  = {}
			EigenmodesTH[m][l][nt] = {}
			if r!='0.0':
				EigenmodesPH[m][l][nt] = {}

			tnow = tstart + nt*dt #Shift the starting time forward by nt*dt

			passed_tend = 'no'

			sample_count = 0 #initialize sample count

			alternating_counter = 0 #keep track of alternating sign, in case we're doing half periods

			sign=1. #initialize sign

			while passed_tend=='no':

				if half_periods=='yes':
					if alternating_counter % 2 == 0: #If even, multiply by 1
						sign=1.
					else:
						sign=-1.

				EigenmodesR[m][l][nt][sample_count] = sign*ERarrayspl[m][l](ru,tnow)
				EigenmodesTH[m][l][nt][sample_count] = sign*ETHarrayspl[m][l](ru,tnow)
				if r!='0.0':
					EigenmodesPH[m][l][nt][sample_count] = sign*EPHarrayspl[m][l](ru,tnow)

				fnow = xmidspl[m](tnow) #get current oscillation frequency

				if half_periods=='yes':
					tnow += 0.5e3/fnow #step forward in time by half a period
				else:
					tnow += 1.0e3/fnow #step forward in time by one period
				
				sample_count += 1

				alternating_counter += 1

				if tnow>tend: #Check if should exit the loop, i.e. if we passed tend
					passed_tend = 'yes'

EigenmodesRarrays  = {}
EigenmodesTHarrays = {}
if r!='0.0':
	EigenmodesPHarrays = {}

for m in modes:

	EigenmodesRarrays[m]  = {}
	EigenmodesTHarrays[m] = {}
	if r!='0.0':
		EigenmodesPHarrays[m] = {}

	for l in poloidal_numbers:

		EigenmodesRarrays[m][l]  = {}
		EigenmodesTHarrays[m][l] = {}
		if r!='0.0':
			EigenmodesPHarrays[m][l] = {}

		nshifts_keys = EigenmodesR[m][l].keys()

		for nt in nshifts_keys:

			nsamples_keys = EigenmodesR[m][l][nt].keys()

			EigenmodesRarrays[m][l][nt]  = np.zeros((len(nsamples_keys),len(ru)))
			EigenmodesTHarrays[m][l][nt] = np.zeros((len(nsamples_keys),len(ru)))
			if r!='0.0':
				EigenmodesPHarrays[m][l][nt] = np.zeros((len(nsamples_keys),len(ru)))

			for ns in nsamples_keys:

				EigenmodesRarrays[m][l][nt][ns,:] = EigenmodesR[m][l][nt][ns]				
				EigenmodesTHarrays[m][l][nt][ns,:] = EigenmodesTH[m][l][nt][ns]
				if r!='0.0':
					EigenmodesPHarrays[m][l][nt][ns,:] = EigenmodesPH[m][l][nt][ns]

if mass_weighted=='yes':
	pickle.dump(EigenmodesRarrays ,open( 'EigenmodesRarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
	pickle.dump(EigenmodesTHarrays,open('EigenmodesTHarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
	if r!='0.0':
		pickle.dump(EigenmodesPHarrays,open('EigenmodesPHarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
else:
	pickle.dump(EigenmodesRarrays ,open( 'EigenmodesRarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
	pickle.dump(EigenmodesTHarrays,open('EigenmodesTHarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
	if r!='0.0':
		pickle.dump(EigenmodesPHarrays,open('EigenmodesPHarrays_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
'''
'''
	for l in poloidal_numbers:

		EigenmodesR[m][l]  = np.zeros((nshifts,len(ru))) #predefine array to hold the eigenmode 'surface', i.e. temporal snapshots over one period
		EigenmodesTH[m][l] = np.zeros((nshifts,len(ru)))
		if r!='0.0':
			EigenmodesPH[m][l] = np.zeros((nshifts,len(ru)))

		for nt in range(nshifts):

			print 'Doing mode '+m+', l = '+str(l)+', shift '+str(nt)+' of '+str(nshifts)+'.'

			tnow = tstart + nt*dt #Shift the starting time forward by nt*dt

			passed_tend = 'no'
	
			while passed_tend=='no':

				EigenmodesR[m][l][nt,:] += ERarrayspl[m][l](ru,tnow)
				EigenmodesTH[m][l][nt,:] += ETHarrayspl[m][l](ru,tnow)
				if r!='0.0':
					EigenmodesPH[m][l][nt,:] += EPHarrayspl[m][l](ru,tnow)

				fnow = xmidspl[m](tnow) #get current oscillation frequency

				tnow += 1e3/fnow #step forward in time by 1/fnow
				#if isnan(tnow)==False:
				#	print tnow
				if tnow>tend: #Check if should exit the loop, i.e. if we passed tend
					passed_tend = 'yes'
'''

















