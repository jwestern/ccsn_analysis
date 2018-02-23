import numpy as np
import pickle
from scipy.signal import get_window

#Get parameters, Window and WindowWidth in particular
execfile('pars.py')

dt    = pickle.load(open(   'dt.dic','rb'))

#Get signal
s = pickle.load(open(  'gwc.dic','rb'))

Ns = {}
for r in rotrates:
	Ns[r] = len(s[r])

#Initialize some dictionaries for holding parameters for spectrogram function
Nperseg  = {} #Number of points over which window is non-zero
Noverlap = {} #Number of points successive windows overlap

#Define parameters for spectrogram function
for r in rotrates:
	Nperseg[r]  = int(WindowWidth*1e-3/dt[r])
	Noverlap[r] = Nperseg[r]-1

#Create windows
W = {}

for r in rotrates:
	W[r] = get_window(Window,Nperseg[r])
'''
#Define points of array to iterate over, each time multiplying the signal by the window
points_to_iterate_over = {}

for r in rotrates:
	if (Nperseg[r] % 2) == 0: #Check if even
		points_to_iterate_over[r] = range(Nperseg[r]/2,Ns[r]-1-Nperseg[r]/2+1) #Check these definitions with examples of small window lengths
	else:
		points_to_iterate_over[r] = range(Nperseg[r]/2,Ns[r]-1-Nperseg[r]/2  )

first='yes'
for i in points_to_iterate_over['0.0'][0:10]:

	#Multiply signal with window, making stemp the same length as the window (no zero padding -> no sinc interpolation & faster fft)
	if (Nperseg['0.0'] % 2) == 0: #Check if even
		stemp = s['0.0'][i-Nperseg['0.0']/2:i+Nperseg['0.0']/2  ]*W['0.0']   #*np.concatenate(( np.zeros(i-Nperseg[r]/2),W['0.0'],np.zeros(Ns['0.0']-Nperseg['0.0']/2-i-1) ))
	else:
		stemp = s['0.0'][i-Nperseg['0.0']/2:i+Nperseg['0.0']/2+1]*W['0.0']   #*np.concatenate(( np.zeros(i-Nperseg[r]/2),W['0.0'],np.zeros(Ns['0.0']-Nperseg['0.0']/2-i-1) ))

	if first=='yes':
		shat_temp = np.fft.rfft(stemp)
		nn = len(shat_temp)
		spec = np.zeros(( nn, len(points_to_iterate_over['0.0']) ))*(1.+1j)
		spec[:,0] = shat_temp
		first='no'
	else:
		spec[:,i-Nperseg['0.0']/2] = np.fft.rfft(stemp)
'''
