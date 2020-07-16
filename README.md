# various_covid_utilities
Various state scrapers and data visualizations for COVID-related data mining in the U.S.

Requirements:


  1. Python version 3.x
  2. Java 8+ (for Tabula)

To install: 


  (Optional) Create a virtual environment (google) if you want an instanced install
  1. From the cmd line either within your activated virtual environment or outside of it, navigate to the root of this various_covid_utilities directory and type:
  
    pip install -r requirements.txt
    
To run Florida Lab Testing Scraper Utility:


  1. Navigate to the root of this various_covid_utilities directory and type:
  
    python scrapers/florida_scraping.py
    
    
  2.  This will generate 2 files:
  - A PDF pull date-marked today in state_data/florida/report_pulls
  - A CSV date-marked in state_data/florida/fl_csv_daily_files

Misc:
- If you aren't interested in the csv output and would instead liek to work directly with a pandas dataframe, you can use the return (pd.DataFrame) from extract_fl_df_from_pdf(path-to-pdf)
- If the number of pages needing to be scraped changes in the daily report, simply copy the 'tabula_templates\fl_summary_pdf_2020-07-16.tabula-template.json' file and edit its entries to include more/less pages
  
