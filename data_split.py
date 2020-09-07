import os

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(os.path.join('raw', 'train.csv'))
train_df, test_df = train_test_split(df, test_size=0.15, stratify=df.target)

os.makedirs('data', exist_ok=True)
train_df.to_csv(os.path.join('data', 'train.csv'), index=False)
test_df.to_csv(os.path.join('data', 'test.csv'), index=False)
