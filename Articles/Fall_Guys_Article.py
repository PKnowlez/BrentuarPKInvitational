import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

fg1 = Image.open("./Images/Fall Guys/fg1.png")
fg2 = Image.open("./Images/Fall Guys/fg2.png")
fg3 = Image.open("./Images/Fall Guys/fg3.png")
fg4 = Image.open("./Images/Fall Guys/fg4.png")
fg5 = Image.open("./Images/Fall Guys/fg5.png")
fg6 = Image.open("./Images/Fall Guys/fg6.png")
fg7 = Image.open("./Images/Fall Guys/fg7.png")
fg8 = Image.open("./Images/Fall Guys/fg8.png")
fg9 = Image.open("./Images/Fall Guys/fg9.png")
fg10 = Image.open("./Images/Fall Guys/fg10.png")
fg11 = Image.open("./Images/Fall Guys/fg11.png")
fg12 = Image.open("./Images/Fall Guys/fg12.png")

def article():
    date = "Thursday 04/30/2026"
    author = "The Intern"

    st.subheader('''More Like Fail Guys''')
    st.markdown('''
                What a showing, or should I say disaster for the team captains. Good thing they drafted players who were better than them otherwise this would have been a complete and total disaster.

                Both Brentuar and PK could hardly get off the start line in each event. However, both teams had some rising stars. Without Pretz and Eddie, I would have just turned Twitch off. Dude, how are you all making me praise Eddie. This is absolutely insane. That guy can't even drive around a circuit once without totalling his car, but somehow he ascends to MLG ranks when playing Fall Guys???? Are you serios???

                But that's enough glazing for him, especially since Oscar the Grouch has never even ripped off that much trash talking, straight up disrespectful.

                Now Pretz on the other hand. What a GOAT. The only member of Team Brentuar that held on each and every round. Had Eddie sneezed or lost a little bit of focus, Pretz would be leading the tournament in points. unfortunately for the team in red, that isn't what happened.

                Alright, that's enough of a recap. It's time for some memes. And no, I do not apologize for any of these. Deal with it nerds.
                ''')
    st.image(fg1)
    st.image(fg2)
    st.image(fg3)
    st.image(fg4)
    st.image(fg5)
    st.image(fg6)
    st.image(fg7)
    st.image(fg8)
    st.image(fg9)
    st.image(fg10)
    st.image(fg11)
    st.image(fg12)
    st.markdown('''
                Next week we will see which Tavera brother is the better overall gamer, if the Grayson v. Connor beef is all its cracked up to be, if Nick or Josh's past gaming glory is greater, and if Brentuar or PK can clean the sheets and not soil their beds again if you know what I mean.
                ''')
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