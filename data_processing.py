"""
Created by : Team Unique Tech for ITSP, IIT Bombay

The below code is for processing the signal coming from the electrical circuit through the RaspberryPi. 

The code modifies the array of data collected from the RaspberryPi to filter out the noise through fft algorithms.The data collected 
from RPi is stored in an array to which we apply the fft algorithm which takes us to the intensity vs frequency plot and then remove 
the unwanted frequencies and just keep the band of useful frequencies. 

We then apply ifft to the data to come back in the intensity vs time plot where we just locate the peak of the intensity and the time
at which the intensity attained its maxima. 

"""

import numpy as np
import time
from math import pi
from data_storage import data
from data_storage import n
from data_storage import freq
from data_storage import df

def processing(mic_data):
	
	mic_fft = np.fft.fft(mic_data) # applied fft to mic_data

	abs_mic_fft = 2/n*np.abs(mic_fft) # magnitude of the complex mic_fft array(scaled) 

	fft_freq = np.array([df*i if i<n//2 else df*(n-i) for i in range(n)]) # creates an array where freq[i] = frequency corresponding to mic_fft[i]

	# frequency filter code

	eps = 100 # frequencies within range (freq-eps, freq+eps) will be retained in the filtered signal

	for temp in range(n):

		if((fft_freq < freq + eps) & (fft_freq > freq - eps)):
			continue

		else:
			abs_mic_fft[temp] = 0
			mic_fft[temp] = 0

	# at this point the fft data contains only the relevant frequencies and the noise has been filtered

	mic_ifft = np.fft.ifft(mic_fft) # this is the required noise-free signal obatined by processing signal from the mic

	mic_ifft_max = mic_ifft.max() # max value in the mic_ifft array
	mic_ifft_argmax = np.argmax(mic_ifft) # index corresponding to mic_ifft_max

	max_time = t_axis[mic_ifft_argmax] # time at which mic_ifft_max is attained
	
	return max_time

mic_data_0, mic_data_1, mic_data_2, mic_data_3 = data()

max_time_array = np.array([processing(mic_data_0), processing(mic_data_3), processing(mic_data_2), processing(mic_data_3)])
