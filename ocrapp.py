import easyocr as ocr  #OCR
import streamlit as st  #Web App
try:
    import Image
except ImportError:
    from PIL import Image

import numpy as np #Image Processing 
import pandas as pd

img= Image.open('5200010.png')
st.set_page_config(page_title='OCR app', page_icon=img)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
<style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#title
st.title("Image to text converter")

st.markdown('#### Optical Character Recognition with EasyOcr')

st.markdown("")

#image uploaded
image = st.file_uploader(label = "Upload the image",type=['png','jpg','jpeg','gif'])

reader = ocr.Reader(['en'])

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 Running "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])
        
        df = pd.DataFrame(result_text)
        
        st.dataframe(df)
