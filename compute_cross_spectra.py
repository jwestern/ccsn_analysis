from numpy import *
from scipy.signal import spectrogram
from scipy.signal import csd

#execfile('./read_in_data2.py')

#Define spectrogram parameters in physical units
WindowWidth = 35 #in Hz

#Define spectrogram parameters
Window = 'bohman'
Scaling = 'spectrum'

Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap
Nfft     = {} #Number of points to perform FFT over (>= Nperseg, if greater then it is equivalent to sinc interpolation (no extra "real" resolution))
for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-1
	Nfft[r]     = None

startfrom=31500

#Compute spectrograms
gw_anue_csd  = {}
gw_nux_csd   = {}
anue_nux_csd = {}

for r in rotrates:
	gw_anue_csd[r]  = csd(gwc[r][startfrom:], anuec[r][startfrom:],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)
	gw_nux_csd[r]   = csd(gwc[r][startfrom:],  nuxc[r][startfrom:],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)
	anue_nux_csd[r] = csd(anuec[r][startfrom:],nuxc[r][startfrom:],fs=1./dt[r],window=(Window),nperseg=Nperseg[r],noverlap=Noverlap[r],nfft=Nfft[r],scaling=Scaling)

#Shift times so that bounce time = 0
'''
for r in rotrates:
	gwspect[r]   =   gwspect[r] -   gwspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	anuespect[r] = anuespect[r] - anuespect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)
	nuxspect[r]  =  nuxspect[r] -  nuxspect[r].min() + (t[r][0] + Noverlap[r]*dt[r]/2.)

#		                      ^ brings min to 0    ^ brings min to the min of original times, but only to within half the overlap time (since missing that chunk).

'''

