#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')

#data = np.loadtxt("rmsf_IEGF2_global_1_7.txt")
#data = open("rmsf_IEGF2_global_1_7.txt", "r")

x1 = [1,2,3,4,5]
x2 = [4,2,1,6,7]
n, bins, patches = plt.hist(x1, 51, normed = 1, facecolor='b', alpha=0.5)
plt.show()

