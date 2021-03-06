import numpy as np
import pickle

execfile('./pars_velocity.py')

#r = rotrate_to_decompose

for r in ['1.0']: #,'1.0']:

	print 'Calling decomp script for rot '+r+' and tighten_factor = '+str(tighten_factor)+'.'

	t = pickle.load(open('./'+datadir+'/t_filtered_tightenfactor'+str(tighten_factor)+'.dic','rb'))

	times = range(len(t[r]))
	times = times[888:]
	
	ER  = {}
	ETH = {}
	if r!='0.0':
		EPH = {}
	
	firstcall = 'yes' #for only reading in data once in decomposition script
	for ti in times:
		execfile('spherical_harmonic_decomposition_nospline.py')
		firstcall='no'
		ER[ti]  = Er
		ETH[ti] = Eth
		if r!='0.0':
			EPH[ti] = Eph
		print ti

	if mass_weighted=='yes':
		pickle.dump(ER ,open('./'+datadir+'/vel_sph_harm_coeffs_radius_rot'+r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
		pickle.dump(ETH,open('./'+datadir+'/vel_sph_harm_coeffs_theta_rot' +r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
		if r!='0.0':
			pickle.dump(EPH,open('./'+datadir+'/vel_sph_harm_coeffs_phi_rot'   +r+'_tightenfactor'+str(tighten_factor)+'_massweight_'+str(mass_weight)+'.dic','wb'))
	else:
		pickle.dump(ER ,open('./'+datadir+'/vel_sph_harm_coeffs_radius_rot'+r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
		pickle.dump(ETH,open('./'+datadir+'/vel_sph_harm_coeffs_theta_rot' +r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))
		if r!='0.0':
			pickle.dump(EPH,open('./'+datadir+'/vel_sph_harm_coeffs_phi_rot'   +r+'_tightenfactor'+str(tighten_factor)+'.dic','wb'))

'''
ERavg = {}
ETHavg= {}

for m in modes:
	ERavg[m]={}
	ETHavg[m]={}
	for l in poloidal_numbers:
		ERavg[m][l] = np.zeros(len(ER[times[0]][m][l][:,0,0]))
		if l!=0:
			ETHavg[m][l]= np.zeros(len(ERavg[m][l]))
		for ti in times:
			ERavg[m][l]+=ER[ti][m][l][:,0,0]**2/len(times)
			if l!=0:
				ETHavg[m][l]+=ETH[ti][m][l][:,0,0]**2/len(times)
'''
