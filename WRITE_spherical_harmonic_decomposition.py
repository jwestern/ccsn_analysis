from numpy import *
from matplotlib import *
import numpy
from scipy.special import sph_harm
from scipy.interpolate import SmoothBivariateSpline

execfile('./pars_velocity.py')

#xx       = pickle.load(open(           'xx.dic','rb'))*1e-5 #Convert to km
#yy       = pickle.load(open(           'yy.dic','rb'))*1e-5 #Convert to km
rr       = pickle.load(open(            'rr.dic','rb'))*1e-5 #Convert to km
theta    = pickle.load(open(         'theta.dic','rb'))

rr       = np.round(rr,9) #Round to 9 decimal places, so we can accurately count how many unique values there are
theta    = np.round(theta,9)

t        = pickle.load(open(    't_filtered.dic','rb')) #[rotrates_to_filter], chosen in parameter file
vr       = pickle.load(open( 'velr_filtered.dic','rb')) #[rotrates_to_filter][points][modes], see spectrogram_filter.py
vth      = pickle.load(open('velth_filtered.dic','rb')) #Same as above.
vph      = vth #Change to velphi once you have that data.

masks    = pickle.load(open('velocity_spectrogram_masks.dic','rb')) #Just to get keys from

dt = 0.1*1e-3 #time resolution for velocity field
ti = 560 #time index to analyze
r  = rotrate_to_decompose

modes  = masks[r].keys() #Get mode keys
#points = range(len(rr)) #Get point keys
radii  = np.unique(rr)
thetas = np.unique(theta)

### Define vector spherical harmonic derivative w/ resp to theta

def dsph_harm(l,theta): #(d/dtheta) Y_lm... We use phi=m=0 since we're in axisymmetry and it doesn't matter
	m=0
	return sqrt( (l-m)*(l+m+1) ) * sph_harm(m+1,l,0.,theta)

### Repackage velocity data, for feeding into splines

vrre  = {} #Repackaged velocity dictionaries
vthre = {}
vphre = {}

for m in modes: #Loop over modes for this particular rotation case

	vrre[m]  = [] #Define a list for each mode
	vthre[m] = []
	vphre[m] = []
	points   = vr[r].keys() #Get point keys

	for p in points: #Put each point's data into the lists

		vrre[m].append(  vr[r][p][m][ti])
		vthre[m].append(vth[r][p][m][ti])
		vphre[m].append(vph[r][p][m][ti])

	vrre[m]  = np.array( vrre[m]) #Turn lists into numpy arrays
	vthre[m] = np.array(vthre[m])
	vphre[m] = np.array(vphre[m])

### Define 2d splines of velocity field

vrsp  = {} #Spline dictionaries, keys will be mode frequency names
vthsp = {}
vphsp = {}

for m in modes: #Loop over modes for this particular rotation case

	vrsp[m]  = SmoothBivariateSpline(rr,theta, vrre[m])
	vthsp[m] = SmoothBivariateSpline(rr,theta,vthre[m])
	vphsp[m] = SmoothBivariateSpline(rr,theta,vphre[m])

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

		for rad in radii:
			#Integrate over solid angles assuming axisymmetry
			Er[m][l].append(  2*pi * np.trapz(  vrsp[m](rad,thetas) *  real(sph_harm(0,l,0.,thetas)) * np.sin(thetas), dx=thetas[1]-thetas[0] ) )

			if l==0: #If l==0 need to do special case, otherwise dividing by 0
				Eth[m][l].append(0.)
				Eph[m][l].append(0.)
			else:
				Eth[m][l].append( ( 1./(l*(l+1.)) ) * 2*pi * np.trapz( vthsp[m](rad,thetas) * real(dsph_harm(  l,   thetas)) * np.sin(thetas), dx=thetas[1]-thetas[0] ) )
				Eph[m][l].append( ( 1./(l*(l+1.)) ) * 2*pi * np.trapz( vphsp[m](rad,thetas) * real(dsph_harm(  l,   thetas)) * np.sin(thetas), dx=thetas[1]-thetas[0] ) )
		#Turn into numpy arrays
		Er[m][l]  = np.array( Er[m][l])
		Eth[m][l] = np.array(Eth[m][l])
		Eph[m][l] = np.array(Eph[m][l])

