#import streamlit as st
#st.write('Hello world!')

#st.header('st.button')

#if st.button('Say hello'):
#    st.write('Why hello there')
#else:
#    st.write('Goodbye')

#import numpy as np
#import altair as alt
#import pandas as pd
#import streamlit as st

#st.header('st.write')

#Example 1

#st.write('Hello, *World!* :sunglasses:')

#Example 2

#st.write(1234)

#Example 3

#df = pd.DataFrame({
 #   'first column': [1, 2, 3, 4],
  #  'second column': [10, 20, 30, 40] })

#st.write(df)

#Example 4

#st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

#Example 5

#df2 = pd.DataFrame(
 #   np.random.randn(200, 3),
  #  columns = ['a', 'b', 'c'])
#c = alt.Chart(df2).mark_circle().encode(
 #   x = 'a', y = 'b', sixe = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
#git st.write(c)


#import streamlit as st

#st.header('st.checkbox')

#st.write ('What would you like to order?')

#icecream = st.checkbox('Ice cream')
#coffee = st.checkbox('Coffee')
#cola = st.checkbox('Cola')
#tea = st.checkbox('tea')

#if icecream:
#     st.write("Great! Here's some more 🍦")

#if coffee: 
#     st.write("Okay, here's some coffee ☕")

#if cola:
 #    st.write("Here you go 🥤")

#if tea:
#     st.write("Devs take coffee!")


#import streamlit as st
#import pandas as pd
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

#st.header('`streamlit_pandas_profiling`')

#df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

#pr = df.profile_report()
#st_profile_report(pr)

#st.header('st.latex')

#st.latex(r'''
 #    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
  #   \sum_{k=0}^{n-1} ar^k =
   #  a \left(\frac{1-r^{n}}{1-r}\right)
    # ''')

#st.title('Customizing the theme of Streamlit apps')

#st.write('Contents of the `.streamlit/config.toml` file of this app')

#st.code("""
#[theme]
#primaryColor="#F39C12"
#backgroundColor="#2E86C1"
#secondaryBackgroundColor="#AED6F1"
#textColor="#FFFFFF"
#font="monospace"
#""")

#number = st.sidebar.slider('Select a number:', 0, 10, 5)
#st.write('Selected number from slider widget is:', number)

#[theme]
#primaryColor="#F39C12"
#backgroundColor="#2E86C1"
#secondaryBackgroundColor="#AED6F1"
#textColor="#FFFFFF"
#font="monospace"


#import streamlit as st

#st.title('st.secrets')

# Everything is accessible via the st.secrets dict:

#st.write("DB username:", st.secrets["db_username"])
#st.write("My cool secrets:", st.secrets["my_cool_secrets"]["I_like"])

# And the root-level secrets are also accessible as environment variables:

#import os
#st.write(
#	"Has environment variables been set:",
#	os.environ["db_username"] == st.secrets["db_username"])

#import streamlit as st
#import pandas as pd

#st.title('st.file_uploader')

#st.subheader('Input CSV')
#uploaded_file = st.file_uploader("Choose a file")

#if uploaded_file is not None:
  #df = pd.read_csv(uploaded_file)
  #st.subheader('DataFrame')
  #st.write(df)
  #st.subheader('Descriptive Statistics')
 # st.write(df.describe())
#else:
#  st.info('Upload a CSV file')


import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Nyama Choma', 'Mukimo', 'Ugali Sukuma', 'Samaki', 'Ratish'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
