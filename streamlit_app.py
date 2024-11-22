import streamlit as st
from PIL import Image
#st.title('SADA APP')
#st.write('Hello world!')

# URL to the image on GitHub
image_url = "SADA.png"

# Display the image
st.image(image_url,use_column_width=True)

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# URL to the image on GitHub (replace with your own)
image_url = "SADA.png"

# Open the image from the URL using PIL
image = Image.open("SADA.png")

# Create a draw object to add text
draw = ImageDraw.Draw(image)

# Specify the font and size
try:
    font = ImageFont.truetype("arial.ttf", 50)  # Use a system font (you may need to adjust the font)
except IOError:
    font = ImageFont.load_default()  # Default font if specific one not found

# Set the text, color, and position
text = "This is SADA!"
font_color = (255, 0, 0)  # Red color for the text
position = (100, 100)  # Position (x, y) where the text should be placed

# Add the text to the image
draw.text(position, text, fill=font_color, font=font)

# Display the image in Streamlit with the text overlay
st.image(image, caption="Image with Text Overlay", use_column_width=True)

