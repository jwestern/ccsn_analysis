import pickle
from numpy import *
from scipy.signal import spectrogram

#Define parameters
execfile('./pars_velocity.py')

#Load in data
t        = pickle.load(open(      'tt.dic','rb'))
#velx     = pickle.load(open(    'velx.dic','rb'))
#vely     = pickle.load(open(    'vely.dic','rb'))
velr     = pickle.load(open(    'velr.dic','rb'))
veltheta = pickle.load(open('veltheta.dic','rb'))

#Define number of points in the star we have
numpoints = shape(velr[rotrates[0]])[1]
points = range(numpoints)

#Define dt for each rotation case
dt = {}
for rot in rotrates:
	dt[rot] = 0.1*1e-3 #0.1 milliseconds

#Initialize some dictionaries for holding parameters for spectrogram function
Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap
Nfft     = {} #Number of points to perform FFT over (>= Nperseg, if greater then it is equivalent to sinc interpolation (no extra "real" resolution))

#Define parameters for spectrogram function
for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-1
	Nfft[r]     = None

#Compute spectrograms
'''
velxspecf      = {}
velxspect      = {}
velxspec       = {}

velyspecf      = {}
velyspect      = {}
velyspec       = {}
'''
velrspecf      = {}
velrspect      = {}
velrspec       = {}

velthetaspecf  = {}
velthetaspect  = {}
velthetaspec   = {}

for r in rotrates:
	'''
	velxspecf[r]     = {}
	velxspect[r]     = {}
	velxspec[r]      = {}

	velyspecf[r]     = {}
	velyspect[r]     = {}
	velyspec[r]      = {}
	'''
	velrspecf[r]     = {}
	velrspect[r]     = {}
	velrspec[r]      = {}

	velthetaspecf[r] = {}
	velthetaspect[r] = {}
	velthetaspec[r]  = {}

for r in rotrates:
	for p in points:
		'''
		velxspecf[r][p],         velxspect[r][p],     velxspec[r][p] = spectrogram(    velx[r][:,p],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling, mode=Mode)
		velyspecf[r][p],         velyspect[r][p],     velyspec[r][p] = spectrogram(    vely[r][:,p],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling, mode=Mode)
		'''
		velrspecf[r][p],         velrspect[r][p],     velrspec[r][p] = spectrogram(    velr[r][:,p],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling, mode=Mode)
		velthetaspecf[r][p], velthetaspect[r][p], velthetaspec[r][p] = spectrogram(veltheta[r][:,p],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling, mode=Mode)

#Shift times so that bounce time = 0
for r in rotrates:
	for p in points:
		'''
		velxspect[r][p]     =     velxspect[r][p] -     velxspect[r][p].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
		velyspect[r][p]     =     velyspect[r][p] -     velyspect[r][p].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
		'''
		velrspect[r][p]     =     velrspect[r][p] -     velrspect[r][p].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
		velthetaspect[r][p] = velthetaspect[r][p] - velthetaspect[r][p].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)

#		                            ^ brings min to 0        ^ brings min to the min of original times, but only to within half the overlap time (since missing that chunk).

#Define integrated spectra, for later normalizing the cross-spectra
'''
velxspecint     = {}
velyspecint     = {}
'''
velrspecint     = {}
velthetaspecint = {}

for r in rotrates:
	'''
	velxspecint[r]     = {}
	velyspecint[r]     = {}
	'''
	velrspecint[r]     = {}
	velthetaspecint[r] = {}

for r in rotrates:
	for p in points:
		'''
		velxspecint[r][p]     = np.trapz(    velxspec[r][p],dx=     velxspecf[r][p][1] -     velxspecf[r][p][0],axis=0)
		velyspecint[r][p]     = np.trapz(    velyspec[r][p],dx=     velyspecf[r][p][1] -     velyspecf[r][p][0],axis=0)
		'''
		velrspecint[r][p]     = np.trapz(    velrspec[r][p],dx=     velrspecf[r][p][1] -     velrspecf[r][p][0],axis=0)
		velthetaspecint[r][p] = np.trapz(velthetaspec[r][p],dx= velthetaspecf[r][p][1] - velthetaspecf[r][p][0],axis=0)
'''
pickle.dump(    velxspecf,open(    'velxspecf_'+Mode+'.dic','wb'))
pickle.dump(    velyspecf,open(    'velyspecf_'+Mode+'.dic','wb'))
'''
pickle.dump(    velrspecf,open(    'velrspecf_'+Mode+'.dic','wb'))
pickle.dump(velthetaspecf,open('velthetaspecf_'+Mode+'.dic','wb'))
'''
pickle.dump(    velxspect,open(    'velxspect_'+Mode+'.dic','wb'))
pickle.dump(    velyspect,open(    'velyspect_'+Mode+'.dic','wb'))
'''
pickle.dump(    velrspect,open(    'velrspect_'+Mode+'.dic','wb'))
pickle.dump(velthetaspect,open('velthetaspect_'+Mode+'.dic','wb'))
'''
pickle.dump(    velxspec,open(    'velxspec_'+Mode+'.dic','wb'))
pickle.dump(    velyspec,open(    'velyspec_'+Mode+'.dic','wb'))
'''
pickle.dump(    velrspec,open(    'velrspec_'+Mode+'.dic','wb'))
pickle.dump(velthetaspec,open('velthetaspec_'+Mode+'.dic','wb'))
'''
pickle.dump(    velxspecint,open(    'velxspecint_'+Mode+'.dic','wb'))
pickle.dump(    velyspecint,open(    'velyspecint_'+Mode+'.dic','wb'))
'''
pickle.dump(    velrspecint,open(    'velrspecint_'+Mode+'.dic','wb'))
pickle.dump(velthetaspecint,open('velthetaspecint_'+Mode+'.dic','wb'))
