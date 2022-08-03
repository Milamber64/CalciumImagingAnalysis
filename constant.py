"""
This python file include all constants. Change them here, and the changes will apply to all python file that you run afterwards
"""

from scipy import signal
import sys
import numpy as np

#set debug to True to show all debugging statements, and set to False to hide all (also saves time)
debug = True
#folder containing 3 children folder: Data (original data), OutputData(normalized, smoothed, etc. data),
# and Figure(output figures)
parentFolder = "#3"
#to be added to each file name
planeNumber= "P0"
#start of the stimulus (in frames, cannot be 0, must be >=1)
#input stimStart = "all" if want the entirety of the recording
stimStart = 1
#if want the entirety of the recording, input stimEnd = "all"
#if exceed max frame number, automatically take the 
stimEnd = "all"

#start of baseline
baselineStart = 1

#end of baseline (used to measure noise)
baselineEnd = 2000

expNumber = parentFolder
#path to raw data

pathToRaw = "../"+parentFolder+"/Data/"+parentFolder+"_"+planeNumber+"_"
# directory = '../#2_Data/#2_P0_Results.csv'

pathToData = "../"+parentFolder+"/Data/"+parentFolder+"_"
# directory = ../#2_Data/#2_

pathToOutputData = "../"+parentFolder+"/"+"OutputData/"
# OutPath = '../#2_Output/'

pathToFigure = "../"+parentFolder+"/"+"Figure/"

#ROIs of interest if say np.arrange (1,3), then will only include ROI 1 and 2
# ROIs = np.array([1])
ROIs = 'all'

#the prefix to add before all OutputData and Figures
prefix = expNumber + "_" + planeNumber+ " _frm" + str(stimStart) + "-"+ str(stimEnd)+ "_" 

#the prefix excluding frame number
splPrefix = expNumber + "_" + planeNumber+ "_"

# sample spacing
T = 1.0 / 8.0 # 8Hz
#window for normalization
window = 400 
#window size for smoothing
# this is the window in which the polynomial fits. Larger numbers are more smooth, 
# but can decrease the height of transient peaks. Choose something on the same scale as your events, 
# e.g. if a transient peak lasts around 30 frames, 15 is a good starting point.
window_size = 15
#polynomial order for smoothing
#this is the order of polynomial used for smoothing. 
# Bigger numbers fit the curve more closely (i.e. less smooth, but more accurate)
polynomial = 3
#Design a digital low-pass filter at 4Hz to remove frequencies faster than 4Hz
sos = signal.butter(N = 10,Wn = 4, btype = 'lowpass', fs=8.2, output='sos') 
# signal above threshold are considered an event
threshold = 0.5
