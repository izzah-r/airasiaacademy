
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('drive/MyDrive/ColabDataset/Advertising.csv')
df.head()
