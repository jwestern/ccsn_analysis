from numpy import *
import scipy.signal as ss

execfile('./pars.py')
print 'Loading files now'
t     = pickle.load(open(    't.dic','rb'))
gwc   = pickle.load(open(  'gwc.dic','rb'))
anuec = pickle.load(open('anuec.dic','rb'))
nuxc  = pickle.load(open( 'nuxc.dic','rb'))
nuec  = pickle.load(open( 'nuec.dic','rb'))
dt    = pickle.load(open(   'dt.dic','rb'))

#Shorten spectrogram parameter
WW=WindowWidth


Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap
Nfft     = {} #Number of points to perform FFT over (>= Nperseg, if greater then it is equivalent to sinc interpolation (no extra "real" resolution))

for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-1
	Nfft[r]     = None


#Compute spectrograms
gw_anue_cohspec  = {}
gw_nux_cohspec   = {}
gw_nue_cohspec   = {}
anue_nux_cohspec = {}
anue_nue_cohspec = {}
nue_nux_cohspec  = {}
print 'Pre-defining arrays now'
#Pre-define the cross spectrum arrays
howmanytimes = {}
howmanyfreqs = {}
beginhere    = {}
freqs_cspec  = {}
times_cspec  = {}
for r in rotrates:
	howmanytimes[r]        = (len(gwc[r])-int(WindowWidth*1e-3/dt[r])-1)/2
	howmanyfreqs[r]        = Nperseg[r]/2+1
	gw_anue_cohspec[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nux_cohspec[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nue_cohspec[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nux_cohspec[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nue_cohspec[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	nue_nux_cohspec[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	beginhere[r]           = Nperseg[r]/2+1
	if mod(Nperseg[r],2)==0:
		times_cspec[r] = t[r][beginhere[r]:-beginhere[r]+1]
	else:
		times_cspec[r] = t[r][beginhere[r]:-beginhere[r]  ]
print 'Computing coherence spectrograms now'
for r in rotrates:
	bh = beginhere[r]
	getfreqs = 'yes'
	for time in range(howmanytimes[r]):
		bup = ss.coherence(  gwc[r][time:time+Nperseg[r]], anuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		gw_anue_cohspec[r][:,time]  = bup[1]
		bup = ss.coherence(  gwc[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		gw_nux_cohspec[r][:,time]   = bup[1]
		bup = ss.coherence(  gwc[r][time:time+Nperseg[r]],  nuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		gw_nue_cohspec[r][:,time]   = bup[1]
		bup = ss.coherence(anuec[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		anue_nux_cohspec[r][:,time] = bup[1]
		bup = ss.coherence(anuec[r][time:time+Nperseg[r]],  nuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		anue_nue_cohspec[r][:,time] = bup[1]
		bup = ss.coherence( nuec[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r]/2,noverlap=Nperseg[r]/2-1,nfft=Nfft[r])
		nue_nux_cohspec[r][:,time]  = bup[1]
		if getfreqs=='yes':
			freqs_cspec[r] = bup[0]
			getfreqs = 'no'
print 'Dumping files now'
pickle.dump( gw_anue_cohspec,open( 'gw_anue_cohspec.dic','wb'))
pickle.dump(  gw_nux_cohspec,open(  'gw_nux_cohspec.dic','wb'))
pickle.dump(  gw_nue_cohspec,open(  'gw_nue_cohspec.dic','wb'))
pickle.dump(anue_nux_cohspec,open('anue_nux_cohspec.dic','wb'))
pickle.dump(anue_nue_cohspec,open('anue_nue_cohspec.dic','wb'))
pickle.dump( nue_nux_cohspec,open( 'nue_nux_cohspec.dic','wb'))
pickle.dump(     times_cspec,open(        'times_cspec.dic','wb'))
pickle.dump(     freqs_cspec,open(        'freqs_cspec.dic','wb'))
