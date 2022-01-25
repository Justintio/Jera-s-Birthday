import streamlit as st
from PIL import Image

st.title('Hai.')
st.write('Happy Birthday Cantikku')

left_col, mid_col, right_col = st.columns(3)
image1 = Image.open('jera1.jpeg')
st.left_col.image(image1)
image2 = Image.open('jera2.jpeg')
st.mid_col.image(image2)
image3 = Image.open('jera3.jpeg')
st.right_col.image(image3)
