from numpy import *
from scipy.interpolate import CubicSpline
import pickle

#Define parameters
execfile('./pars_velocity.py')

#Read in data
veldata = {}

for rot in rotrates:
	veldata[rot] = loadtxt('veldata_'+rot+'_wide.dat')

#Extract some parameters, initialize some arrays
numtimes  =  shape(veldata[rotrates[0]])[0]
numpoints = (shape(veldata[rotrates[0]])[1]-1)/4

tt = {}

for rot in rotrates:
	tt[rot] = np.zeros( numtimes )

	for i in range(numtimes):
		tt[rot][i] = veldata[rot][i,0]

	tt[rot] = tt[rot] - bouncetimes[rot] #Shift times so that bounce occurs at t=0 

xx        = np.zeros( numpoints )
yy        = np.zeros( numpoints )
theta     = np.zeros( numpoints )
rr        = np.zeros( numpoints )

velx, vely, veltheta, velr = {}, {}, {}, {}

for rot in rotrates:	
	velx[rot]      = np.zeros( (numtimes,numpoints) )
	vely[rot]      = np.zeros( (numtimes,numpoints) )
	veltheta[rot]  = np.zeros( (numtimes,numpoints) )
	velr[rot]      = np.zeros( (numtimes,numpoints) )

#Extract spatial coordinates and velocity data,
#transform to spherical coordinates.
for i in range(numpoints):
	xx[i] = veldata[rotrates[0]][0,4*i+1] #This is where the x-coordinate columns are
	yy[i] = veldata[rotrates[0]][0,4*i+2] #This is where the y-coordunate columns are
	rr[i] = sqrt( xx[i]**2. + yy[i]**2. ) #Compute radial coordinate

	#Compute theta coordinate
	if yy[i]>=0:
		theta[i] = arctan(xx[i]/yy[i]) #Upper quadrant
	else:
		theta[i] = pi + arctan(xx[i]/yy[i]) #Lower quadrant

	#Transform vector components to spherical coordinates
	for rot in rotrates:
		for j in range(numtimes):
			velx[rot][j,i]     = veldata[rot][j,4*i+3] #This is where vx columns are
			vely[rot][j,i]     = veldata[rot][j,4*i+4] #This is where vy columns are

			#Note this isn't usual polar coordinate transform, since theta is measured from
			#the rotation axis y.
			velr[rot][j,i]     = sin(theta[i])*velx[rot][j,i] + cos(theta[i])*vely[rot][j,i]
			veltheta[rot][j,i] = cos(theta[i])*velx[rot][j,i] - sin(theta[i])*vely[rot][j,i]

#Remove first part of the signal, up to WindowWidth prior to the bounce time. This keeps the data and spectrogram filesizes more manageable.
ww=WindowWidth*1e-3
for rot in rotrates:
	tcoord         = abs(tt[rot]+ww).argmin()
	velx[rot]      =     velx[rot][tcoord:,:]
	vely[rot]      =     vely[rot][tcoord:,:]
	velr[rot]      =     velr[rot][tcoord:,:]
	veltheta[rot]  = veltheta[rot][tcoord:,:]
	tt[rot]        =       tt[rot][tcoord:]

pickle.dump(tt,       open(      'tt.dic','wb'))
pickle.dump(xx,       open(      'xx.dic','wb'))
pickle.dump(yy,       open(      'yy.dic','wb'))
pickle.dump(rr,       open(      'rr.dic','wb'))
pickle.dump(theta,    open(   'theta.dic','wb'))
pickle.dump(velx,     open(    'velx.dic','wb'))
pickle.dump(vely,     open(    'vely.dic','wb'))
pickle.dump(velr,     open(    'velr.dic','wb'))
pickle.dump(veltheta, open('veltheta.dic','wb'))
