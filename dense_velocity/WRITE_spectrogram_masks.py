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

xl[plotr][Hz],yl[plotr][Hz]=[7.5,16.,22.5,35.5,55.,74.],[1500.,1464.7,1473.2,1544.4,1644.,1786.]
xh[plotr][Hz],yh[plotr][Hz]=[7.5,8.5,20.,25.5,52.,74.],[1500.,1561.5,1621.,1678.2,1778.,1786.]


## 1250-1500 Hz mode

Hz='1400'

#Define points in time-frequency space for splines of piecewise-linear functions which form the boundary of the hot band

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18,89.0],[1300.,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01,1604.35]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.0,15.111,34.103,62.834,86.2083,89.0],[1300.,1374.0,1422.38,1494.97,1582.5,1629.46,1604.35]


## 1150-1200 Hz mode 

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz]=[14.4,22.2,38.5,50.2],[1167.7,1153.,1231.3,1329.2]
xh[plotr][Hz],yh[plotr][Hz]=[14.4,16.4,31.3,50.2],[1167.7,1216.6,1314.5,1329.2]


## 1100 Hz mode 

Hz='1100'

xl[plotr][Hz],yl[plotr][Hz]=[14.5,20.4,33.5,44.3,57.2],[1092.,1047.4,1053.,1070.,1148.6]
xh[plotr][Hz],yh[plotr][Hz]=[14.5,18.5,20.75,25.8,32.4,46.6,57.2],[1092.,1143.,1140.,1143.,1177.,1182.,1148.6]


## 900-1000 Hz mode

Hz='900'

#version 1 (bit too fat)
#xl[plotr][Hz],yl[plotr][Hz]=[5.7,7.6,11.5,26.9,38.5,63.,75.,76.3],[912.3,861.7,844.8,856.,895.5,929.2,946.,991.1]

#version 2 (bit thinner)
xl[plotr][Hz],yl[plotr][Hz]=[5.7,11.3,33.,75.,76.3],[912.3,870.3,899.,952.5,991.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.84,18.8,26.86,34.7,41.8,46.3,49.5,60.2,74.2,76.3],[912.3,957.3,991.,996.7,996.7,1011.,1016.7,1030.,1058.6,1047.4,991.1]


## 840-880 Hz mode

Hz='850'

xl[plotr][Hz],yl[plotr][Hz]=[11.8,17.4,27.4,57.7,66.],[830.1,810.6,820.,835.,889.]

xh[plotr][Hz],yh[plotr][Hz]=[11.8,14.3,32.5,56.7,66.],[830.1,879.,903.5,928.,889.]


## 750 Hz mode

Hz='750'

#version 1 (fat)
#xl[plotr][Hz],yl[plotr][Hz]=[10.9,12.65,16.15,38.75,53.6,65.,71.],[750.,705.16,684.8,680.7,717.4,770.4,811.125]
#xh[plotr][Hz],yh[plotr][Hz]=[10.9,13.52,18.3,25.25,35.3,45.3,57.9,71.],[750.,803.,823.35,827.4,823.35,839.65,831.5,811.125]

#version 2 (thinner, cleaner)
xl[plotr][Hz],yl[plotr][Hz]=[12.2,14.2,20.7,41.8,51.4,65.5,69.5],[727.4,693.1,678.5,707.8,712.7,737.2,800.8]
xh[plotr][Hz],yh[plotr][Hz]=[12.2,13.7,28.8,45.3,63.5,69.5],[727.4,781.2,805.7,830.1,835.,800.8]


## 650 Hz mode

Hz='650'

xl[plotr][Hz],yl[plotr][Hz]=[7.,15.75,51.7,67.25,88.],[611.4,591.04,582.9,611.4,676.6]
xh[plotr][Hz],yh[plotr][Hz]=[7.,8.5,17.3,45.5,57.7,88.],[611.4,668.5,683.4,703.,708.,803.]


## 500 Hz mode

Hz='500'

