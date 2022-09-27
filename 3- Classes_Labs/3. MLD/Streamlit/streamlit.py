# https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from PIL import Image

st.title('Hello World')

st.text('StreamLit text')

st.markdown('Markdown')
st.markdown('`Markdown`')

st.header('Header')
st.subheader('SubHeader')

st.success('Success! Congrats.')
st.info('Info! Warning!!!')
st.error('Error!!!')

st.help(range)
st.help('string')
st.write('This is a text written with write function, it can write even a dataframe.')
img = Image.open('asim.JPG')
st.image(img, caption='Asim', use_column_width=True)

my_video = open('Ezan.webm', 'rb')
st.video(my_video)

# st.video('‪D:\Ezan.webm') 

#Checkbox
if st.checkbox('Hide and Seek'):
    st.write('Seek')
    
# st.radio('What is your favourite colour?', ('Red', 'Green', 'Blue'))

status = st.radio('What is your favourite colour?', ('Red', 'Green', 'Blue'))
st.write(f'Your favourite colour is {status}')

if st.button('Click it!'):
    st.success('big brain move')
    
#SelectBox
selected_number = st.selectbox('Select a number', [0, 1, 2, 3, 4, 5])
if selected_number == 0:
    st.write('No cats for you -.-')
else:
    st.write(f'I am sending you {selected_number} cats')
    
multi_select = st.multiselect('Select multiple numbers', [0, 1, 2, 3, 4, 5])
if len(multi_select) > 0:
    st.write(f'you selected {multi_select}')
else:
    st.write('You didnt select anything')
    
st.slider('Select a number', 0, 10, 2, 2)  # start, stop, default, step

st.slider("Select a number", 0., 5., 3., 0.1)

name = st.text_input('Enter your name')

if st.button('Submit'):
    st.write(f'Hello, {name.title()}')
    
st.text_area('Enter a message1:', 'type your message right here...')  # with default message
st.text_area('Enter a message2:', placeholder='type your message right here...')  # with default message
st.date_input('Date:', datetime.datetime.now())
st.time_input('Hour:', datetime.datetime.now())
st.time_input('Select Hour:', datetime.time(12,0))

birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', birthday)

st.code('import pandas as pd \nimport numpy as np')

with st.echo():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame({'a':[1, 2, 3], 'b':[4, 5, 6]})
    df

#### sidebar ####

st.sidebar.title('Hello World')
st.sidebar.text('StreamLit text')

#### sidebar ####

df = pd.read_csv('Mall_Customers.csv')
st.table(df.head())
st.write(df.head())
st.dataframe(df.head())
st.sidebar.dataframe(df.tail())

st.line_chart(df['Age'])
st.sidebar.line_chart(df['Age'][:50])

x = st.slider('x')
st.line_chart(df['Age'].sample(x))

