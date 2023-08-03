import streamlit
import pandas
streamlit.title(" Swiggy Instamart ")
streamlit.header(" Items ")
streamlit.text(" Cakes ")
streamlit.text(" Drinks ")
streamlit.text(" Chocolates ")
streamlit.header("Fruits")
fruits = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits = fruits.set_index('Fruit')
streamlit.multiselect("Pick a Fruit: ", list(fruits.index),["Apple","Avocado"])
streamlit.dataframe(fruits)


