from numpy import *
from matplotlib import *
import numpy as np
from scipy.signal import istft
import pickle

execfile('./pars_velocity.py')

rr            = pickle.load(open(           './'+datadir+'/rr.dic','rb'))*1e-5 #Convert to km
theta         = pickle.load(open(        './'+datadir+'/theta.dic','rb'))

#Get unique coordinate values
ru = np.unique(np.round(   rr,9)) #Get unique vals of rr
tu = np.unique(np.round(theta,9)) #Get unique vals of theta

#Get addresses of all unique values... We will filter every single point
ra = range(len(ru))
ta = range(len(tu))

masks = pickle.load(open('./'+datadir+'/velocity_spectrogram_masks_tightenfactor'+str(tighten_factor)+'.dic','rb'))

dt = 0.1*1e-3 #time resolution for velocity field

################### CHECK whether this stuff is the same as when you *computed* the spectrograms.
Nperseg  = int(WindowWidth*1e-3/dt)
Noverlap = Nperseg-1
Nfft     = None

### Just multiply them. Do not dump again (files are large, and we're considering way too many modes).

vr  = {} #Initialize time-domain filtered velocity dictionaries
vth = {}
vph = {}
t   = {}

for r in rotrates_to_filter: #rotrates:

	modes = masks[r].keys() #Get mode keys
	modes.append('unfiltered') #Add an unfiltered case

	for pr in ra: #Loop over radii

		velrspec     = pickle.load(open(    './'+datadir+'/velrspec_complex_rot'+r+'_r'+str(pr)+'.dic','rb'))
		velthetaspec = pickle.load(open('./'+datadir+'/velthetaspec_complex_rot'+r+'_r'+str(pr)+'.dic','rb'))
		if r!='0.0':
			velphispec   = pickle.load(open(  './'+datadir+'/velphispec_complex_rot'+r+'_r'+str(pr)+'.dic','rb'))

		for pt in ta: #Loop over angles

			### Filter, then invert spectrogram

			vr[pt]  = {}
			vth[pt] = {}
			if r!='0.0':
				vph[pt] = {}

			tempr  =     velrspec[pt]
			tempth = velthetaspec[pt]
			if r!='0.0':
				tempph =   velphispec[pt]

			for m in modes: #Loops over modes
				print 'Computing rotation rate '+r+', radius '+str(ru[pr])+' km, angle '+str(tu[pt])+' rad, mode '+m+' Hz.'
				if m=='unfiltered': #Do not apply any mask													  #vvv must be False, otherwise doesn't reproduce the same length of time as the 
					t[r],  vr[pt][m] = istft(    velrspec[pt]            , fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
					t[r], vth[pt][m] = istft(velthetaspec[pt]            , fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
					if r!='0.0':
						t[r], vph[pt][m] = istft(  velphispec[pt]            , fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
				else:
					t[r],  vr[pt][m] = istft(    velrspec[pt]*masks[r][m], fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
					t[r], vth[pt][m] = istft(velthetaspec[pt]*masks[r][m], fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
					if r!='0.0':
						t[r], vph[pt][m] = istft(  velphispec[pt]*masks[r][m], fs=1./dt, window=(Window), nperseg=Nperseg, noverlap=Noverlap, nfft=Nfft, boundary=False)
		
		pickle.dump(vr,  open( './'+datadir+'/velr_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
		pickle.dump(vth, open('./'+datadir+'/velth_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
		if r!='0.0':
			pickle.dump(vph, open('./'+datadir+'/velph_filtered_rot'+r+'_r'+str(pr)+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
		
#Shift the times again so that they match with what our spectrogram plots indicate. Best for matching with when mask first becomes non-zero.
for r in rotrates_to_filter:
	torig=pickle.load(open('./'+datadir+'/tt.dic','rb'))
	t[r] = (t[r] + torig[r][0])*1e3

pickle.dump(t, open('./'+datadir+'/t_filtered_tightenfactor'+str(tighten_factor)+'.dic','wb'))

