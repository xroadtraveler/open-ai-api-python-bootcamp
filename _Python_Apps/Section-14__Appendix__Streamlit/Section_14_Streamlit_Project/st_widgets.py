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


# CHECKBOX
agree = st.checkbox('I agree')
if agree:
    'Great, you agreed!'

checked = st.checkbox('Continue', value=True)
if checked:
    ':+1:' * 5

df = pd.DataFrame({'Name': ['Anne', 'Mario', 'Douglas'],
                   'Age': [30, 45, 40]
                   })

if st.checkbox('Show data'):
    st.write(df)

st.divider()


# RADIO
pets = ['cat', 'dog', 'fish', 'turtle']
pet = st.radio('Favorite pet', pets, index=2)
st.write(f'Your favorite pet: {pet}')

st.divider()


# SELECT
cities = ['London', 'Berlin', 'Paris', 'Madrid']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You live in {city}')

st.divider()


# SLIDER
x = st.slider('x', value=15, min_value=12, max_value=78, step=3)
st.write(f'x is {x}')

st.divider()


# FILE UPLOADER
uploaded_file = st.file_uploader('Upload a file:', type=[])



