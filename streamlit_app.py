import streamlit as st
from PIL import Image
#st.title('SADA APP')

#st.write('Hello world!')

import streamlit as st

# Correct file path as a raw string
image_path = r"C:\Users\best\Desktop\SADA.png"
st.image(image_path, caption="This is SADA!", use_column_width=True)

