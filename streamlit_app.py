import streamlit as st
from PIL import Image
#st.title('SADA APP')

#st.write('Hello world!')

import streamlit as st

# Relative path to the image inside the 'images' folder
image_path = "images/SADA.png"  # Use the path relative to your script

# Display the image
st.image(image_path, caption="This is SADA!", use_column_width=True)

