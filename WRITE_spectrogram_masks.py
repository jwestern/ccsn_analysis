from numpy import *
from matplotlib import *
import pickle

execfile('./pars_velocity.py')
'''
xx            = pickle.load(open(           'xx.dic','rb'))*1e-5 #Convert to km
yy            = pickle.load(open(           'yy.dic','rb'))*1e-5 #Convert to km
rr            = pickle.load(open(           'rr.dic','rb'))*1e-5 #Convert to km
theta         = pickle.load(open(        'theta.dic','rb'))
'''
#velxspecf     = pickle.load(open(    'velxspecf_psd.dic','rb'))
#velyspecf     = pickle.load(open(    'velyspecf_psd.dic','rb'))
#velrspecf     = pickle.load(open(    'velrspecf_psd.dic','rb'))
velthetaspecf = pickle.load(open('velthetaspecf_psd.dic','rb'))

#velxspect     = pickle.load(open(    'velxspect_psd.dic','rb'))
#velyspect     = pickle.load(open(    'velyspect_psd.dic','rb'))
#velrspect     = pickle.load(open(    'velrspect_psd.dic','rb'))
velthetaspect = pickle.load(open('velthetaspect_psd.dic','rb'))

#velxspec      = pickle.load(open(     'velxspec_psd.dic','rb'))
#velyspec      = pickle.load(open(     'velyspec_psd.dic','rb'))
#velrspec      = pickle.load(open(     'velrspec_psd.dic','rb'))
velthetaspec  = pickle.load(open( 'velthetaspec_psd.dic','rb'))


xl,yl,xh,yh = {},{},{},{}

################################
### rot='0.0', normal resolution
################################

plotr='0.0' #rotation case

xl[plotr],yl[plotr],xh[plotr],yh[plotr] = {},{},{},{}

## 1500+ Hz mode

Hz='1500'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[7.5,16.,22.5,35.5,55.,74.],[1500.,1464.7,1473.2,1544.4,1644.,1786.]
xh[plotr][Hz],yh[plotr][Hz]=[7.5,8.5,20.,25.5,52.,74.],[1500.,1561.5,1621.,1678.2,1778.,1786.]

## 1200-1500 Hz mode

Hz='1400'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

#Define points in time-frequency space for splines of piecewise-linear functions which form the boundary of the hot band

xl[plotr][Hz],yl[plotr][Hz]=[-1.945,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18],[1251.6,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01]
xh[plotr][Hz],yh[plotr][Hz]=[-1.945,-1.932,2.53,15.111,34.103,62.834,86.2083],[1251.6,1304.97,1342.39,1422.38,1494.97,1582.5,1629.46]

## 1000-1400 Hz blob (identified from GW spectrogram)

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[8.5,13.,28.7,59.6,73.2],[1080.3,995.,995.,1043.8,1190.]
xh[plotr][Hz],yh[plotr][Hz]=[8.5,11.4,26.,39.4,62.05,73.2],[1080.3,1263.,1311.5,1409.,1397.,1190.]

## 750 Hz mode

Hz='750'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[10.9,12.65,16.15,38.75,53.6,65.,71.],[750.,705.16,684.8,680.7,717.4,770.4,811.125]
xh[plotr][Hz],yh[plotr][Hz]=[10.9,13.52,18.3,25.25,35.3,45.3,57.9,71.],[750.,803.,823.35,827.4,823.35,839.65,831.5,811.125]

## 650 Hz mode

Hz='650'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[7.,15.75,51.7,67.25,88.],[611.4,591.04,582.9,611.4,676.6]
xh[plotr][Hz],yh[plotr][Hz]=[7.,8.5,16.7,41.5,70.6,88.],[611.4,668.5,697.,717.4,770.4,803.]

## 500 Hz mode

Hz='500'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[7.,9.45,18.25,29.5,42.7,50.3,82.,88.],[500.,453.,411.15,430.,447.,423.1,459.,519.]
xh[plotr][Hz],yh[plotr][Hz]=[7.,10.25,15.85,21.5,39.,47.5,88.],[500.,554.5,572.5,566.5,596.4,590.5,519.]

################################
################################


#Generates a mask given a rotation case (plotr), and points (xl,yl,xh,yh) for upper and lower mode-boundary splines

def createmask(xl,yl,xh,yh,plotr):

	#Generate piecewise linear splines

	xlo=interp1d(xl,yl,bounds_error=False)

	xhi=interp1d(xh,yh,bounds_error=False)

	#Generate mask from spectrogram array

	p=velthetaspec[plotr].keys()[0] #specifies a random point in star (not important which, since masks are already defined by xlo, xhi)

	bup=velthetaspec[plotr][p]*1.

	for i in range(shape(velthetaspec[plotr][p])[0]):
	    for j in range(shape(velthetaspec[plotr][p])[1]):
	        if ((velthetaspect[plotr][p][j]*1e3>=amax([xl[0],xh[0]])) and (velthetaspect[plotr][p][j]*1e3<=amin([xl[-1],xh[-1]]))):
	            if ((velthetaspecf[plotr][p][i]<=xlo(velthetaspect[plotr][p][j]*1e3)) or (velthetaspecf[plotr][p][i]>=xhi(velthetaspect[plotr][p][j]*1e3))):
	                bup[i,j]=0.
	            else:
	                bup[i,j]=1.
	        else:
	            bup[i,j]=0.

	return bup

#####

keys1 = xl.keys()
keys2 = xl[keys1[0]].keys()

masks = {}

for i in keys1:
	masks[i] = {}
	for j in keys2:
		masks[i][j] = createmask(xl[i][j],yl[i][j],xh[i][j],yh[i][j],i)

pickle.dump(masks,open('velocity_spectrogram_masks.dic','wb'))
