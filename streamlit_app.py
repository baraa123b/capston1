import streamlit as st
from PIL import Image
#st.title('SADA APP')
#st.write('Hello world!')

# URL to the image on GitHub
#image_url = "SADA.png"

# Display the image
#st.image(image_url,use_column_width=True)


from PIL import Image, ImageDraw, ImageFont


# Load the image
image = Image.open("SADA.png")
draw = ImageDraw.Draw(image)

# Get image dimensions
img_width, img_height = image.size

# Add text input and color picker for position and color
text = st.text_input("Enter text:", "This is SADA!")
font_color = st.color_picker("Pick a text color", "#FF0000")  # Default Red
font_size = st.slider("Font Size", 10, 100, 50)  # Adjust font size
x_position = st.slider("X Position", 0, img_width, img_width // 2)  # Horizontal position
y_position = st.slider("Y Position", 0, img_height, img_height // 2)  # Vertical position

# Set font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

# Convert hex color to RGB
hex_color = font_color.lstrip('#')
font_color_rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Draw text on image
draw.text((x_position, y_position), text, fill=font_color_rgb, font=font)




