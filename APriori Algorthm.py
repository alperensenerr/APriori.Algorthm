import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

#Thanks to 'Yu Mochizuki' for algorthm

veriler = pd.read_csv('sepet.csv', header = None)

t = []
for i in range (0,7501):
    t.append([str(veriler.values[i,j]) for j in range (0,19)])

kurallar = apriori(t,min_support=0.01, min_confidence=0.2, min_lift = 3, min_length=4)

print(list(kurallar))
# we see that if some one buy herb & pepper it is 3.29 times more likely to buy ground beef
