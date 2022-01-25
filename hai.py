import streamlit as st
from PIL import Image

st.title('Hai.')

bener = ['kosong', 'bener', 'salah']
nama = st.selectbox('bener ga hari ini ulang tahun ? ', bener)

if bener == 'salah' :
  st.write('boong lu !')
  
if bener == 'bener' :
  st.write('Happy Birthday Cantikku')

  left_col, mid_col, right_col = st.columns(3)
  image1 = Image.open('jera1.jpeg')
  left_col.image(image1)
  image2 = Image.open('jera2.jpeg')
  mid_col.image(image2)
  image3 = Image.open('jera3.jpeg')
  right_col.image(image3)
