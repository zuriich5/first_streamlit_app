import streamlit # Import streamlit library

streamlit.title ('Hello World!')
streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Import pandas library 
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# read_csv function reads our CSV file from that S3 bucket 
# to pull the data into a dataframe we'll call my_fruit_list. 

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

# New section to display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

# Added text_input function to generate text box
# Added write function to enable input
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Import requests library. Used for making HTTP requests/calls
import requests

# Used the HTTP request GET command
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Specified which fruit to get
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# Added fruit_choice function that we created to get data from user input
fruityvice_response = request.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# Just writes the data on the screen
streamlit.text(fruityvice_response.json())

# Just shows the HTTP response type
streamlit.text(fruityvice_response)

# Using pandas library to read the json file 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Added dataframe function to display it as a table
streamlit.dataframe(fruityvice_normalized)