#version 1 (ugly)
#xl[plotr][Hz],yl[plotr][Hz]=[7.,9.45,18.25,29.5,42.7,50.3,82.,88.],[500.,453.,411.15,430.,447.,423.1,459.,519.]
#xh[plotr][Hz],yh[plotr][Hz]=[7.,10.25,15.85,21.5,39.,47.5,88.],[500.,554.5,572.5,566.5,596.4,590.5,519.]

#version 2 (neater, bit tighter)
xl[plotr][Hz],yl[plotr][Hz]=[8.2,12.9,25.,55.6,63.],[477.9,438.7,433.9,453.4,497.5]
xh[plotr][Hz],yh[plotr][Hz]=[8.2,11.4,16.6,47.7,63.],[477.9,521.9,531.7,551.3,497.5]


## 350 Hz mode

Hz='350'

xl[plotr][Hz],yl[plotr][Hz]=[12.8,17.9,25.5,75.,86.1],[331.7,280.,264.4,280.,331.7]
xh[plotr][Hz],yh[plotr][Hz]=[12.8,23.,46.,75.3,86.1],[331.7,378.4,388.7,378.4,331.7]

## 200 Hz mode

Hz='200'

xl[plotr][Hz],yl[plotr][Hz]=[12.2,16.7,49.2,60.],[155.6,114.1,109.,181.5]
xh[plotr][Hz],yh[plotr][Hz]=[12.2,15.4,24.3,51.7,60.],[155.6,217.7,233.3,233.3,181.5]

################################
################################




################################
### rot='0.5'
################################

plotr='0.5'

xl[plotr],yl[plotr],xh[plotr],yh[plotr] = {},{},{},{}

## 1500+ Hz mode, this actually looks like 2 modes, depending on the point we look at

Hz='1500'

xl[plotr][Hz],yl[plotr][Hz]=[7.5,16.,22.5,35.5,55.,74.],[1500.,1464.7,1473.2,1544.4,1644.,1786.]
xh[plotr][Hz],yh[plotr][Hz]=[7.5,8.5,20.,25.5,52.,74.],[1500.,1561.5,1621.,1678.2,1778.,1786.]

## 1250-1500 Hz mode

Hz='1400'

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18,89.0],[1300.,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01,1604.35]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.0,15.111,34.103,62.834,86.2083,89.0],[1300.,1374.0,1422.38,1494.97,1582.5,1629.46,1604.35]

## 1200-1300 Hz mode

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz]=[14.4,22.2,38.5,50.2],[1167.7,1153.,1231.3,1329.2]
xh[plotr][Hz],yh[plotr][Hz]=[14.4,16.4,31.3,50.2],[1167.7,1216.6,1314.5,1329.2]

## 1100 Hz mode 

Hz='1100'

xl[plotr][Hz],yl[plotr][Hz]=[14.5,20.4,33.5,44.3,57.2],[1092.,1047.4,1053.,1070.,1148.6]
xh[plotr][Hz],yh[plotr][Hz]=[14.5,18.5,20.75,25.8,32.4,46.6,57.2],[1092.,1143.,1140.,1143.,1177.,1182.,1148.6]

## 830-900 Hz mode

Hz='900'

xl[plotr][Hz],yl[plotr][Hz]=[10.,15.2,23.6,55.5,66.5,72.3],[815.5,791.,791.,840.,864.4,918.2]
xh[plotr][Hz],yh[plotr][Hz]=[10.,13.9,51.5,72.3],[815.5,879.,952.5,918.2]

## 730-790 Hz mode

Hz='750'

xl[plotr][Hz],yl[plotr][Hz]=[12.4,17.,31.3,61.2,65.1],[726.2,689.5,707.8,756.8,805.7]
xh[plotr][Hz],yh[plotr][Hz]=[12.4,17.,24.1,30.6,59.3,65.1],[726.2,781.2,800.,805.,830.1,805.7]

## 630-750 Hz mode

Hz='650'

