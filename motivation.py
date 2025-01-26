import streamlit as st
import random

def motivation_quotes():
        st.title(":rainbow[Motivational quotes]")

        # list of motivational quotes
        motivational_quotes = ["The harder the battle, the sweeter the victory.",
                "You miss 100% of the shots you don't take.", "The pain you feel today will be the strength you feel tomorrow.",
                "Winning isn't everything, but wanting to win is.",
                "The difference between the impossible and the possible lies in a person's determination.",
                "It’s not whether you get knocked down; it's whether you get up.",
                "Champions keep playing until they get it right.", "Hard work beats talent when talent doesn't work hard.",
                "Don't watch the clock; do what it does. Keep going.", "Success is where preparation and opportunity meet.",
                "You are never a loser until you quit trying.",
                "The only way to achieve the impossible is to believe it is possible.",
                "Believe in yourself and all that you are.",
                "The only limit to our realization of tomorrow will be our doubts of today.",
                "Determination today leads to success tomorrow.",
                "Great things come from hard work and perseverance. No excuses.",
                "Success is not the absence of failure; it's the persistence through failure.",
                "Push yourself because no one else is going to do it for you.", "Your only limit is you.",
                "The difference between ordinary and extraordinary is that little extra.",
                "Success usually comes to those who are too busy to be looking for it.", "Dream big and dare to fail.",
                "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                "Do something today that your future self will thank you for.",
                "Push yourself"]


        # Initialize session state for random quote
        if "random_quote" not in st.session_state:
            st.session_state.random_quote = "Click the button to get motivated!"

        # Button to generate a new quote
        if st.button("Click here to get some motivation", use_container_width= True):
            # assign a new random quote to session state
            st.session_state.random_quote = random.choice(motivational_quotes)



        # Display the quote with larger text using HTML
        st.markdown(f"<h2 style='text-align: center;'>{st.session_state.random_quote}</h2>", unsafe_allow_html=True)

        # create columns and make second column bigger
        c1, c2, c3 = st.columns([1,2,1])

        # use second column so picture is centered
        with c2:
                # display image for the page to be visually more appealing
                st.image("motivation.png",use_column_width="always")
                # credit for creator (hyperlink to profile)
                st.write("By [mediamodifier](https://pixabay.com/de/users/mediamodifier-1567646/)")

