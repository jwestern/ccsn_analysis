from numpy import *
from scipy.signal import spectrogram
from scipy.signal import csd

execfile('./pars.py')

print 'Reading in data'
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

print 'Pre-defining arrays'
#Compute spectrograms
gw_anue_cspec_real  = {}
gw_anue_cspec_imag  = {}
gw_nux_cspec_real   = {}
gw_nux_cspec_imag   = {}
gw_nue_cspec_real   = {}
gw_nue_cspec_imag   = {}
anue_nux_cspec_real = {}
anue_nux_cspec_imag = {}
anue_nue_cspec_real = {}
anue_nue_cspec_imag = {}
nue_nux_cspec_real  = {}
nue_nux_cspec_imag  = {}

#Pre-define the cross spectrum arrays
howmanytimes = {}
howmanyfreqs = {}
beginhere    = {}
freqs_cspec  = {}
times_cspec  = {}
for r in rotrates:
	howmanytimes[r]        = len(gwc[r])-int(WindowWidth*1e-3/dt[r])-1
	howmanyfreqs[r]        = Nperseg[r]/2+1
	gw_anue_cspec_real[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nux_cspec_real[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nue_cspec_real[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nux_cspec_real[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nue_cspec_real[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	nue_nux_cspec_real[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_anue_cspec_imag[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nux_cspec_imag[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nux_cspec_imag[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	gw_nue_cspec_imag[r]   = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nux_cspec_imag[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	anue_nue_cspec_imag[r] = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	nue_nux_cspec_imag[r]  = np.zeros((howmanyfreqs[r],howmanytimes[r]))
	beginhere[r]           = Nperseg[r]/2+1
	if mod(Nperseg[r],2)==0:
		times_cspec[r] = t[r][beginhere[r]:-beginhere[r]+1]
	else:
		times_cspec[r] = t[r][beginhere[r]:-beginhere[r]  ]

print 'Computing cross spectrograms'
for r in rotrates:
	bh = beginhere[r]
	getfreqs = 'yes'
	for time in range(howmanytimes[r]):
		bup = csd(  gwc[r][time:time+Nperseg[r]], anuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		gw_anue_cspec_real[r][:,time]  = real(bup[1])
		gw_anue_cspec_imag[r][:,time]  = imag(bup[1])
		bup = csd(  gwc[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		gw_nux_cspec_real[r][:,time]   = real(bup[1])
		gw_nux_cspec_imag[r][:,time]   = imag(bup[1])
		bup = csd(  gwc[r][time:time+Nperseg[r]],  nuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		gw_nue_cspec_real[r][:,time]   = real(bup[1])
		gw_nue_cspec_imag[r][:,time]   = imag(bup[1])
		bup = csd(anuec[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		anue_nux_cspec_real[r][:,time] = real(bup[1])
		anue_nux_cspec_imag[r][:,time] = imag(bup[1])
		bup = csd(anuec[r][time:time+Nperseg[r]],  nuec[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		anue_nue_cspec_real[r][:,time] = real(bup[1])
		anue_nue_cspec_imag[r][:,time] = imag(bup[1])
		bup = csd(nuec[r][time:time+Nperseg[r]],  nuxc[r][time:time+Nperseg[r]],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=0,nfft=Nfft[r],scaling=Scaling)
		nue_nux_cspec_real[r][:,time]  = real(bup[1])
		nue_nux_cspec_imag[r][:,time]  = imag(bup[1])
		if getfreqs=='yes':
			freqs_cspec[r] = bup[0]
			getfreqs = 'no'

print 'Dumping cross spectrograms to file'
pickle.dump( gw_anue_cspec_real,open( 'gw_anue_cspec_real.dic','wb'))
pickle.dump( gw_anue_cspec_imag,open( 'gw_anue_cspec_imag.dic','wb'))
pickle.dump(  gw_nux_cspec_real,open(  'gw_nux_cspec_real.dic','wb'))
pickle.dump(  gw_nux_cspec_imag,open(  'gw_nux_cspec_imag.dic','wb'))
pickle.dump(  gw_nue_cspec_real,open(  'gw_nue_cspec_real.dic','wb'))
pickle.dump(  gw_nue_cspec_imag,open(  'gw_nue_cspec_imag.dic','wb'))
pickle.dump(anue_nux_cspec_real,open('anue_nux_cspec_real.dic','wb'))
pickle.dump(anue_nux_cspec_imag,open('anue_nux_cspec_imag.dic','wb'))
pickle.dump(anue_nue_cspec_real,open('anue_nue_cspec_real.dic','wb'))
pickle.dump(anue_nue_cspec_imag,open('anue_nue_cspec_imag.dic','wb'))
pickle.dump( nue_nux_cspec_real,open( 'nue_nux_cspec_real.dic','wb'))
pickle.dump( nue_nux_cspec_imag,open( 'nue_nux_cspec_imag.dic','wb'))
pickle.dump(        times_cspec,open(        'times_cspec.dic','wb'))
pickle.dump(        freqs_cspec,open(        'freqs_cspec.dic','wb'))
