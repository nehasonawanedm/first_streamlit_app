streamlit.title("My Mom's New Healthy Diner")
 
streamlit.header('Breakfast favourites')
streamlit.text('ðŸ¥£ Omega 3 & Blueberry Oatmeal')
streamlit.text('ðŸ¥— Kale, Spinach & Rocket Smoothie')
streamlit.text('ðŸ” Hard-Boiled Free-Range Egg')
streamlit.text('ðŸ¥‘ðŸž Avocada Toast')

streamlit.header('ðŸŒðŸ¥­ Build Your Own Fruit Smoothie ðŸ¥ðŸ‡')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
