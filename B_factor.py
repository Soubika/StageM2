#!/usr/bin/env python 3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def trouve_calpha(filename):
    calpha_list = []
    with open(filename,"r") as protein_file:
        for line in protein_file:
            if line[0:6].strip() == 'ATOM' and line[12:16].strip() == 'CA':
                # on stocke la ligne du C-alpha
                # sans le retour à la ligne en fin de ligne
                calpha_list.append(line)
    return calpha_list


calpha = trouve_calpha("I-EGF2.pdb")
print(calpha[:,8:])
