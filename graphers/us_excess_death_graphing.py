import pandas as pd

CDC_URL = 'https://data.cdc.gov/api/views/xkkf-xrst/rows.csv?accessType=DOWNLOAD&bom=true&format=true%20target='


def get_cdc_df(link):
    return pd.read_csv(link)


if __name__ == '__main__':
    excess_deaths_df = get_cdc_df(CDC_URL)

    test_df = excess_deaths_df.loc(excess_deaths_df['Outcome'] == "All causes, excluding COVID-19")

    print(test_df.head())