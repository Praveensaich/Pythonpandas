import pandas
import streamlit
streamlit.header(" Table of Fruits ")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
stremlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
streamlit.dataframe( my_fruit_list )
