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
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
# Display the table with pick list option 
streamlit.dataframe(my_fruit_list)
