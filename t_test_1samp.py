import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import os
import csv
from matplotlib import pyplot as plt

# import seaborn as sns
# sns.set()

# 表示桁数の指定
# %precision 3
# グラフをjupyter Notebook内に表示させるための指定
# %matplotlib inline

""
2群のデータに対する，対応のあるt検定
""
print("ファイル名を入力してください：")
filename = input()
data = pd.read_csv(filename + ".csv")

f = open('result.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
label = ['statictics', 'pvalue']
writer.writerow(label)


before = data['before']
after = data['after']

statictics, pvalue = stats.ttest_rel(after, before)
list = [statictics, pvalue]
writer.writerow(list)

f.close()
