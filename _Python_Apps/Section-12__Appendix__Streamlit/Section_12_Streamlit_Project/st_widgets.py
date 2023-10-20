import streamlit as st
import pandas as pd

# TEXT INPUT:
name = st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}!')

# NUMBER INPUT:
x = st.number_input('Enter a number: ', min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')

st.divider()

# BUTTON: 
clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:' * 3)

st.divider()

