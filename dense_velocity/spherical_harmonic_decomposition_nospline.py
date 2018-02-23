from numpy import *
from matplotlib import *
import numpy
from scipy.special import sph_harm
#from scipy.interpolate import SmoothBivariateSpline
from scipy.interpolate import interp1d
import numpy as np
import pickle

execfile('./pars_velocity.py')
r  = rotrate_to_decompose
print "DOING ROT "+r+" AND TIGHTEN_FACTOR "+str(tighten_factor)

if firstcall=='yes':
	print 'On first call of decomposition script, reading in data...'

	rr       = pickle.load(open(            './'+datadir+'/rr.dic','rb'))*1e-5 #Convert to km
	theta    = pickle.load(open(         './'+datadir+'/theta.dic','rb'))

	rr       = np.round(rr,9) #Round to 9 decimal places, so we can accurately count how many unique values there are
	theta    = np.round(theta,9)

	t        = pickle.load(open(       './'+datadir+'/t_filtered_tightenfactor'+str(tighten_factor)+'.dic','rb')) #[rotrates_to_filter], chosen in parameter file
	#tspec    = pickle.load(open(                                         'spect_complex.dic','rb'))
	#tspec    = tspec[r][:len(t[r])]*1e3 #In case there's a 1-point length mismatch, also change to ms

	masks    = pickle.load(open('./'+datadir+'/velocity_spectrogram_masks_tightenfactor'+str(tighten_factor)+'.dic','rb')) #Just to get keys from

	dt = 0.1*1e-3 #time resolution for velocity field

	if test=='yes':
		ti = 0 #time index to analyze
		modes = ['test']
	else:
		modes = masks[r].keys() #Get mode keys
		modes.append('unfiltered')


	#modes  = ['750'] #masks[r].keys() #Get mode keys
	#points = range(len(rr)) #Get point keys
	ru = np.unique(rr)
	tu = np.unique(theta)
	ra = range(len(ru))
	ta = range(len(tu))


	### Define vector spherical harmonic derivative w/ resp to theta

	def dsph_harm(l,theta): #(d/dtheta) Y_lm... We use phi=m=0 since we're in axisymmetry and it doesn't matter
		m=0
		return sqrt( (l-m)*(l+m+1) ) * sph_harm(m+1,l,0.,theta)


	### Read in all radii for this particular rotation rate
	vr  = {}
	vth = {}
	vph = {}
	if mass_weighted=='yes':
		rho = {}

	for pr in ra:
		if test=='yes':
			vr[pr]  = {}
			vth[pr] = {}
			vph[pr] = {}

			for pt in ta: #Make same dictionary structure as actual data
				vr[pr][pt]  = {}
				vth[pr][pt] = {}
				vph[pr][pt] = {}

				vr[pr][pt]['test']  = {}
				vth[pr][pt]['test'] = {}
				vph[pr][pt]['test'] = {}

			rad   = ru[pr]

			l_r   = 2 #poloidal numbers to excite
			l_th  = 3
			l_ph  = 4
			xi_r  = np.sin(2*pi*rad/30.) #this is a trial radial mode function
			xi_th = np.cos(2*pi*rad/20.) #this is a trial polodial mode function
			xi_ph = np.cos(2*pi*rad/40.) #this is a trial azimuthal mode function

			for pt in ta:

				vr[pr]

				thta = tu[pt]
				vr[pr][pt]['test'][0]  = xi_r *real(sph_harm(0,l_r, 0.,thta))
				vth[pr][pt]['test'][0] = xi_th*real(dsph_harm( l_th,   thta))
				vph[pr][pt]['test'][0] = xi_ph*real(dsph_harm( l_ph,   thta))
		else:

			vr[pr]  = pickle.load(open( './'+datadir+'/velr_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
			vth[pr] = pickle.load(open('./'+datadir+'/velth_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
			if r!='0.0':
				vph[pr] = pickle.load(open(  './'+datadir+'/velph_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))

	if mass_weighted=='yes':
	
		rhospl_in_time = {}

		rho = pickle.load(open('./'+datadir+'/rho.dic','rb')) #[r], and has shape(number of times, number of radii*number of angles.
							#for a given time ti, [ti,:number of radii] has the radial profile along
							#the first angle, theta=0. Then theta increases all the way to pi.
		rho = rho[r]

		toriginal=pickle.load(open('./'+datadir+'/tt.dic','rb')) #The original time array. Same length as rho (along the time axis).

		toriginal=toriginal[r]*1e3

		for pr in ra:
			rhospl_in_time[pr] = {}
			for pt in ta:
				rhospl_in_time[pr][pt] = interp1d(toriginal,rho[:,len(ra)*pt+pr],fill_value='extrapolate')

elif firstcall=='no':
	print 'On subsequent call of decomposition script, I/O skipped.'

### Perform decomposition

Er  = {} #Dictionaries to hold the radial coefficients
Eth = {}
Eph = {}

for m in modes:

	Er[m]  = {}
	Eth[m] = {}
	Eph[m] = {}

	for l in poloidal_numbers:

		Er[m][l]  = []
		Eth[m][l] = []
		Eph[m][l] = []

		for pr in ra:
			rad=ru[pr]
			#Integrate over solid angles assuming axisymmetry

			vrintme = np.zeros(len(tu)) #Collect values along constant radius into an array
			for pt in ta:
				if mass_weighted=='yes':
					vrintme[pt] = vr[pr][pt][m][ti] * rhospl_in_time[pr][pt](t[r][ti])**mass_weight
				else:
					vrintme[pt] = vr[pr][pt][m][ti]

			Er[m][l].append(  2*pi * np.trapz(  vrintme *  real(sph_harm(0,l,0.,tu)) * np.sin(tu), dx=tu[1]-tu[0] ) )

			if l==0: #If l==0 need to do special case, otherwise dividing by 0
				Eth[m][l].append(0.)
				Eph[m][l].append(0.)
			else:

				vthintme = np.zeros(len(tu)) #Collect values along constant radius into an array
				for pt in ta:
					if mass_weighted=='yes':
						vthintme[pt] = vth[pr][pt][m][ti] * rhospl_in_time[pr][pt](t[r][ti])**mass_weight
					else:
						vthintme[pt] = vth[pr][pt][m][ti]

				Eth[m][l].append( ( 1./(l*(l+1.)) ) * 2*pi * np.trapz( vthintme * real(dsph_harm(  l,   tu)) * np.sin(tu), dx=tu[1]-tu[0] ) )
				if r!='0.0':
					vphintme = np.zeros(len(tu)) #Collect values along constant radius into a list
					for pt in ta:
						if mass_weighted=='yes':
							vphintme[pt] = vph[pr][pt][m][ti] * rhospl_in_time[pr][pt](t[r][ti])**mass_weight
						else:
							vphintme[pt] = vph[pr][pt][m][ti]

					Eph[m][l].append( ( 1./(l*(l+1.)) ) * 2*pi * np.trapz( vphintme * real(dsph_harm(  l,   tu)) * np.sin(tu), dx=tu[1]-tu[0] ) )

		#Turn into numpy arrays
		Er[m][l]  = np.array( Er[m][l])
		Eth[m][l] = np.array(Eth[m][l])
		if r!='0.0':
			Eph[m][l] = np.array(Eph[m][l])

'''
pickle.dump(Er, open( 'vr_sph_harm_coeffs_rot'+r+'.dic','wb'))
pickle.dump(Eth,open('vth_sph_harm_coeffs_rot'+r+'.dic','wb'))
if r!='0.0':
	pickle.dump(Eph,open('vph_sph_harm_coeffs_rot'+r+'.dic','wb'))
'''

