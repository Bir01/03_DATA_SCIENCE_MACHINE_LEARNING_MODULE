# https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from PIL import Image

#### Text/Title ####
st.title("Streamlit Tutorials")

st.text("Hello Streamlit")

#### Header/Subheader ####
st.header("This is a header")
st.subheader("This is a subheader")

#### Markdown ####
st.markdown("### This is a Markdown")
st.markdown('`This is a Markdown`')

#### Error/Colorful Text ####
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

#### Get Help Info About Python ####
st.help(range)
st.help('string')

#### Writing Text ####
st.write('This is a text written with write function, it can write even a dataframe.')
st.write(range(10))

#### Images ####
from PIL import Image
img = Image.open("Clarusway_Logo.JPG")
st.image(img, width=300,caption="Clarusway")

img = Image.open('Clarusway_Logo.JPG')
st.image(img, caption='Clarusway', use_column_width=True)

#### Videos ####
vid_file = open("Clarusway_Info.mp4", "rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

#### Audio ####
audio_file = open("Kelebekler De Ağlar.mp3","rb").read()
st.audio(audio_file, format="audio/mp3")

#### Widget ####
# https://docs.streamlit.io/library/api-reference/widgets

#### Checkbox ####
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")
    st.write('Seek')

#### Radio Buttons ####
status = st.radio("What is your status", ("Active", "Inactive"))
                                          
if status == 'Active':
     st.success("You are active")
else:
     st.warning("Inactive, Activate")


status = st.radio('What is your favourite colour?', ('Red', 'Green', 'Blue'))
st.write(f'Your favourite colour is {status}')

if st.button('Click it!'):
    st.success('big brain move')

#### SelectBox ####
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write("You selected this option", occupation)


selected_number = st.selectbox('Select a number', [0, 1, 2, 3, 4, 5])
if selected_number == 0:
    st.write('No cats for you -.-')
else:
    st.write(f'I am sending you {selected_number} cats')

#### Multiselect ####
location = st.multiselect("Where do you work?", ("London", "New York", "Accra", "Kiev", "Nepal"))
st.write("You selected", len(location), "locations")


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



















