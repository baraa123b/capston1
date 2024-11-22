import streamlit as st
from PIL import Image

# URL to the image on GitHub
#image_url = "SADA.png"

# Display the image
#st.image(image_url,use_column_width=True)

from PIL import Image, ImageDraw, ImageFont

# Step 1: Load the image
image = Image.open("SADA.png")  # Ensure the image path is correct
draw = ImageDraw.Draw(image)

# Step 2: Get image dimensions
img_width, img_height = image.size

# Step 3: Define static values for text, color, font size, and position
text = "This is SADA!"  # Static text to overlay
font_color = "#FF5733"  # Static color in hex format
font_size = 50  # Static font size
x_position = img_width // 2  # X Position (centered horizontally)
y_position = img_height // 2  # Y Position (centered vertically)

# Step 4: Set font (ensure the font is available on your system)
try:
   font = ImageFont.truetype("arial.ttf", font_size)  # Use Arial font, you can replace it with another font if needed
except IOError:
    font = ImageFont.load_default()  # Use default font if Arial is not available

# Step 5: Convert hex color to RGB
hex_color = font_color.lstrip('#')
font_color_rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Step 6: Draw the text on the image
draw.text((x_position, y_position), text, fill=font_color_rgb, font=font)

# Step 7: Display the modified image
st.image(image, use_column_width=True)



