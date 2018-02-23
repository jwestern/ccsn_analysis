from numpy import *
from scipy.signal import spectrogram

execfile('./pars.py')

t     = pickle.load(open(    't.dic','rb'))
gwc   = pickle.load(open(  'gwc.dic','rb'))
anuec = pickle.load(open('anuec.dic','rb'))
nuxc  = pickle.load(open( 'nuxc.dic','rb'))
nuec  = pickle.load(open( 'nuec.dic','rb'))
dt    = pickle.load(open(   'dt.dic','rb'))

Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap
Nfft     = {} #Number of points to perform FFT over (>= Nperseg, if greater then it is equivalent to sinc interpolation (no extra "real" resolution))
for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-1
	Nfft[r]     = None

#Compute spectrograms
gwspecf   = {}
gwspect   = {}
gwspec    = {}

anuespecf = {}
anuespect = {}
anuespec  = {}

nuxspecf  = {}
nuxspect  = {}
nuxspec   = {}

nuespecf  = {}
nuespect  = {}
nuespec   = {}

for r in rotrates:
	gwspecf[r],     gwspect[r],   gwspec[r] = spectrogram(  gwc[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling,mode=Mode)
	anuespecf[r], anuespect[r], anuespec[r] = spectrogram(anuec[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling,mode=Mode)
	nuxspecf[r],   nuxspect[r],  nuxspec[r] = spectrogram( nuxc[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling,mode=Mode)
	nuespecf[r],   nuespect[r],  nuespec[r] = spectrogram( nuec[r],1/dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling,mode=Mode)

#Shift times so that bounce time = 0
for r in rotrates:
	gwspect[r]   =   gwspect[r] -   gwspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	anuespect[r] = anuespect[r] - anuespect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	nuxspect[r]  =  nuxspect[r] -  nuxspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	nuespect[r]  =  nuespect[r] -  nuespect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)

#		                      ^ brings min to 0    ^ brings min to the min of original times, but only to within half the overlap time (since missing that chunk).

#Define integrated spectra, for later normalizing the cross-spectra
gwspecint   = {}
anuespecint = {}
nuxspecint  = {}
nuespecint  = {}

for r in rotrates:
	gwspecint[r]   = np.trapz(  gwspec[r],dx=  gwspecf[r][1]-  gwspecf[r][0],axis=0)
	anuespecint[r] = np.trapz(anuespec[r],dx=anuespecf[r][1]-anuespecf[r][0],axis=0)
	nuxspecint[r]  = np.trapz( nuxspec[r],dx= nuxspecf[r][1]- nuxspecf[r][0],axis=0)
	nuespecint[r]  = np.trapz( nuespec[r],dx= nuespecf[r][1]- nuespecf[r][0],axis=0)

pickle.dump(  gwspecf,open(  'gwspecf.dic','wb'))
pickle.dump(anuespecf,open('anuespecf.dic','wb'))
pickle.dump( nuxspecf,open( 'nuxspecf.dic','wb'))
pickle.dump( nuespecf,open( 'nuespecf.dic','wb'))

pickle.dump(  gwspect,open(  'gwspect.dic','wb'))
pickle.dump(anuespect,open('anuespect.dic','wb'))
pickle.dump( nuxspect,open( 'nuxspect.dic','wb'))
pickle.dump( nuespect,open( 'nuespect.dic','wb'))

pickle.dump(  gwspec,open(  'gwspec.dic','wb'))
pickle.dump(anuespec,open('anuespec.dic','wb'))
pickle.dump( nuxspec,open( 'nuxspec.dic','wb'))
pickle.dump( nuespec,open( 'nuespec.dic','wb'))

pickle.dump(  gwspecint,open(  'gwspecint.dic','wb'))
pickle.dump(anuespecint,open('anuespecint.dic','wb'))
pickle.dump( nuxspecint,open( 'nuxspecint.dic','wb'))
pickle.dump( nuespecint,open( 'nuespecint.dic','wb'))
