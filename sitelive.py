import streamlit as st
from PIL import Image
import time

# Load the uploaded image
logo_path = "site_logo.JPG"
main = "Main.JPG"
logo = Image.open(logo_path)

# Page Configuration
st.set_page_config(
    page_title="MyUdyog",
    page_icon=logo,
    layout="centered",
)

# App Title and Banner
st.markdown("""
        <style>
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .banner {
            font-size: 2.8em;
            font-weight: bold;
            text-align: center;
            color: #FF6F61;
            margin-bottom: 10px;
        }
        .tagline {
            font-size: 1.5em;
            text-align: center;
            color: #555;
            margin-top: -15px;
        }
        .subtext {
            font-size: 1.2em;
            text-align: center;
            color: #777;
            margin-bottom: 25px;
        }
        .congrats-box {
            background-color: #F9F9F9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .button-center {
            margin-top: 20px;
        }
    </style>
    <div class="banner"> !!! Congratulations !!!<br> DHAMAYANTI AGRI TECH PRIVATE LIMITED!</div>
    <div class="tagline">Empowering Growth, Cultivating Success</div>
    <div class="subtext">We're thrilled to release the new website, "MyUdyog."</div>
""", unsafe_allow_html=True)

# Display the logo
st.image(main, use_container_width = True)

# Company Info Section
st.markdown("""
<div class="congrats-box">
    <h3 style="text-align: center;">DHAMAYANTI AGRI TECH PRIVATE LIMITED</h3>
    <p style="text-align: center; font-size: 1.1em;">
        Directors: <b>Damayanti Katariya</b> and <b>Nischay Jethalal Katariya</b>
    </p>
</div>
""", unsafe_allow_html=True)

# High-Level Content
st.write("""
### A New Chapter of Innovation and Excellence
This is a defining moment for **Dhamayanti Agri Tech** as we launch the website that symbolizes growth, innovation, and success. Congratulations to the team for their hard work and dedication.

It's time to take **MyUdyog** live and let the world see the fruits of your efforts.
""")

# Release Button
st.markdown('<div class="button-center">', unsafe_allow_html=True)
if st.button("🚀 Go Live with MyUdyog"):
    st.balloons()
    st.markdown("[Click here to open MyUdyog](https://myudyogindia.com/)", unsafe_allow_html=True)
    with st.spinner("MyUdyog is lunching....."):
        time.sleep(10)
    st.success("Site deployment complete")
    st.success("Website successfully launched! 🌟")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="border: 1px solid #ddd; margin-top: 30px;">
<p style="text-align: center; font-size: 0.9em; color: #888;">
    Built with ❤️ to celebrate this incredible milestone. Here's to many more successes!
</p>
""", unsafe_allow_html=True)
