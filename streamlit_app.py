import streamlit
import pandas as p
import requests
import snowflake.connector as sfc
from urllib.error import URLError

streamlit.title('My Parents for New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('Avacado Toast')
streamlit.header('🍌 Build Your Own Fruit Smoothie')

#import pandas as p

my_fruit_list=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
#have to create User Interactive widget so that user can pick the fruits they want in their smoothies
# Put a pick list 
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index)) --- this takes the column1 as indes which is a number, this doesn't make any sense. have to provide the choice to choose the fruits by names. It is required to change the index to 'Fruit'. 
my_fruit_list=my_fruit_list.set_index('Fruit')
# Display the table with pick list option 
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

# We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 
#let's put a pick list so the customer can pick the fruit what they want

#streamlit.dataframe(my_fruit_list)

# we just have to make the table below the picker a bit smarter so it's doesn't load all the fruits, just the ones shown in the pick list

#put the list of selected fruits into a variable 
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#------------------------------------------------------------------------------------
#Making as comments, we have implemented this block with TRY-EXCEPT loop in below 
# streamlit.header("Fruityvice Fruit Advice!")
#adding a text entry box 
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#displaying the user choice 
# streamlit.write('The user entered ', fruit_choice)
# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())   # this writes the data to screen 
#below code is to Normalize the semi structured json data into a flat file
# fruityvice_normalized = p.json_normalize(fruityvice_response.json())
# this is to display a dataframe as a interactive table
# streamlit.dataframe(fruityvice_normalized)   
# -------------------------------------------------------------------------------------------------

# with Try-Except loop 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:  
  streamlit.error("Please select a fruit to get information.")
 else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized = p.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
 except URLError as e:
  streamlit.error()

streamlit.stop()

# import snowflake.connector as sfc

my_cnx = sfc.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_cur.execute("SELECT * from fruit_load_list")

#my_data_row = my_cur.fetchone()

my_data_rows = my_cur.fetchall()

#streamlit.text("The fruit load list containts:")
#streamlit.text(my_data_row)
streamlit.header("The fruit load list containts:")
#streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)

#adding a text entry box 
fruit_choice2 = streamlit.text_input('What fruit would you like to add','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice2)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")







