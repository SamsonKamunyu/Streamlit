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

import streamlit as st

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

import streamlit as st
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

import streamlit as st

st.title('st.secrets')

st.write(st.secrets['abcde'])
