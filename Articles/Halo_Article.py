import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

h00 = Image.open("./Images/Halo/h00.png")
h0 = Image.open("./Images/Halo/h0.png")
h1 = Image.open("./Images/Halo/h1.png")
h2 = Image.open("./Images/Halo/h2.png")
h3 = Image.open("./Images/Halo/h3.png")
h4 = Image.open("./Images/Halo/h4.png")
h5 = Image.open("./Images/Halo/h5.png")
h6 = Image.open("./Images/Halo/h6.png")
h7 = Image.open("./Images/Halo/h7.png")
h8 = Image.open("./Images/Halo/h8.png")
h9 = Image.open("./Images/Halo/h9.png")
h10 = Image.open("./Images/Halo/h10.png")

def article():
    date = "Thursday 05/07/2026"
    author = "The Intern"

    st.subheader('''All That Talk From Grayson and Erick''')
    st.image(h00)
    st.markdown('''
                A little tldr; up front, the big news is Team Brentuar has fallen a bit behind, but mathematically they aren't out just yet. They've just gotta DNF Team PK in Brazil next week.
                
                Video Game Highschool and day time soap operas have nothing on this FPS drama. Let's just start with PK's continuous inability to launch a game mode. Literally, every, single, time something was wrong. Someone take his degrees away.

                Once Nick figured out his keybinds, Josh had reconnected, and Erick's internet gave out, the rounds went pretty smoothly. Well, other than all the times PK and Brentuar whiffed. Accuracy lower than Ghandi's BMI. The real story wasn't how bad those two were though.

                The real story was all the talk that lead up to this matchup. Legend has it, Connor abandoned Erick, who got triggered like a snowflake, and then PK opened his mouth and got Jr. in on the nonsense, which means Erick needed Grayson as backup, and after all the drama finished, Erick brought nothing to the table, #T.A.C.O. Tavera Always Chickens Out.

                If you want a recap of how the games went, you should have watched the stream. So instead of that, enjoy the memes.
                ''')
    st.image(h0)
    st.image(h1)
    st.image(h2)
    st.image(h3)
    st.image(h4)
    st.image(h5)
    st.image(h6)
    st.image(h7)
    st.image(h8)
    st.image(h9)
    st.image(h10)
    st.markdown('''
                Ok, so I was told I have to do some kind of recap. Otherwise the fans will boo.

                Round 1 was a good ole fashioned draw during a match of Assault One Bomb. Neither team possessed enough skillz to do anything worthwhile.

                Then the gang moved on to a game of Oddball after being unable to launch a game of Land Grab. This was actually extremely competitve and truly could have gone either way. Worth a re-watch.

                Then Grayson talked a bunch of smoke and proceeded to get smoked in a round of Tactical Slayer. Bro could only kill PK and, well, that isn't really an achievement...

                Finally, the round of Capture the Flag was a bit of a blow out until Team Brentuar snagged one capture late in the round.
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