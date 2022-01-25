import streamlit as st
from PIL import Image

st.title('Hai.')
st.write('Happy Birthday Cantikku')

left_col, mid_col, right_col = st.columns(3)
image1 = Image.open('jera1.jpeg')
left_col.image(image1)
