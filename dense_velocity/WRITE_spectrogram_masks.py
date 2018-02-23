from numpy import *
from matplotlib import *
import pickle
from scipy.interpolate import interp1d

execfile('./pars_velocity.py')

spect = pickle.load(open(      './'+datadir+'/spect_complex.dic','rb'))
specf = pickle.load(open(      './'+datadir+'/specf_complex.dic','rb'))
#spec  = pickle.load(open('velrspec_complex_r0.dic','rb'))

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


## 1250-1500 Hz mode

Hz='1400'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

#Define points in time-frequency space for splines of piecewise-linear functions which form the boundary of the hot band

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18,89.0],[1300.,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01,1604.35]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.0,15.111,34.103,62.834,86.2083,89.0],[1300.,1374.0,1422.38,1494.97,1582.5,1629.46,1604.35]


## 1150-1200 Hz mode ####################### not in 1.0 yet

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[15.,20.6,30.6,43.2,45.3],[1134.7,1119.,1150.,1171.1,1221.8]
xh[plotr][Hz],yh[plotr][Hz]=[15.,19.6,26.9,40.,45.3],[1134.7,1205.,1255.5,1266.8,1221.8]


## 1100 Hz mode ####################### not in 1.0 yet

Hz='1100'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[14.5,20.4,33.5,44.3,57.2],[1092.,1047.4,1053.,1070.,1148.6]
xh[plotr][Hz],yh[plotr][Hz]=[14.5,18.5,20.75,25.8,32.4,46.6,57.2],[1092.,1143.,1140.,1143.,1177.,1182.,1148.6]


## 900-1000 Hz mode

Hz='900'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[5.7,7.6,11.5,26.9,38.5,63.,75.,76.3],[912.3,861.7,844.8,856.,895.5,929.2,946.,991.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.84,18.8,26.86,34.7,41.8,46.3,49.5,60.2,74.2,76.3],[912.3,957.3,991.,996.7,996.7,1053.,1041.7,1030.,1058.6,1047.4,991.1]

#xl[plotr][Hz],yl[plotr][Hz]=[8.5,13.,28.7,59.6,73.2],[1080.3,995.,995.,1043.8,1190.]
#xh[plotr][Hz],yh[plotr][Hz]=[8.5,11.4,26.,39.4,62.05,73.2],[1080.3,1263.,1311.5,1409.,1397.,1190.]


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

################################
### rot='1.0', normal resolution
################################

plotr='1.0' #rotation case

xl[plotr],yl[plotr],xh[plotr],yh[plotr] = {},{},{},{}


## 1500+ Hz mode

Hz='1500'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[7.5,16.,22.5,35.5,55.,74.],[1500.,1464.7,1473.2,1544.4,1644.,1786.]
xh[plotr][Hz],yh[plotr][Hz]=[7.5,8.5,20.,25.5,52.,74.],[1500.,1561.5,1621.,1678.2,1778.,1786.]


## 1250-1500 Hz mode

Hz='1400'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

#Define points in time-frequency space for splines of piecewise-linear functions which form the boundary of the hot band

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18,89.0],[1300.,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01,1604.35]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.0,15.111,34.103,62.834,86.2083,89.0],[1300.,1374.0,1422.38,1494.97,1582.5,1629.46,1604.35]


## 1120-1220 Hz mode

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[13.,17.1,32.6,37.5,48.,57.8],[1030.5,1002.4,1019.2,1002.4,1025.,1114.9]
xh[plotr][Hz],yh[plotr][Hz]=[13.,16.4,21.6,32.5,41.3,50.3,57.8],[1030.5,1075.5,1081.1,1109.3,1148.6,1165.5,1114.9]


## 1030-1100 Hz mode

Hz='1100'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[9.3,15.1,20.5,32.5,41.8,46.1],[1109.,1086.7,1070.,1098.,1148.6,1244.3]
xh[plotr][Hz],yh[plotr][Hz]=[9.3,12.7,18.3,22.2,30.4,41.3,46.1],[1109.,1154.3,1176.8,1193.7,1233.,1272.4,1244.3]


## 900-1000 Hz mode

Hz='900'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[5.7,7.6,11.5,26.9,38.5,63.,75.,76.3],[912.3,861.7,844.8,856.,895.5,929.2,946.,991.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.84,18.8,26.86,34.7,41.8,46.3,49.5,60.2,74.2,76.3],[912.3,957.3,991.,996.7,996.7,1053.,1041.7,1030.,1058.6,1047.4,991.1]


