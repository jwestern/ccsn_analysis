from numpy import *
from matplotlib import *
import pickle
from scipy.interpolate import interp1d

execfile('./pars_velocity.py')

xl = pickle.load(open('./'+datadir+'/xl.dic','rb'))
xh = pickle.load(open('./'+datadir+'/xh.dic','rb'))
yl = pickle.load(open('./'+datadir+'/yl.dic','rb'))
yh = pickle.load(open('./'+datadir+'/yh.dic','rb'))

rots  = ['1.0'] #xl.keys()

xmid = {}

for r in rots:
	xmid[r] = {}
	modes   = xl[r].keys()
	ERtemp  = pickle.load(open('./'+datadir+'/vel_sph_harm_coeffs_radius_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','rb'))
	for m in modes:
		
		xmid[r][m] = {}

		xlo = interp1d(xl[r][m],yl[r][m],bounds_error=False,fill_value='extrapolate')
		xhi = interp1d(xh[r][m],yh[r][m],bounds_error=False,fill_value='extrapolate')

		xmin = amin(xl[r][m])
		xmax = amax(xl[r][m])

		xs = arange( xmin, xmax, (xmax-xmin)/len(ERtemp.keys()) )[:-1]

		xmid[r][m]['freq'] = 0.5*(xhi(xs)+xlo(xs))
		xmid[r][m]['time'] = xs

pickle.dump(xmid,open('./'+datadir+'/xmid.dic','wb'))
