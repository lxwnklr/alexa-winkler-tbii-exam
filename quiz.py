import streamlit as st

def quiz():
    st.title("Cross-Country Skiing Quiz")

    # initialize a tracker to determine the state of the quiz
    if 'quiz_tracker' not in st.session_state:
        st.session_state.quiz_tracker = 0

    # function to start the quiz, changes the tracker to 1
    def start_quiz():
        st.session_state.quiz_tracker = 1

    # function to reset the quiz, changes the tracker back to 0
    def reset_quiz():
        st.session_state.quiz_tracker = 0

    # create placeholder for the starting button
    placeholder = st.empty()
    # display a button to start the quiz; on clicking, call `start_quiz` function
    placeholder.button("Click to start", on_click=start_quiz)

    # if the quiz has started (tracker = 1), display the quiz questions
    if st.session_state.quiz_tracker == 1:
        # clear placeholder - this removes the "Click to start" button
        placeholder.empty()
        # use html to make text bold
        st.write("<b>Answer all the questions down below. Click on 'Show result' to get your score.</b>", unsafe_allow_html=True)

        # questions and answer options
        q1 = st.radio("What is essential to maintain during the glide phase in both classic and skate skiing?",
                      ["Upright posture", "Balanced stance", "Fast pace"])
        q2 = st.radio("What type of wax is used for grip in classic cross-country skiing?",
                      ["Glide wax", "Kick wax", "Base wax"])
        q3 = st.radio("Which part of the ski is designed to grip the snow in classic skiing?",
                      ["Tip", "Tail", "Kick zone"])
        q4 = st.radio("What is the purpose of glide wax?",
                      ["To improve grip", "To protect the ski base", "To reduce friction and increase speed"])
        q5 = st.radio("What should you do to maintain your skis after each outing?",
                      ["Store them wet", "Clean and dry them", "Leave them outside"])
        q6 = st.radio("In which technique do you use a V-shaped motion?",
                      ["Classic", "Skating", "Both"])
        q7 = st.radio("Which technique involves pushing off with one ski while gliding on the other in classic skiing?",
                      ["Herringbone", "Double poling", "Diagonal stride"])
        q8 = st.radio("Which muscle group is primarily used in double poling?",
                      ["Leg muscles", "Arm and core muscles", "Back muscles"])
        q9 = st.radio("What type of ski binding system is commonly used in cross-country skiing?",
                      ["Alpine", "NNN or SNS", "Telemark"])
        q10 = st.radio("What is the V1 skate skiing technique best used for?",
                       ["Flat terrain", "Uphill sections", "Downhill sections"])

        # track the number of correct answers
        correct = 0

        # check answers for correctness and increase score if answer is right
        if q1 == "Balanced stance":
            correct += 1
        if q2 == "Kick wax":
            correct += 1
        if q3 == "Kick zone":
            correct += 1
        if q4 == "To reduce friction and increase speed":
            correct += 1
        if q5 == "Clean and dry them":
            correct += 1
        if q6 == "Skating":
            correct += 1
        if q7 == "Diagonal stride":
            correct += 1
        if q8 == "Arm and core muscles":
            correct += 1
        if q9 == "NNN or SNS":
            correct += 1
        if q10 == "Uphill sections":
            correct += 1

        # button to show the quiz result
        if st.button("Show result"):
            # provide feedback based on the number of correct answers
            if correct < 4:
                st.subheader(F"You have {correct} correct answers.")
                st.subheader(":blue[You are a beginner🐧]")
            elif correct < 8:
                st.subheader(F"You have {correct} correct answers.")
                st.subheader(":blue[You know the basics❄️]")
            else:
                st.subheader(F"You have {correct} correct answers.")
                st.subheader(":rainbow[You are an expert⛷️]")

        # button to reset the quiz and go back to the start
        st.button("Go back to the start", on_click=reset_quiz)
