import pandas as pd


def read_file(name):
    return pd.read_csv(name)


def count_occurrence(df, n):
    return df['emoji'].value_counts()[:n].sort_values(ascending=False)


def check_emoji_set(df):
    a = df['emoji'].unique()
    print(sorted(a))


if __name__ == '__main__':
    name = 'result.csv'
    df = pd.read_csv(name)
    n = 28
    print(count_occurrence(df, n))
