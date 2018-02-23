####################################################################
# Parameter file for computing and plotting velocity spectrograms. #
####################################################################

rotrates           = ['0.0'] #Rotation rate cases (rad/s)

bouncetimes={}	#Time at which bounce occurs (seconds)
bouncetimes['0.0'] = 0.300 #in seconds
bouncetimes['2.0'] = 0.316 #in seconds

#Spectrogram parameters
Window='bohman'
WindowWidth=35 #in ms
Scaling='spectrum' 
Mode='complex' #'psd' for visualizing spectrograms, 'complex' for filtering and inverting spectrograms

#Which components of velocity to plot
plotv = ['velr','veltheta'] #,'veltheta'] #'velx','vely'

#Which rotrate to plot (only one at a time)
plotr = '0.0'

#Which points to plot (specify range of r (km) and theta (rad))
minr = 74.0
maxr = 86.0
mintheta = 0.9*pi/4
maxtheta = 1.1*3*pi/4#1.1*3*pi/4

#Plotting parameters
titles=[r'v_r',r'$v_\theta$'] #,r'$v_\theta$'] #r'$v_x$',r'$v_y$'

###################
# Filter parameters
###################

rotrates_to_filter = ['0.0']

############################################
#Spherical harmonic decomposition parameters
############################################

rotrate_to_decompose = '0.0' #one at a time for now
poloidal_numbers     = range(0,11,1) #which angular momentum numbers l to compute spherical harmonics for
