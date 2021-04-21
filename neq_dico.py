#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

NEQ_H798P = np.loadtxt('/mnt/c/Users/soubi/OneDrive/Bureau/Travail/Calf1Calf2/Calf1Calf2_H798P/PBxplore/md_CC_H798P_traj_all.PB.Neq.txt')



neq_H798P = {}
for i in NEQ_H798P:
	col1 = i[0]
	col2 = i[1]
	if col1 not in neq_H798P.keys():
		neq_H798P[col1] = col2

for key, val in neq_H798P.items():
	if val > 5:
		print(key, val)
