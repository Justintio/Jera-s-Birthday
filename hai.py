import streamlit as st
from PIL import Image

st.title('Hai.')

bener = ['kosong', 'bener', 'salah']
nama = st.selectbox('bener ga hari ini ulang tahun ? ', bener)

if nama == 'salah' :
  st.write('boong lu !')
  
if nama == 'bener' :
  st.title('Happy Birthday Cantik')
  st.write('May all of your wishes will come true')
  
  st.title('  ')
  left_col, mid_col, right_col = st.columns(3)
  image1 = Image.open('jera1.jpeg')
  left_col.image(image1)
  st.title('  ')  
  image2 = Image.open('jera2.jpeg')
  mid_col.image(image2)
  st.title('  ')
  image3 = Image.open('jera3.jpeg')
  right_col.image(image3)
  st.title('  ')
  st.title('Love you')
  st.write('Udah yak gitu aja, gabisa jadi manis ')
  st.write('bisanya mencintaimu ahay ')
