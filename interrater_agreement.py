import pandas as pd
from krippendorff import krippendorff
from nltk import agreement


def read_file(name):
    return pd.read_csv(name)


def preprocess_rates(df):
    emojis = df['emoji'].to_numpy()
    length = len(emojis)
    rates = []
    for i in range(0, 10):
        rater = []
        for j in range(i, length, 10):
            rater.append(emojis[j])
        rates.append(rater)
    kappa = krippendorff.alpha(rates)
    return rates


def convert_to_higher_categories(rates):
    for j in range(0, 10):
        for index, i in enumerate(rates[j]):
            if i == 2 or i == 3 or i == 4 or i == 6 or i == 7 or i == 0 or i == 1 or i == 11 \
                    or i == 13 or i == 5 or i == 8 or i == 9:
                rates[j][index] = 0
            elif i == 16 or i == 18:
                rates[j][index] = 1
            elif i == 22 or i == 14 or i == 19 or i == 15:
                rates[j][index] = 2
            elif i == 21 or i == 20 or i == 17:
                rates[j][index] = 3
            elif i == 23 or i == 24 or i == 25:
                rates[j][index] = 4
            elif i == 12 or i == 26 or i == 27 or i == 28 or i == 10:
                rates[j][index] = 5
    return rates


def rater_agreement(rates):
    taskdata = []
    ratingtask = None
    for j in range(0, 10):
        taskdata += [[j, i, rates[j][i]] for i in range(len(rates[j]))]
        ratingtask = agreement.AnnotationTask(data=taskdata)
    return ratingtask


if __name__ == '__main__':
    name = 'result.csv'
    df = pd.read_csv(name)
    rates = preprocess_rates(df)
    rates = convert_to_higher_categories(rates)
    ratingtask = rater_agreement(rates)

    print("kappa " + str(ratingtask.kappa()))
    print("fleiss " + str(ratingtask.multi_kappa()))
    print("alpha " + str(ratingtask.alpha()))
    print("scotts " + str(ratingtask.pi()))
