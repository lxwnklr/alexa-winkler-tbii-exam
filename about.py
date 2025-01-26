import streamlit as st

def about_me():
    st.title("About me")
    # create the number of columns
    c1, c2 = st.columns(2)

    with c1:
        # display image
        st.image("about_me.jpg",caption="📌 Hohenzollern Skistadion")

    with c2:
        # text about myself
        st.header("Hi, I'm Alexa👋🏼")
        st.write("While I was in school I used to do biathlon and since cross-country skiing is part of this amazing sport I wanted to create an application for you to learn more about it, track your own progress and this in a fun way!")
        st.subheader("LOTS OF FUN!!!")
