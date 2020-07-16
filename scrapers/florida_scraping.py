import datetime
from pathlib import Path
import requests
import tabula
import pandas as pd

today = datetime.datetime.today().date()


def download_fl_report():
    """
    Takes a snapshot of the FL covid report for the day that this utility was run and saves it in the report_pulls
    directory

    :return: str file path of written file
    """

    URL = 'http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/state_reports_latest.pdf'

    response = requests.get(URL)

    filename = Path('../state_data/florida/report_pulls/fl_summary_pdf_{}.pdf'.format(today))
    filename.write_bytes(response.content)

    return '../state_data/florida/report_pulls/fl_summary_pdf_{}.pdf'.format(today)


def extract_fl_df_from_pdf(file_path='../state_data/florida/report_pulls/fl_summary_pdf_{}.pdf'.format(today)):
    """
    Pulls the pdf from the report_pulls directory and uses tabula-py to create a list of pandas dataframes.
    Then iterates over those dataframes to clean input (remove mixed header/NaN first 2 rows) and concatenates
    them to single dataframe

    :param file_path: the string path to the pdf file you want analyzed
    :return: pandas.DataFrame
    """

    COLUMNS = ['Reporting Lab', 'Inconclusive', 'Negative', 'Positive', 'Percent Positive', 'Total']

    lab_stats_df_list = tabula.read_pdf_with_template(
        input_path=file_path,
        template_path='../tabula_templates/fl_summary_pdf_2020-07-16.tabula-template.json'
    )

    # Removing junk header/NaN rows from each parsed dataframe
    lab_testing_df = pd.concat(df.drop([0, 1]) for df in lab_stats_df_list)
    lab_testing_df.columns = COLUMNS

    return lab_testing_df


def write_df_to_csv(df, file_path='../state_data/florida/fl_csv_daily_files/lab_testing_data_{}.csv'.format(today)):
    """
    Write pandas dataframe to csv

    :param df: a pandas.DataFrame object
    :param file_path: the desired filepath for your output csv
    :return: the relative path to the file from the execution of this script
    """
    df.to_csv(file_path, index=False)
    return '../state_data/florida/fl_csv_daily_files/lab_testing_data_{}.csv'.format(today)


if __name__ == '__main__':
    path = download_fl_report()
    fl_testing_df = extract_fl_df_from_pdf(path)
    write_df_to_csv(fl_testing_df)