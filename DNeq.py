#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

pathway = "C:/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/"
neq_WT = np.loadtxt('{}Calf1Calf2_WT/Neq/CC_WT_traj_all_global.PB.Neq.txt'.format(pathway))
neq_H798P = np.loadtxt('{}Calf1Calf2_H798P/PBxplore/md_CC_H798P_traj_all.PB.Neq.txt'.format(pathway))

neq1 = neq_WT[:,1]
neq2 = neq_H798P[:,1]
delta_neq = abs(neq1 - neq2)
x = neq_WT[:,0]

plt.xlabel("Residues")
plt.ylabel('Delta Neq')
plt.title("Delta Neq WT vs H798P")
plt.plot(x, delta_neq)
#plt.plot(neq1[:,0], neq1[:,1], color = 'r')
#plt.plot(neq2[:,0], neq2[:,1], color = 'g')
plt.show()

'''
dico_neq_H798P = {}
for i in neq1[:,0] :
	col1 = i
	col2 = delta_neq
	if col1 not in dico_neq_H798P.keys():
		dico_neq_H798P[col1] = col2

for key, val in dico_neq_H798P.items():
	print(val)
'''
'''
dico = {}
for i, j in zip(list(range(603,960)),delta_neq) :
	dico[i] = j
for k, v in dico.items() :
	if v >= 2 :
		print(k, v)
'''
















