import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My New Healthy Dinner")

streamlit.header("BreakFast Menu")
streamlit.text("Banana")
streamlit.text("bread & butter")
streamlit.text ("Hot Masala Chai")
streamlit.text ("Sandwitch")
streamlit.text ("Juice")

#import pandas
my_fruit_list  = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#import requests
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit list contains:")
streamlit.dataframe(my_data_row)
add_my_fruit = streamlit.text_input('What Fruit you would like to add ?' ,'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit')")





               
