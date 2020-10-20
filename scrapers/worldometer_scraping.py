from bs4 import BeautifulSoup
import pandas as pd
import requests
import constants


def get_worldometer_world_data():
    html = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(html, 'lxml')

    data_table = soup.find_all('table')[0]
    rows = data_table.find_all('tr')

    data = []

    for index, row in enumerate(rows):
        if index == 0:
            pass
        else:
            row_data = []
            cols = row.find_all('td')
            if cols[0].text == '':
                pass
            else:
                for col_pos, col in enumerate(cols):
                    try:
                        row_data.append(int(col.text.replace(',', '')))
                    except ValueError:
                        row_data.append(col.text)

                data.append(row_data)

    country_df = pd.DataFrame(data, columns=constants.ALL_COUNTRIES_DF_HEADERS).set_index('Rank')

    return country_df


def get_worldometer_us_data():
    html = requests.get('https://www.worldometers.info/coronavirus/country/us').text
    soup = BeautifulSoup(html, 'lxml')

    data_table = soup.find_all('table', id='usa_table_countries_today')[0]
    rows = data_table.find_all('tr')

    data = []

    for index, row in enumerate(rows):
        if index in [0, 1, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]:
            pass
        else:
            row_data = []
            cols = row.find_all('td')
            for col_pos, col in enumerate(cols):
                value = col.text.strip('\n').strip()
                try:
                    row_data.append(int(value.replace(',', '')))
                except ValueError:
                    row_data.append(value)

            data.append(row_data)

    us_state_df = pd.DataFrame(data, columns=constants.US_STATES_DF_HEADERS).set_index('Rank')

    return us_state_df


if __name__ == "__main__":
    print(get_worldometer_us_data())
