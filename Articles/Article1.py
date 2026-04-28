import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

# image = Image.open("./Images/image.png")

def article():
    date = "Monday 04/27/2026"
    author = "The Intern"

    st.subheader('''A New Era of Gaming''')
    st.markdown('''
                Welcome one and all to what might go down as the single most dumbfounding gaming event of all time. Yes, I, the illustrious intern of The Alternative F1 League have taken supreme command of all articles for this event. Strap in because I am not going to pull my punches.

                Over the course of three weeks, we will see some of the crumbiest gaming the world has ever known. Somehow, against all odds, I still expect this to be lit.

                Follow along here for recaps, points updates, and brutal meming of each individual who has unwittingly joined this roast of their unc gaming skills.
                ''')
    # st.image(image)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

# ----- How to add a GIF: ----- #
# gif = open('./Images/surfer.gif','rb')
# contents = gif.read()
# data_url = base64.b64encode(contents).decode('utf-8')
# st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)

# ----- How to add a Carousel ----- #
# carousel_images = [
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#         ]

# carousel(items=carousel_images, interval=20000)