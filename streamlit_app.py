import streamlit as st
from PIL import Image
#st.title('SADA APP')

#st.write('Hello world!')

# Title
#st.title("Display Local Image")

# Display the image from your desktop
image_path = "C:\Users\best\Desktop\SADA.png"  # Replace with your image path
st.image(image_path, caption="This is SADA!", use_column_width=True)


