import streamlit

streamlit.title("My Mom's New Healthy Diner")
 
streamlit.header('Breakfast favourites')
streamlit.text('ðŸ¥£ Omega 3 & Blueberry Oatmeal')
streamlit.text('ðŸ¥— Kale, Spinach & Rocket Smoothie')
streamlit.text('ðŸ” Hard-Boiled Free-Range Egg')
streamlit.text('ðŸ¥‘ðŸž Avocada Toast')

streamlit.header('ðŸŒðŸ¥­ Build Your Own Fruit Smoothie ðŸ¥ðŸ‡')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list1 = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list1.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list1)

fruits_to_show = my_fruit_list1.loc['Apple']
streamlit.dataframe(fruits_to_show)
