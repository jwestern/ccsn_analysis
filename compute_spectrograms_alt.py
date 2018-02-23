from numpy import *
from scipy.signal import spectrogram

execfile('./pars_alt.py')

t     = pickle.load(open(     't.dic','rb'))
rhoc  = pickle.load(open(  'rhoc.dic','rb'))
Rpnsc = pickle.load(open( 'Rpnsc.dic','rb'))
Tpnsc = pickle.load(open( 'Tpnsc.dic','rb'))
dt    = pickle.load(open(    'dt.dic','rb'))

Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap
Nfft     = {} #Number of points to perform FFT over (>= Nperseg, if greater then it is equivalent to sinc interpolation (no extra "real" resolution))
for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-100
	Nfft[r]     = None

#Compute spectrograms
rhospecf   = {}
rhospect   = {}
rhospec    = {}

Rpnsspecf = {}
Rpnsspect = {}
Rpnsspec  = {}

Tpnsspecf  = {}
Tpnsspect  = {}
Tpnsspec   = {}

for r in rotrates:
	rhospecf[r],   rhospect[r],  rhospec[r] = spectrogram( rhoc[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)
	Rpnsspecf[r], Rpnsspect[r], Rpnsspec[r] = spectrogram(Rpnsc[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)
	Tpnsspecf[r], Tpnsspect[r], Tpnsspec[r] = spectrogram(Tpnsc[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)

#Shift times so that bounce time = 0
for r in rotrates:
	rhospect[r]  =  rhospect[r] -  rhospect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	Rpnsspect[r] = Rpnsspect[r] - Rpnsspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	Tpnsspect[r] = Tpnsspect[r] - Tpnsspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)

#		                      ^ brings min to 0    ^ brings min to the min of original times, but only to within half the overlap time (since missing that chunk).

#Define integrated spectra, for later normalizing the cross-spectra
rhospecint   = {}
Rpnsspecint  = {}
Tpnsspecint  = {}

for r in rotrates:
	rhospecint[r]   = np.trapz(  rhospec[r],dx=  rhospecf[r][1]-  rhospecf[r][0],axis=0)
	Rpnsspecint[r]  = np.trapz( Rpnsspec[r],dx= Rpnsspecf[r][1]- Rpnsspecf[r][0],axis=0)
	Tpnsspecint[r]  = np.trapz( Tpnsspec[r],dx= Tpnsspecf[r][1]- Tpnsspecf[r][0],axis=0)

pickle.dump(  rhospecf,open(  'rhospecf.dic','wb'))
pickle.dump( Rpnsspecf,open( 'Rpnsspecf.dic','wb'))
pickle.dump( Tpnsspecf,open( 'Tpnsspecf.dic','wb'))

pickle.dump(  rhospect,open(  'rhospect.dic','wb'))
pickle.dump( Rpnsspect,open( 'Rpnsspect.dic','wb'))
pickle.dump( Tpnsspect,open( 'Tpnsspect.dic','wb'))

pickle.dump(  rhospec,open(  'rhospec.dic','wb'))
pickle.dump( Rpnsspec,open( 'Rpnsspec.dic','wb'))
pickle.dump( Tpnsspec,open( 'Tpnsspec.dic','wb'))

pickle.dump(  rhospecint,open(  'rhospecint.dic','wb'))
pickle.dump( Rpnsspecint,open( 'Rpnsspecint.dic','wb'))
pickle.dump( Tpnsspecint,open( 'Tpnsspecint.dic','wb'))
