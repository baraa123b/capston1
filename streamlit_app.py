import streamlit as st
from PIL import Image

# URL to the image on GitHub
#image_url = "SADA.png"

# Display the image
#st.image(image_url,use_column_width=True)

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Function for Home Page
def home_page():
    st.title("Welcome to SADA")

    # Load the image
    image = Image.open("SADA.png")  # Ensure the image path is correct
    draw = ImageDraw.Draw(image)

    # Define the text to be written on the image
    text = "Made with love"
    font_color = "white"  # White color for the text
    font_size = 40  # Font size for the text

    # Set the font (ensure it's available)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text width and height to center it at the bottom
    text_width, text_height = draw.textsize(text, font=font)
    img_width, img_height = image.size
    x_position = (img_width - text_width) // 2  # Center horizontally
    y_position = img_height - text_height - 10  # Position near the bottom

    # Draw the text on the image
    draw.text((x_position, y_position), text, font=font, fill=font_color)

    # Display the image with the caption
    st.image(image, caption="SADA", use_column_width=True)

    # Add "Sign In" and "Sign Up" buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Sign In", key="sign_in"):
            st.session_state.page = "Sign In"  # Set session state to track page
            st.experimental_rerun()  # Rerun to switch page

    with col2:
        if st.button("Sign Up", key="sign_up"):
            st.session_state.page = "Sign Up"  # Set session state to track page
            st.experimental_rerun()  # Rerun to switch page

# Function for Sign In Page
def sign_in_page():
    st.title("Sign In Page")
    st.write("This is where users can sign in.")
    # Add additional sign-in form elements here (e.g., email, password, etc.)

# Function for Sign Up Page
def sign_up_page():
    st.title("Sign Up Page")
    st.write("This is where users can sign up.")
    # Add additional sign-up form elements here (e.g., email, password, etc.)

# Main function to manage pages and navigation
def main():
    # Initialize session state if it's not set yet
    if 'page' not in st.session_state:
        st.session_state.page = "Home"  # Default to home page when first loading
    
    # Show the correct page based on session state
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Sign In":
        sign_in_page()
    elif st.session_state.page == "Sign Up":
        sign_up_page()

if __name__ == "__main__":
    main()


