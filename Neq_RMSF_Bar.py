#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("rmsf_IEGF2_global_1_7.txt")
data2 = np.loadtxt('md_IEGF2_traj_all.PB.Neq.txt')

bar_width = 0.3
opacity = 0.4
y1 = data[:,1]
y2 = data2[:,1]

fig, ax1 = plt.subplots()
t = data[:,1]
ax1.bar(np.arange(len(y1)) + bar_width, y1, bar_width, align = 'center', alpha = opacity, color = 'b')
ax1.set_xlabel('Residues')
ax1.set_ylabel('RMSF', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
t2 = data2[:,1]
ax2.bar(np.arange(len(y2)), y2, bar_width, align = 'center', alpha = opacity, color = 'r')
ax2.set_ylabel('Neq', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()