xl[plotr][Hz],yl[plotr][Hz]=[8.15,14.,25.,56.3,108.3,109.6],[616.,561.,573.3,604.,683.4,750.6]
xh[plotr][Hz],yh[plotr][Hz]=[8.15,9.45,27.,49.1,107.,109.6],[616.,677.3,701.7,726.2,817.9,750.6]

## 460-530 Hz mode

Hz='500'

xl[plotr][Hz],yl[plotr][Hz]=[8.9,16.7,23.2,37.5,43.3],[453.4,429.,433.9,482.8,551.2]
xh[plotr][Hz],yh[plotr][Hz]=[8.9,11.5,18.7,29.7,43.3],[453.4,502.3,531.7,566.,551.2]

## 350 Hz mode

Hz='350'

xl[plotr][Hz],yl[plotr][Hz]=[17.9,21.2,29.,43.9,106.4,109.6],[334.8,292.,279.8,279.8,304.2,347.]
xh[plotr][Hz],yh[plotr][Hz]=[17.9,24.4,32.2,71.9,107.7,109.6],[334.8,377.6,389.8,402.,395.9,347.]


## 200 Hz mode

Hz='200'

xl[plotr][Hz],yl[plotr][Hz]=[13.,16.3,22.8,50.8,56.7],[181.9,230.8,243.,224.7,163.5]
xh[plotr][Hz],yh[plotr][Hz]=[13.,18.9,41.7,48.8,56.7],[181.9,120.7,96.3,102.4,163.5]

################################
################################




################################
### rot='1.0', normal resolution
################################

plotr='1.0' #rotation case

xl[plotr],yl[plotr],xh[plotr],yh[plotr] = {},{},{},{}


## 1500+ Hz mode

Hz='1500'

xl[plotr][Hz],yl[plotr][Hz]=[7.5,16.,22.5,35.5,68.,74.],[1500.,1464.7,1473.2,1544.4,1689.,1786.]
xh[plotr][Hz],yh[plotr][Hz]=[7.5,8.5,20.,52.,74.],[1500.,1561.5,1621.,1778.,1786.]


## 1250-1500 Hz mode

Hz='1400'

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.915,12.1897,20.55,26.3117,42.8685,66.2427,87.18,89.0],[1300.,1247.33,1253.73,1281.5,1315.64,1405.3,1494.97,1559.01,1604.35]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.0,15.111,34.103,62.834,86.2083,89.0],[1300.,1374.0,1422.38,1494.97,1582.5,1629.46,1604.35]


## 1120-1220 Hz mode

Hz='1200'

xl[plotr][Hz],yl[plotr][Hz]=[9.3,15.1,20.5,32.5,41.8,46.1],[1109.,1086.7,1070.,1098.,1148.6,1244.3]
xh[plotr][Hz],yh[plotr][Hz]=[9.3,12.7,18.3,22.2,30.4,41.3,46.1],[1109.,1154.3,1176.8,1193.7,1233.,1272.4,1244.3]


## 1030-1100 Hz mode

Hz='1100'

xl[plotr][Hz],yl[plotr][Hz]=[13.,17.1,32.6,36.,51.,57.8],[1030.5,1002.4,1019.2,1015.4,1057.,1114.9]
xh[plotr][Hz],yh[plotr][Hz]=[13.,16.4,21.6,32.5,41.3,50.3,57.8],[1030.5,1075.5,1081.1,1109.3,1148.6,1165.5,1114.9]


## 900-1000 Hz mode

Hz='900'

xl[plotr][Hz],yl[plotr][Hz]=[5.7,7.6,11.5,26.9,38.5,63.,75.,76.3],[912.3,861.7,844.8,856.,895.5,929.2,946.,991.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,9.84,18.8,26.86,34.7,43.,49.5,60.2,74.2,76.3],[912.3,957.3,991.,996.7,996.7,1010.,1030.,1058.6,1047.4,991.1]


## 750 - 830 Hz mode

Hz='750'

