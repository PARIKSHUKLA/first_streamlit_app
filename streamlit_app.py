import streamlit
streamlit.title("My New Healthy Dinner")

streamlit.header("BreakFast Menu")
streamlit.text("Banana")
streamlit.text("bread & butter")
streamlit.text ("Hot Masala Chai")
streamlit.text ("Sandwitch")
streamlit.text ("Juice")

import pandas
my_fruit_list  = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + frutit_choice)
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


               
