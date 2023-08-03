import pandas
import streamlit
streamlit.header("Table of Fruits ")
my_fruits = pandas.readcsv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits)
