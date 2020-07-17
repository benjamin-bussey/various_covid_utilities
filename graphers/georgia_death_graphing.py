import pandas as pd
import matplotlib.pyplot as plt


def create_georgia_boxplot():
    df_deaths = pd.read_csv('../state_data/georgia/ga_covid_data/deaths.csv')
    df_deaths_age = df_deaths.pop('age')

    deaths_list_raw = df_deaths_age.tolist()
    deaths_list_clean = []

    for death in deaths_list_raw:
        if death == '90+':
            deaths_list_clean.append(90)
        elif death == '.':
            pass
        else:
            try:
                deaths_list_clean.append(int(death))
            except:
                print(death)

    red_square = dict(markerfacecolor='r', marker='s')
    fig, ax = plt.subplots()
    ax.set_title('Georgia COVID-19 Deaths')
    ax.set_ylabel('Deaths')
    ax.set_xlabel('Age')

    ax.boxplot(deaths_list_clean, vert=False, flierprops=red_square)
    fig.show()


if __name__ == '__main__':
    create_georgia_boxplot()