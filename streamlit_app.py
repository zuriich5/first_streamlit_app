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

# We will ask the streamlit library to display it on the page by typing the code below:
streamlit.dataframe(my_fruit_list)
