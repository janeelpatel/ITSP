"""
Created by : Team Unique Tech for ITSP, IIT Bombay

The below code is for calculating the angle through which the bot needs to rotate in order to reach to the source. 
The code extracts the required data and then using principles similar to YDSE, calculates the rotation angle.

"""

import numpy as np
import time
import math
from data_processing import max_time_array as mta

dist = 0.05 # distance between mic in metres  
sound_speed = 343 # speed of sound in m/s 

time_diff_01 = np.abs(mta[0]-mta[1])

dist_01 = time_diff_01 * sound_speed

angle_01 = atan2(dist_01, dist) # in radians

if (mta[0]<mta[1]): # checks which mic is near the source
	orientation = 'C'
else:
	orientation = 'AC'
	
# the orientation is fixed now
# the sound waves are assumed to be planar 

angle_rad = angle_01 # average rotation angle in radians 
angle_deg = angle_rad*180/(math.pi) # average rotation angle in degrees 
