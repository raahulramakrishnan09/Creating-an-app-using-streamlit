
import streamlit as st
import time
st.write('Hello, *World!* :sunglasses:')
st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3''')
st.image("/content/Dodge_Charger.jpg")
st.audio("/content/you-are-my-hope.wav")
st.checkbox('yes')
st.button('Click')

st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])

st.multiselect('choose a planet',['Jupiter','Mars','Neptune'])
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('Pick a number',0,50)

st.number_input('Pick a number',0,10)
st.text_input('Email address')
st.date_input('Date')
st.time_input('Time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('choose your favorite color')
st.balloons()
st.progress(10)
with st.spinner('loading...'):
    time.sleep(5)
st.success('Done!')