import streamlit as st
import pandas as pd
#import requests
#import snowflake.connector as sfc
#from urllib.error import URLError
#my_cnx = sfc.connect(**streamlit.secrets["snowflake"])
#read_file = pd.read_excel (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData.xlsx')
#read_file.to_csv (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData_Convert.csv', index = None, header=True)

import os

def file_selector(folder_path='.'):
    filenames = os.listdir(D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data)
    selected_filename = st.selectbox('Select a file', PData.xlsx)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
