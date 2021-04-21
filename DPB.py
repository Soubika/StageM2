#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

PB1 = np.loadtxt('CC_WT_traj_all_global.PB.count.txt', skiprows=1)
PB2 = np.loadtxt('md_CC_H798P_traj_all.PB.count.txt', skiprows=1)



pb1 = PB1[0:,1:]
pb2 = PB2[0:,1:]
frame1 = sum(pb1[2])- (pb1[2][0])
frame2 = sum(pb2[2])- (pb2[2][0])

tableau1 = pb1 / frame1
tableau2 = pb2 / frame2
ab = abs(tableau1 - tableau2)
so = np.sum(ab, axis = 1)
'''
plt.xlabel('Residues')
plt.ylabel('Delta PB')
plt.title('Delta PB WT vs H798P')
plt.plot(PB1[:,0], so)
plt.show()
'''

for i in zip(PB1[:,0], so) :
	print(i)
'''

dico = {}
for i,j in zip(list(range(603,960)), so) :
	dico[i] = j
for k, v in dico.items() :
	if v > 1 :
		print(k, v)
'''











