#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

RMSF_WT = np.loadtxt('/mnt/c/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/Calf1Calf2_WT/RMSF/rmsf_C1C2_WT_global.txt')
RMSF_H798P = np.loadtxt('/mnt/c/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/Calf1Calf2_H798P/analyse/rmsf_CC_H798P_global_1_6.txt')

rmsf_wt = {}
for i in RMSF_WT:
	col1 = i[0]
	col2 = i[1]
	if col1 not in rmsf_wt.keys():
		rmsf_wt[col1] = col2

for key, val in rmsf_wt.items() :
	if val > 0.75 :
			print(key, val)

rmsf_H798P = {}
for j in RMSF_H798P:
	col3 = j[0]
	col4 = j[1]
	if col3 not in rmsf_H798P.keys():
		rmsf_H798P[col3] = col4

for key2, val2 in rmsf_H798P.items():
	if val2 > 0.75:
		print(key2, val2)
