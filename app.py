import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
sender_email = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASS')

# Check if environment variables are loaded correctly
if sender_email is None or password is None:
    st.error("Environment variables for email not set. Please check your .env file or deployment settings.")
else:
    # Set up the main page configurations
    st.set_page_config(
        page_title="ReelStreamVentures",
        page_icon=":clapper:",
        layout="wide"
    )

    # Hide Streamlit's default footer
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Sidebar Navigation
    st.sidebar.title("ReelStreamVentures")
    st.sidebar.subheader("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About Us", "Services", "Contact"])

    # Home Page
    if selection == "Home":
        st.title("Welcome to ReelStreamVentures!")
        st.image("https://yourimageurl.com/banner.jpg", use_column_width=True)
        st.write("""
        At ReelStreamVentures, we specialize in creating high-quality video productions that tell compelling stories. 
        From concept to completion, our team is dedicated to bringing your vision to life.
        """)

    # About Us Page
    elif selection == "About Us":
        st.title("About ReelStreamVentures")
        st.image("https://yourimageurl.com/team.jpg", use_column_width=True)
        st.write("""
        ReelStreamVentures was founded with the mission of providing exceptional video production services. Our team consists of experienced professionals who are passionate about storytelling and dedicated to producing top-notch content.
        """)

    # Services Page
    elif selection == "Services":
        st.title("Our Services")
        st.image("https://yourimageurl.com/services.jpg", use_column_width=True)
        st.write("""
        We offer a wide range of services to meet your production needs:
        - **Pre-Production**: Concept Development, Scriptwriting, Storyboarding
        - **Production**: Filming, Directing, Cinematography
        - **Post-Production**: Editing, Visual Effects, Sound Design
        - **Additional Services**: Live Streaming, Event Coverage, Corporate Videos
        """)

    # Contact Page
    elif selection == "Contact":
        st.title("Contact Us")
        st.image("https://yourimageurl.com/contact.jpg", use_column_width=True)
        st.write("""
        We'd love to hear from you! Whether you have a project in mind or just want to learn more about what we do, feel free to get in touch.
        """)
        st.write("**Email:** reelstreamventures@proton.me")
        st.write("**Phone:** (0049) 1742584800")
        st.write("**Address:** Aachen, Germany")

        # Contact Form
        st.subheader("Send us a message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send")

            if submitted:
                # Send the email
                receiver_email = "contact@reelstreamventures.com"

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = f"New contact form submission from {name}"

                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                msg.attach(MIMEText(body, 'plain'))

                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, password)
                    text = msg.as_string()
                    server.sendmail(sender_email, receiver_email, text)
                    server.quit()

                    st.success("Thank you for reaching out! We'll get back to you soon.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # Run the app
    if __name__ == '__main__':
        st.write("ReelStreamVentures Streamlit App")
