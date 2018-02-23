from numpy import *
from matplotlib import *
import numpy
from scipy.signal import istft

execfile('./pars_velocity.py')
'''
xx            = pickle.load(open(           'xx.dic','rb'))*1e-5 #Convert to km
yy            = pickle.load(open(           'yy.dic','rb'))*1e-5 #Convert to km
rr            = pickle.load(open(           'rr.dic','rb'))*1e-5 #Convert to km
theta         = pickle.load(open(        'theta.dic','rb'))

velxspecf     = pickle.load(open(    'velxspecf_complex.dic','rb'))
velyspecf     = pickle.load(open(    'velyspecf_complex.dic','rb'))
velrspecf     = pickle.load(open(    'velrspecf_complex.dic','rb'))
velthetaspecf = pickle.load(open('velthetaspecf_complex.dic','rb'))

velxspect     = pickle.load(open(    'velxspect_complex.dic','rb'))
velyspect     = pickle.load(open(    'velyspect_complex.dic','rb'))
velrspect     = pickle.load(open(    'velrspect_complex.dic','rb'))
velthetaspect = pickle.load(open('velthetaspect_complex.dic','rb'))
'''
#velxspec      = pickle.load(open(     'velxspec_complex.dic','rb'))
#velyspec      = pickle.load(open(     'velyspec_complex.dic','rb'))
'''
velrspec      = pickle.load(open(     'velrspec_complex.dic','rb'))
velthetaspec  = pickle.load(open( 'velthetaspec_complex.dic','rb'))

masks         = pickle.load(open('velocity_spectrogram_masks.dic','rb'))
'''
dt = 0.1*1e-3 #time resolution for velocity field

################### CHECK whether this stuff is the same as when you *computed* the spectrograms.
Nperseg  = int(WindowWidth*1e-3/dt)
Noverlap = Nperseg-1
Nfft     = None

### Just multiply them. Do not dump again (files are large, and we're considering way too many modes).

vr  = {} #Initialize time-domain filtered velocity dictionaries
vth = {}
t   = {}

for r in rotrates_to_filter: #rotrates:

	vr[r]  = {}
	vth[r] = {}

	modes = masks[r].keys() #Get mode keys

	points = velrspec[r].keys() #Get point keys

	### Filter, then invert spectrogram

	for p in points: #Loops over points

		vr[r][p]  = {}
		vth[r][p] = {}

		tempr  =     velrspec[r][p]
		tempth = velthetaspec[r][p]

		for m in modes: #Loops over modes
			print 'Computing rotation rate '+r+', point '+str(p)+', mode '+m+' .'
			t[r],  vr[r][p][m] = istft(    velrspec[r][p]*masks[r][m], fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=True)
			t[r], vth[r][p][m] = istft(velthetaspec[r][p]*masks[r][m], fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=True)

pickle.dump( t,  open(    't_filtered.dic','wb'))
pickle.dump(vr,  open( 'velr_filtered.dic','wb'))
pickle.dump(vth, open('velth_filtered.dic','wb'))
