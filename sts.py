import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics as st
from collections import Counter
sns.set(style="darkgrid")

def central_tendency(column):
  data = {}
  data['Column'] = column.name
  data['Mean'] = st.mean(column)
  data['Mode'] = Counter(column).most_common()[0][0]
  data['Median'] = st.median(column)
  return pd.DataFrame([data])

def dispersion(column):
  data = {}
  data['Column'] = column.name
  data['Variance'] = st.variance(column)
  data['Standard Deviation'] = st.stdev(column)
  data['Skew'] = column.skew()
  return pd.DataFrame([data])

def plot_distribution(column):
  f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, figsize=(10, 6),
                                      gridspec_kw={"height_ratios": {0.2, 1}})
  
  info = central_tendency(column)
  mean = info['Mean'].values[0]
  median = info['Median'].values[0]
  mode = info['Mode'].values[0]

  sns.boxplot(x=column, ax=ax_box)
  ax_box.axvline(mean, color='r', linestyle='--')
  ax_box.axvline(median, color='g', linestyle=':')
  ax_box.axvline(mode, color='b', linestyle='-')
  ax_box.set(xlabel='')

  sns.histplot(x=column, ax=ax_hist, kde=True)
  ax_hist.axvline(mean, color='r', linestyle='--')
  ax_hist.axvline(median, color='g', linestyle=':')
  ax_hist.axvline(mode, color='b', linestyle='-')

  plt.legend({'Mean':mean, 'Median':median, 'Mode':mode})
  plt.show()

def find_outlier(column):
  Q1 = column.quantile(0.25)
  Q3 = column.quantile(0.75)
  IQR = Q3 - Q1
  outliers = []

  for data in column:
    if (data > (Q3 + 1.5 * IQR)) | (data < (Q1 - 1.5 * IQR)):
      outliers.append(data)

  return outliers