xl[plotr][Hz],yl[plotr][Hz]=[5.7,6.3,11.5,18.6,25.93,35.85,47.3,58.1,69.3,75.3,76.3],[732.3,707.8,683.4,698.,712.7,737.2,756.75,766.5,766.5,795.9,830.1]
xh[plotr][Hz],yh[plotr][Hz]=[5.7,7.0,12.5,25.7,34.9,42.76,53.2,68.95,75.1,76.3],[732.3,761.6,794.5,834.3,859.2,859.2,884.,884.,869.1,830.1]

#Thinner one, as a test
#xl[plotr][Hz],yl[plotr][Hz]=[14.5,19.2,34.7,51.3,70.3],[749.1,726.7,766.,794.2,805.4]
#xh[plotr][Hz],yh[plotr][Hz]=[14.5,19.2,33.7,52.8,68.3,70.3],[749.1,771.7,811.,839.2,839.2,805.4]

## 630-730 mode

Hz='650'

#version 1 (crappy)
#xl[plotr][Hz],yl[plotr][Hz]=[10.4,11.3,22.,33.8,43.9,61.5,75.5,76.25],[644.2,610.,628.,624.7,649.1,663.8,668.7,717.6]
#xh[plotr][Hz],yh[plotr][Hz]=[10.4,12.3,22.75,35.5,45.2,57.4,74.5,76.25],[644.2,678.5,698.3,742.,761.6,766.5,786.1,717.6]

#version 2 (better)
xl[plotr][Hz],yl[plotr][Hz]=[17.3,21.8,37.,68.4,89.4,105.4,106.],[624.7,610.,620.,649.2,658.9,693.1,727.4]
xh[plotr][Hz],yh[plotr][Hz]=[17.3,20.5,74.7,104.7,106.],[624.7,673.6,742.,771.4,727.4]

## 530-600 Hz mode

Hz='500'

#version 1 (misses the band a bit)
#xl[plotr][Hz],yl[plotr][Hz]=[6.0,9.5,17.5,32.85,58.1,74.,76.25],[524.1,487.,502.35,531.7,531.8,556.2,605.1]
#xh[plotr][Hz],yh[plotr][Hz]=[6.0,10.,22.2,41.5,60.9,74.8,76.25],[524.1,600.2,618.,649.1,663.8,649.1,605.1]

#version 2 (bit more precise and clean)
xl[plotr][Hz],yl[plotr][Hz]=[13.6,20.6,35.,70.,86.4],[556.2,502.4,526.8,546.4,595.3]
xh[plotr][Hz],yh[plotr][Hz]=[13.6,17.4,36.5,73.,86.4],[556.2,590.4,615.,639.4,595.3]

## 400 Hz mode

Hz='350'

xl[plotr][Hz],yl[plotr][Hz]=[18.2,24.,93.,105.7,106.3],[390.,346.,365.4,380.,419.2]
xh[plotr][Hz],yh[plotr][Hz]=[18.2,21.4,49.,91.,103.,106.3],[390.,440.,463.,473.,468.,419.2]

# 290 Hz mode

Hz='200'

xl[plotr][Hz],yl[plotr][Hz]=[13.,19.,42.,70.3,78.8],[290.3,228.,217.8,223.,264.4]
xh[plotr][Hz],yh[plotr][Hz]=[13.,18.5,38.8,63.7,77.6,78.8],[290.3,331.2,337.,326.5,326.5,264.4]

################################
################################

pickle.dump(xl,open('./'+datadir+'/xl.dic','wb'))
pickle.dump(xh,open('./'+datadir+'/xh.dic','wb'))
pickle.dump(yl,open('./'+datadir+'/yl.dic','wb'))
pickle.dump(yh,open('./'+datadir+'/yh.dic','wb'))
'''
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

keys1 = rot_to_get_masks_for #xl.keys()

masks = {}

for i in keys1:
	keys2 = xl[i].keys()
	masks[i] = {}
	for j in keys2:
		masks[i][j] = createmask(xl[i][j],yl[i][j],xh[i][j],yh[i][j],i)

pickle.dump(masks,open('./'+datadir+'/velocity_spectrogram_masks_tightenfactor'+str(tighten_factor)+'.dic','wb'))
'''
