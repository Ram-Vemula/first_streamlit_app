import streamlit
import pandas as pd
import requests
import snowflake.connector as sfc
from urllib.error import URLError
my_cnx = sfc.connect(**streamlit.secrets["snowflake"])
read_file = pd.read_excel (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData.xlsx')
read_file.to_csv (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData_Convert.csv', index = None, header=True)
