from numpy import *
from matplotlib import *
import numpy
from scipy.special import sph_harm
#from scipy.interpolate import SmoothBivariateSpline
from scipy.interpolate import interp1d

execfile('pars_velocity.py')

r = rotrate_to_extract

rr       = pickle.load(open(            './'+datadir+'/rr.dic','rb'))*1e-5 #Convert to km
theta    = pickle.load(open(         './'+datadir+'/theta.dic','rb'))

rr       = np.round(rr,9) #Round to 9 decimal places, so we can accurately count how many unique values there are
theta    = np.round(theta,9)

ru = np.unique(rr)
tu = np.unique(theta)
ra = range(len(ru))
ta = range(len(tu))

rhospl_in_r = {}

rho = pickle.load(open('./'+datadir+'/rho.dic','rb')) #[r], and has shape(number of times, number of radii*number of angles.
							#for a given time ti, [ti,:number of radii] has the radial profile along
							#the first angle, theta=0. Then theta increases all the way to pi.
rho = rho[r]

xmid = pickle.load(open('./'+datadir+'/xmid.dic','rb'))

toriginal=pickle.load(open('./'+datadir+'/tt.dic','rb')) #The original time array. Same length as rho (along the time axis).

toriginal=toriginal[r]*1e3

timesi = range(len(toriginal))

starttimes = [] #List of indexes for all starting times for modes
for m in modes:
	starttimes.append(where(toriginal<xmid[r][m]['time'][0])[0][-1])

tmini = amin(starttimes) #Get earliest one
timesi = timesi[tmini:]  #Shorten times we look at... allows to increase rpns_definition_rho

for ti in timesi:
	rhospl_in_r[ti] = {}
	for pt in ta:
		rhospl_in_r[ti][pt] = interp1d(ru,rho[ti,len(ra)*pt:len(ra)*(pt+1)],fill_value='extrapolate')

rpns_avgs = []

runew = arange(ru[0],ru[-1],1e-3) #Very densely sampled radius, for finding where rho = rpns_definition_rho

for ti in timesi: #Averaging the pns radius over angles here
	print 'Getting average PNS radius, where rho = '+str(rpns_definition_rho/1e10)+'*1e10 g/cm^3, at time = '+str(toriginal[ti])+'...'
	temp_rhos = []

	for pt in ta:
		rupnsi = where(rhospl_in_r[ti][pt](runew) > rpns_definition_rho)[0][-1] #index where runew = rpns
		temp_rhos.append(runew[rupnsi])

	rpns_avgs.append( average(temp_rhos) ) 

rpns_avgs_dic={}
rpns_avgs_dic['time']      = toriginal[timesi]
rpns_avgs_dic['rpns_avgs'] = rpns_avgs

pickle.dump(rpns_avgs_dic,open('./'+datadir+'/rpns_avgs_rot'+r+'_rpns_definition_rho_'+str(rpns_definition_rho/1e10)+'e10.dic','wb'))

rpns_spl_avg = interp1d(toriginal[timesi],rpns_avgs)




