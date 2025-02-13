import streamlit as st

def information():
    st.header("Information")
    st.subheader("What do you want to know more about?", divider="blue")
    st.write("Click on the links to get more information about the topic!")

    # create the number of columns
    c1, c2 = st.columns(2)

        # first column, display image in container, subheader as hyperlink
    # Hyperlinks: https://discuss.streamlit.io/t/hyperlink-in-streamlit-without-markdown/7046
    with c1:
        # using containers instead of use_column_width="Always" because this parameter will be removed in a future release
        general = st.container()
        general.image("general.jpg")
        st.subheader("[⬆️General info⬆️](https://www.rei.com/learn/expert-advice/cross-country-skiing-for-beginners.html#:~:text=Basic%20Cross-Country%20Ski%20Techniques%201%20The%20Balanced%20Stance,the%20shuffle-and-glide%29%3A%20...%205%20Expand%20Your%20Skills%20)")

        skating = st.container()
        skating.image("skating.jpg")
        st.subheader("[⬆️Skating technique⬆️](https://www.rei.com/learn/expert-advice/how-to-skate-ski.html)")

    # second column, display image in container, subheader as hyperlink
    with c2:
        waxing = st.container()
        waxing.image("waxing.jpg")
        st.subheader("[⬆️Grip-waxing⬆️](https://www.rei.com/learn/expert-advice/grip-waxing-crosscountry-skis.html)")

        classic = st.container()
        classic.image("classic.jpg")
        st.subheader("[⬆️Classic technique⬆️](https://www.rei.com/learn/expert-advice/how-to-cross-country-ski.html#cross-country-ski-gear)")

    # credit for photos as hyperlink connected to profile of creator
    st.write("Images by [adege](https://pixabay.com/de/users/adege-4994132/)")
