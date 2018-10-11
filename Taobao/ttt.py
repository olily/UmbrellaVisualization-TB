import pandas as pd
import seaborn as sns
import numpy.random as nr
import matplotlib.pyplot as plt

import numpy as np; np.random.seed(8)
mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
x, y = np.random.multivariate_normal(mean, cov, 80).T
ax = sns.regplot(x=x, y=y, color="g", marker="+")

