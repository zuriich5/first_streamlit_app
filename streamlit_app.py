# Import streamlit library
import streamlit
# Import pandas library 
import pandas 
# Import requests library. Used for making HTTP requests/calls
import requests
# The line shown below will tell your app to bring in some code from the snowflake library you added (snowflake-connector-python)
import snowflake.connector
# Library for error handling
from urllib.error import URLError

streamlit.title ('Hello World!')
streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# ----------------------------------------------# Import pandas library 

# read_csv function reads our CSV file from that S3 bucket 
# to pull the data into a dataframe we'll call my_fruit_list. 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# To be able to pick the fruits instead of just numbers
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# Added fruits_selected function name
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Added dataframe loc function to enable filtering on our table
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# streamlit.dataframe(my_fruit_list) , updating the command to the below code to make use of the function
streamlit.dataframe(fruits_to_show)

# ----------------------------------Created function

def get_fruityvice_data(this_fruit_choice):
# Added fruit_choice function that we created to get data from user input
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)

# Using pandas library to read the json file 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Added dataframe function to display it as a table, UPDATED: used return function
    return fruityvice_normalized

# New section to display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

# Added try catch error, if else and function
try:
  
# Added text_input function to generate text box
# Added write function to enable input
  fruit_choice = streamlit.text_input('What fruit would you like information about?')

  if not fruit_choice:
    streamlit.error('Please select a fruit to get information ')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
# streamlit.write('The user entered ', fruit_choice)

# ----------------------------------------------Import requests library. Used for making HTTP requests/calls

# Used the HTTP request GET command
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Specified which fruit to get
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# Just writes the data on the screen
# streamlit.text(fruityvice_response.json())

# Just shows the HTTP response type
# streamlit.text(fruityvice_response)

# ---------------------------------------------- import snowflake.connector will tell your app to bring in some code from the snowflake library you added (snowflake-connector-python)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# streamlist.stop() is used to stop executing code below this command

streamlit.header("View our fruit list - Add your favorites!")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
    # To execute SQL command
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()

# Added button 
if streamlit.button('Get Fruit List'):
# To connect to the secrets settings in Streamlit using the snowflake credentials we added
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# fetchone retrieves one output only, fetchall retrieves all data
    my_data_row = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_row)

# Allowing user to add fruit
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + fruit_name + "')")
        return 'Thank you for adding ' + new_fruit
        
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add fruit'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
