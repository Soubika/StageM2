#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


rmsf_WT = np.loadtxt('/mnt/c/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/Calf1Calf2_WT/RMSF/rmsf_C1C2_WT_global.txt')
rmsf_H798P = np.loadtxt('/mnt/c/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/Calf1Calf2_H798P/analyse/rmsf_CC_H798P_global_1_6.txt')

dico = {}
for li in rmsf_WT:
	col1 = li[0]
	col2 = li[1]
	print(col2)

	if col1 not in dico.keys():
		dico[col1] = col2

for key, val in dico.items():
	if val > 1:
		print(key, val)


'''
rmsf1 = rmsf_WT[:,1]
rmsf2 = rmsf_H798P[:,1]

print(rmsf1, rmsf2)


x = np.arange(len(rmsf1))
plt.plot(x, rmsf1, color = 'b')
plt.plot(x, rmsf2, color = 'r')
plt.show()
'''