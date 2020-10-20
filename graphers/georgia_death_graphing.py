import pandas as pd
import plotly.express as px


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

    fig = px.box(
        y=deaths_list_clean,
        title="Georgia COVID-19 Deaths"
    )
    fig.show()


if __name__ == '__main__':
    create_georgia_boxplot()