## 750 - 830 Hz mode

Hz='750'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.3,11.5,18.6,25.93,35.85,47.3,58.1,69.3,75.3,76.3],[732.3,707.8,683.4,698.,712.7,737.2,756.75,766.5,766.5,795.9,830.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,7.0,12.5,25.7,34.9,42.76,53.2,68.95,75.1,76.3],[732.3,761.6,794.5,834.3,859.2,859.2,884.,884.,869.1,830.1]

#Thinner one, as a test
#xl[plotr][Hz],yl[plotr][Hz]=[14.5,19.2,34.7,51.3,70.3],[749.1,726.7,766.,794.2,805.4]
#xh[plotr][Hz],yh[plotr][Hz]=[14.5,19.2,33.7,52.8,68.3,70.3],[749.1,771.7,811.,839.2,839.2,805.4]

## 630-730 mode

Hz='650'

xl[plotr][Hz],yl[plotr][Hz]=[10.4,11.3,22.,33.8,43.9,61.5,75.5,76.25],[644.2,610.,628.,624.7,649.1,663.8,668.7,717.6]
xh[plotr][Hz],yh[plotr][Hz]=[10.4,12.3,22.75,35.5,45.2,57.4,74.5,76.25],[644.2,678.5,698.3,742.,761.6,766.5,786.1,717.6]


## 600 Hz mode

Hz='600'

xl[plotr][Hz],yl[plotr][Hz],xh[plotr][Hz],yh[plotr][Hz] = {},{},{},{}

xl[plotr][Hz],yl[plotr][Hz]=[6.0,7.03,17.5,32.85,58.1,74.,76.25],[524.1,463.2,502.35,531.7,531.8,556.2,605.1]
xh[plotr][Hz],yh[plotr][Hz]=[6.0,10.,22.2,41.5,60.9,74.8,76.25],[524.1,600.2,618.,649.1,663.8,649.1,605.1]


################################
################################

pickle.dump(xl,open('./'+datadir+'/xl.dic','wb'))
pickle.dump(xh,open('./'+datadir+'/xh.dic','wb'))
pickle.dump(yl,open('./'+datadir+'/yl.dic','wb'))
pickle.dump(yh,open('./'+datadir+'/yh.dic','wb'))

#Generates a mask given a rotation case (plotr), and points (xl,yl,xh,yh) for upper and lower mode-boundary splines

def createmask(xl,yl,xh,yh,plotr):

	#Generate piecewise linear splines

	xlo=interp1d(xl,yl,bounds_error=False)

	xhi=interp1d(xh,yh,bounds_error=False)

	#Generate mask from spectrogram array

	spec = pickle.load(open('./'+datadir+'/velrspec_complex_rot'+plotr+'_r0.dic','rb'))

	p=spec.keys()[0] #specifies a random point in star (not important which, since masks are already defined by xlo, xhi)

	bup=spec[p]*1.

	for i in range(shape(spec[p])[0]):
	    for j in range(shape(spec[p])[1]):

		ttt = spect[plotr][j]*1e3
		fff = specf[plotr][i]

		xlo_new = xlo(ttt) + ( 0.5*(xhi(ttt)+xlo(ttt)) - xlo(ttt) ) * (1. - 1./tighten_factor) #Shrink region according to tighten_factor
		xhi_new = xhi(ttt) - ( xhi(ttt) - 0.5*(xhi(ttt)+xlo(ttt)) ) * (1. - 1./tighten_factor)

	        if ((ttt>=amax([xl[0],xh[0]])) and (ttt<=amin([xl[-1],xh[-1]]))):
	            if ((fff<=xlo_new) or (fff>=xhi_new)):
	                bup[i,j]=0.
	            else:
	                bup[i,j]=1.
	        else:
	            bup[i,j]=0.

	return bup

#####

keys1 = xl.keys()

masks = {}

for i in keys1:
	keys2 = xl[i].keys()
	masks[i] = {}
	for j in keys2:
		masks[i][j] = createmask(xl[i][j],yl[i][j],xh[i][j],yh[i][j],i)

pickle.dump(masks,open('./'+datadir+'/velocity_spectrogram_masks_tightenfactor'+str(tighten_factor)+'.dic','wb'))

