
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a title")
st.text("This is a text")
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")
st.markdown("#### This is a markdown")
st.header("This is a header")
st.subheader("This is a subheader")

# success - info - error
st.success("This is a success message!")
st.info("This is a purely info message")
st.error("This is an error")

# help
st.help(range)

# write
st.write("Hello")

# image
img = Image.open("images.jpeg")
st.image(img, caption="can")

img = Image.open("images.jpeg")
st.image(img, width=300,caption="Can")

# video
#my_video = open("ml.mov",'rb')
#st.video(my_video)
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

# Checkbox
cbox = st.checkbox("Hide and Seek")

if cbox:
    st.text("Hide")
else:
    st.write("Seek")

# Radio Buttons
status = st.radio("Select a color", ("Blue", "Orange", "Yellow"))
                                          
if status == 'Blue':
    st.write("Your color is Blue")
elif status == 'Orange':
    st.write("Your color is Orange")
else:
    st.write("Your color is Yellow")


status = st.radio("Select a color", ("blue", "orange", "yellow"))
st.write("Your favourite color is", status)

# Button
if st.button('Press me!'):
    st.success('Wellcome to the DS world!')

# SelectBox ####
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write("You selected this option", occupation)

selected_number = st.selectbox('Select a number', [0, 1, 2, 3, 4, 5])
if selected_number == 0:
    st.write('No cats for you -.-')
else:
    st.write(f'I am sending you {selected_number} cats')

# Multiselect
location = st.multiselect("Where do you work?", ("London", "New York", "Accra", "Kiev", "Nepal"))
st.write("You selected", len(location), "locations")

multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

# Slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)

st.slider('Select a number', 0, 10, 2, 2)  # start, stop, default, step

st.slider("Select a number", 0., 5., 3., 0.1)

st.slider("Select a number", )  # Hiç bir değer girmeyince default lar ile görüntüledi.

st.write("option2")
option2 = st.slider("Select a number", min_value=5, max_value=80, value=30, step=5)
st.write("option3")
option3 = st.slider("Select a number", min_value=10, max_value=60, value=30, step=5)
result = option2 * option3
st.write("Result is:", result)

# text input
name = st.text_input("Enter your name", placeholder="Your name here")

if st.button("Submit"):
    st.write("Your name is", name.title())

# code
st.code('import pandas as pd')
st.code('import pandas as pd \nimport numpy as np')

# echo
with st.echo():
    import numpy as np
    import pandas as pd
    df = pd.DataFrame({'a':[1, 2, 3], 'b':[4, 5, 6]})
    df

# date input
import datetime
today = st.date_input('Enter the date:')
hour = st.date_input('Enter the hour:', datetime.datetime.now())

# time input
st.time_input("Time is")
st.time_input('Hour:', datetime.datetime.now())
st.time_input('Select Hour:', datetime.time(12,0))

# sidebar
st.sidebar.title("sidebar title")
st.sidebar.header("Sidebar header")
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)

# dataframe
df = pd.read_csv("Advertising.csv", nrows=(100))
st.table(df.head())
st.write(df.head())
st.dataframe(df.head())



#Project Example with Advertising Data
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))
st.write(df.describe())

# Burada prediction için TV, radio ve newspaper için değer girişi yapıyoruz.
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)  # slider ve number_input aynı işlemi yapıyor
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

# Kullanıcının girdiği verileri dict e çeviriyoruz
my_dict = {
    "TV": TV,
    "radio": radio,
    "newspaper": newspaper,
}

# Oluşturulan DICT ile DARAFRAME oluşturuyoruz
df=pd.DataFrame.from_dict([my_dict])

# DF i streamlit ile yazdırıyoruz
st.table(df)

# Burada yeni DF ile PREDICTION yapıyoruz.
if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])
