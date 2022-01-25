import streamlit as st
from PIL import Image

st.title('Hai.')

bener = ['kosong', 'bener', 'salah']
nama = st.selectbox('bener ga hari ini ulang tahun ? ', bener)

if nama == 'salah' :
  st.write('boong lu !')
  
if nama == 'bener' :
  st.title('Happy Birthday Sayang')
  st.write('semoga panjang umur')
  st.write('sehat selalu')
  st.write('tambah kaya')
  st.write('tambah pintar')
  st.write('makin cantik')
  st.write('makin sayang ama gua')
  st.write('ya pokonya makin makin lah yek')
  
  st.write('nih gua kasi poto potolu spesial engga lagi kena bug wkkw :')


  image1 = Image.open('jera1.jpeg')
  st.image(image1)
  st.write(' "cantik bgt pacar sapa ni" ')
  st.title('  ')  
  image2 = Image.open('jera2.jpeg')
  st.image(image2)
  st.write('bokem :3')
  st.title('  ')
  image3 = Image.open('jera3.jpeg')
  st.image(image3)
  st.write('beh manis kek garem')
  st.title('')
  st.write('May all of your wishes will come true')
  st.title('  ')
  st.title('Love you')
  st.write('Udah yak gitu aja, gabisa jadi manis ')
  st.write('bisanya mencintaimu ahay ')
