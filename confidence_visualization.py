import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_file(name):
    return pd.read_csv(name)


def check_emoji_set():
    a = df['emoji'].unique()
    print(sorted(a))


def calculate_confidence():
    confidence = df['confidence'].value_counts()[:n].sort_values(ascending=False)
    print('confidence', confidence)
    print('mean:', df['confidence'].mean())


def calculate_mean(df):
    df = df.iloc[:, 2:4]
    df_mean = df.groupby('emoji')
    df_mean.mean().to_csv('mean.csv')
    print(df.mean())
    return df_mean


def draw_plot(df_mean):
    my_colors = 'rgbkymc'
    plt.figure()
    df_mean.mean().plot(kind='bar', color=my_colors, legend=False, width=0.8, figsize=(30, 10))
    plt.ylabel('Mean confidence', fontsize=20)
    plt.ylim(top=5)
    plt.yticks(np.arange(0, 5.5, step=0.5), fontsize=20)
    plt.xticks(fontsize=20)
    plt.xlabel('Emoji id', fontsize=20)
    plt.show()


if __name__ == '__main__':
    name = 'result.csv'
    df = pd.read_csv(name)
    df_mean = calculate_mean(df)
    draw_plot(df_mean)
