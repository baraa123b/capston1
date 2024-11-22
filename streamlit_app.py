import streamlit as st
from PIL import Image
#st.title('SADA APP')

#st.write('Hello world!')

import streamlit as st

# URL to the image on GitHub
image_url = "https://raw.githubusercontent.com/username/repository/main/images/SADA.png"

# Display the image
st.image(image_url, caption="This is SADA!", use_column_width=True)
