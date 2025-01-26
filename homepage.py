import streamlit as st

#set up the page, before importing my code from other files because otherwise it can result in errors
st.set_page_config(page_title="Nordic skiing", page_icon="❄️")

# import functions from other files
from about import about_me
from motivation import motivation_quotes
from weather import weather_waxing
from training_with_login_register import training
from quiz import quiz
from information import information

# function to create the homepage and mange navigation
def homepage():
    # define menu options
    options = ["Homepage", "Weather and waxing", "Training sessions", "Quiz", "Motivational quotes", "Information", "About me"]

    # sidebar for menu navigation
    page_selection = st.sidebar.selectbox("Menu", options)

    # add additional text to the sidebar for user guidance
    with st.sidebar:
        st.write(f"<b> Use the menu to navigate through the app. <b> ", unsafe_allow_html=True)

    # display content based on the selected menu option
    if page_selection == "Homepage":
        # create a grid of icons using columns
        c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
        with c1:
            # display a dark icon
            st.image("icon_dark.png")
        with c2:
            # display a light icon
            st.image("icon_light.png")
        with c3:
            st.image("icon_dark.png")
        with c4:
            st.image("icon_light.png")
        with c5:
            st.image("icon_dark.png")
        with c6:
            st.image("icon_light.png")
        with c7:
            st.image("icon_dark.png")

        # credit for the icons - link to profile of creator
        st.write("Icons by [OpenIcons](https://pixabay.com/de/users/openicons-28911/)" )
        st.title("Homepage")

        # introduction text
        st.write("Cross-country skiing, also called Nordic skiing, is a winter sport on skis (who would have thought😉). It is health-promoting and easy to start as a beginner. Just rent yourself some skis, poles and boots and you are ready to go!  \n",
                "But it can be hard to learn a new skill alone. That's why this interactive app for learning cross country-skiing might be perfect for you! You can learn a lot about cross-country skiing with the provided links in the 'Learn more'-section and test your knowledge with the quiz. Do you want to start with skiing? Great! Then you can track your progress! Or do you want to wax your own ski for an even better pace? Just click on 'What to wax' to see what the temperature will be and what you should wax according to it. And if you have a bad day and want to skip training just press the 'Click here to get some motivation!'-button and see what happens!")
        st.subheader("Explore the app and most importantly: You don't need to be good to have fun. So just go out and ENJOY LIFE!")

    # for the next code lines same principle: if "example" is selected, call the function example()
    # e.g. if "Motivational quotes" is selected, call the function motivation_quotes()
    elif page_selection == "Motivational quotes":
        motivation_quotes()
    elif page_selection == "Quiz":
        quiz()
    elif page_selection == "Training sessions":
        training()
    elif page_selection == "Information":
        information()
    elif page_selection == "Weather and waxing":
        weather_waxing()
    elif page_selection == "About me":
        about_me()

# call the homepage function to initialize the app
homepage()