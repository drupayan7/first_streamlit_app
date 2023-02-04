import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🍜Breakfast Menu')
streamlit.text('🥗Omega 3 and Blueberry Oatmeal')
streamlit.text('🍗Kale, Spinch & Rocket Smoothie')
streamlit.text('🌮🥑Hard-Boiled Free Range Egg')


streamlit.header('🍜🌮 Build Your Own Fruit Smoothie 🥗🍌')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
