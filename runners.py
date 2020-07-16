from scrapers.florida_scraping import download_fl_report, extract_fl_df_from_pdf, write_df_to_csv
from graphers.worldometer_graphing import main as generate_graphs


def run_florida_lab_data():
    path = download_fl_report()
    fl_testing_df = extract_fl_df_from_pdf(path)
    write_df_to_csv(fl_testing_df)
    print('Finished Generating Florida Lab Data')


def run_worldometer_graphing():
    generate_graphs()


if __name__ == '__main__':
    #run_florida_lab_data()
    run_worldometer_graphing()