#import streamlit as st
#st.write('Hello world!')

#st.header('st.button')

#if st.button('Say hello'):
#    st.write('Why hello there')
#else:
#    st.write('Goodbye')

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

#Example 1

st.write('Hello, *World!* :sunglasses:')

#Example 2

st.write(1234)

#Example 3

df = pd.Dataframe({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)

#Example 4

st.write('Below is a Dataframe:', df, 'Above is a Dataframe.')

#Example 5

df2 = pd.Dataframe(
    np.random.randn(200, 3),
    columns = ['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', sixe = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
st.write(c)