import streamlit
streamlit.title('My Parents for New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('Avacado Toast')
streamlit.header('🍌 Build Your Own Fruit Smoothie')
#importing PANDAS 
import pandas as p
my_fruit_list=p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
#have to create User Interactive widget so that user can pick the fruits they want in their smoothies
# Put a pick list 
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))  
# Display the table with pick list option 
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index)) --- this takes the column1 as indes which is a number, this doesn't make any sense. have to provide the choice to choose the fruits by names. It is required to change the index to 'Fruit'. 

my_fruit_list=my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avacado','Strawberries'])
#streamlit.dataframe(my_fruit_list)
# We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer. 
#let's put a pick list so the customer can pick the fruit what they want

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

streamlit.dataframe(my_fruit_list)

# we just have to make the table below the picker a bit smarter so it's doesn't load all the fruits, just the ones shown in the pick list
