# Code Example of Biology ANOVA
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import shapiro
from scipy.stats import bartlett
from scipy.stats import f_oneway

#Data emter
NT = [10, 8, 9, 7, 9, 10, 12]
P1 = [2, 0, 1, 0, 2, 3, 1]
P2 = [6, 6, 5, 4, 7, 6, 5]
P3 = [5, 3, 2, 6, 4, 5, 7]
P4 = [4, 5, 3, 4, 7, 6, 5]
P5 = [1, 0, 0, 2, 1, 2, 1]
#
# Test of normality of Shapiro-Wilk
shapiro(NT)
shapiro(P1)
shapiro(P2)
shapiro(P3)
shapiro(P4)
shapiro(P5)
# 
# Test of homogeneity of Bartlett
bartlett(NT, P1, P2, P3, P4, P5)
#
# ANOVA
f_oneway (NT, P1, P2, P3, P4, P5)
#
# Multiple comparison of Tukey
df = pd.DataFrame({'score': [10, 8, 9, 7, 9, 10, 12, 2, 0, 1, 0, 2, 3, 1, 6, 6, 5, 4, 7, 6, 5, 5, 3, 2, 6, 4, 5, 7, 4, 5, 3, 4, 7, 6, 5, 1, 0, 0, 2, 1, 2, 1], 'group': np.repeat(['NT', 'P1', 'P2', 'P3', 'P4', 'P5'], repeats=7)}) 
#
tukey = pairwise_tukeyhsd(endog=df['score'], groups=df['group'], alpha=0.05)
#
print(tukey)
