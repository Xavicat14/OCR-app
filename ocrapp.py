import easyocr as ocr  #OCR
import streamlit as st  #Web App
try:
    import Image
except ImportError:
    from PIL import Image

import numpy as np #Image Processing 
import io
import pandas as pd
import base64


img= Image.open('C:/Users/xavie/OneDrive/Desktop/5200010.png')
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

#image uploade
image = st.file_uploader(label = "Upload the image",type=['png','jpg','jpeg','gif'])


@st.cache
def reader(): 
    reader = ocr.Reader(['en','es','hu'])
    return reader 


reader = reader() #load model

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
    

        towrite = io.BytesIO()
        downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
        towrite.seek(0)  # reset pointer
        b64 = base64.b64encode(towrite.read()).decode() 
        linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="ocr.xlsx">Download text in excel file</a>'
        st.markdown(linko, unsafe_allow_html=True)





