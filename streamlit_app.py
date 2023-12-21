import streamlit
streamlit.title("My New Healthy Dinner")

streamlit.header("BreakFast Menu")
streamlit.text("Banana")
streamlit.text("bread & butter")
streamlit.text ("Hot Masala Chai")
streamlit.text ("Sandwitch")

import pandas
my_fruit_list  = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe (my_fruit_list)

               
