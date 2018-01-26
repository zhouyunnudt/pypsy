from __future__ import division, print_function, unicode_literals
from psy import Grm
import numpy as np

scores = np.loadtxt('data/lsat.csv', delimiter=',')
grm = Grm(scores=scores)
print(grm.em())