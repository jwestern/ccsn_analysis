####################################################################
# Parameter file for computing and plotting velocity spectrograms. #
####################################################################

datadir = '100radialpoints/picluster'

rotrates           = ['0.0','1.0'] #Rotation rate cases (rad/s)

bouncetimes={}	#Time at which bounce occurs (seconds)
bouncetimes['0.0'] = 0.300 #in seconds
bouncetimes['1.0'] = 0.301 #in seconds
bouncetimes['2.0'] = 0.316 #in seconds

#Spectrogram parameters
Window='bohman'
WindowWidth=35 #in ms
Scaling='spectrum' 
Mode='complex' #'psd' for visualizing spectrograms, 'complex' for filtering and inverting spectrograms
	       #### ^^^^ NO LONGER TRUE. CANNOT STORE BOTH TYPES, SO PLOTTING USES 'complex' AS WELL.

#Which points to compute spectrograms for
cminr = 0.0 #km
cmaxr = 30.1
cmintheta = -0.01
cmaxtheta = pi+0.01

#Which components of velocity to plot
plotv  = 'veltheta' #One at a time
titlev = r'$v_\theta$' #One at a time

#Which rotrate to plot (only one at a time)
plotr = '1.0'

#Which points to plot (specify range of r (km) and theta (rad))
minr = 6.0
maxr = 7.0
mintheta = 0.42#pi/20
maxtheta = 0.46#1.05*pi/2

skipr = 1 #plot every skipr-th radius
skipt = 3 #plot every skipt-th theta

#################
# Mask parameters
################

tighten_factor = 1. #Shrink mask region by 1/tighten_factor
 

###################
# Filter parameters
###################

rotrates_to_filter = ['1.0']

############################################
#Spherical harmonic decomposition parameters
############################################

test                 = 'no' #Whether to put the script in test mode, testing on known velocity field
rotrate_to_decompose = '1.0' #one at a time for now. Do not set to '0.0' if test = 'yes'.
poloidal_numbers     = range(0,11,1) #which angular momentum numbers l to compute spherical harmonics for
mass_weighted        = 'yes' #Whether to mass-weight the velocities prior to decomposition
mass_weight          = 0.5   #What power to raise the mass density to when weighting the vel field

#################################
# Eigenmode extraction parameters 
#################################

rotrate_to_extract  = '1.0'
#tighten_factor is also used in this script
half_periods        = 'yes' #whether to sample at half periods with alternating minus sign

############################
# Node counting parameters #
############################

rpns_definition_rho = 1e11  #g/cm^3, where to define the radius of the PNS
Ethreshold          = 1.0  #Terminate the node counter when the energy in the mode
			    #integrated up to the current radius is greater than this
			    #fraction of the total mode energy.
