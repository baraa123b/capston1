import streamlit as st
from PIL import Image

# URL to the image on GitHub
#image_url = "SADA.png"

# Display the image
#st.image(image_url,use_column_width=True)

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Function for Page 1
def page_1():
    st.title("Page 1: Image with Text Overlay")
    
    # Load image and overlay text (same as before)
    image = Image.open("SADA.png")  # Replace with your image path
    draw = ImageDraw.Draw(image)
    
    text = "This is SADA!"  # Static text to overlay
    font_color = "#FF5733"  # Text color
    font_size = 50  # Font size
    
    # Set font (ensure it's available)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Use Arial font
    except IOError:
        font = ImageFont.load_default()  # Default font if Arial not available
    
    text_width, text_height = draw.textsize(text, font=font)
    
    # Center the text
    x_position = (image.width - text_width) // 2
    y_position = (image.height - text_height) // 2
    
    # Draw text on the image
    font_color_rgb = tuple(int(font_color[i:i+2], 16) for i in (0, 2, 4))  # Convert hex to RGB
    draw.text((x_position, y_position), text, fill=font_color_rgb, font=font)
    
    # Display the image
    st.image(image, caption="Image with Text Overlay", use_column_width=True)

# Function for Page 2
def page_2():
    st.title("Page 2: Custom Content")
    st.write("This is the second page of the app. You can add other content here.")
    # Add custom content for page 2

# Main function to handle navigation
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a Page", ["Home", "Page 1", "Page 2"])
    
    # Display page content based on the selected option
    if page == "Home":
        st.title("Welcome to the Home Page")
        st.write("This is the home page of the Streamlit app.")
    elif page == "Page 1":
        page_1()
    elif page == "Page 2":
        page_2()

if __name__ == "__main__":
    main()
