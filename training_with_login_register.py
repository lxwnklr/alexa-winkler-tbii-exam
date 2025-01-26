import streamlit as st
import pandas as pd
from datetime import datetime
from pymongo.mongo_client import MongoClient


# main function that handles the training app logic
def training():
    # set up counter if login/register happened, only see login page once
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # set up a credential check
    if 'credentials_check' not in st.session_state:
        st.session_state.credentials_check = False

    # save current user_name in session state
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None

    # function to connect to MongoDB
    def connect_to_mongo():
        # load the user and db password from the secrets.toml file
        user = st.secrets['db_username']
        password = st.secrets['db_password']

        # database connection string
        uri = f"mongodb+srv://{user}:{password}@tb-ii.nri38.mongodb.net/?retryWrites=true&w=majority&appName=tb-ii"

        # connect to MongoDB cluster
        client = MongoClient(uri)

        try:
            # print a message to say the
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            return client
        except Exception as e:
            # if connection was not made, then you will see an error message in your terminal
            print(e)

    # function to connect to  specific MongoDB collection
    def connect_to_collection(db_name, collection_name):
        # connect to cluster
        client = connect_to_mongo()
        # connect to database and collection
        db_name = "streamlit"
        collection_name = "cross_country_skiing_user_database"

        # connect to the collection
        db = client[db_name]
        collection = db[collection_name]

        return collection

    # function to add new training session
    def new_training():
        st.subheader(f"Hi {st.session_state.user_name}! Save your training sessions here")
        # input field for training session date
        date = st.date_input("Date:")

        # Custom time input (HH:MM format)
        duration = st.text_input("Enter duration (HH:MM)", "12:00")
        # https://www.geeksforgeeks.org/python-datetime-strptime-function/
        try:
            # Try parsing the input as a time
            time_obj = datetime.strptime(duration, "%H:%M")
            st.write(f"Duration time: {time_obj.strftime('%H:%M')}")
        except ValueError:
            st.error("Invalid time format. Please use HH:MM.")

        # input for distance
        distance = st.number_input("Distance: (in km)")

        # slider for user's feeling about training session
        feeling = st.select_slider(
            "How did you feel?",
            ["Very Bad", "Bad", "Neutral", "Good", "Very Good"],  # Text for ratings
            value="Neutral")  # Default value

        # Display the selected rating
        st.write(f"You felt: {feeling}")

        # input for additional comments
        comments = st.text_input("Enter additional comments here:")

        # button to submit training
        if st.button("Submit training"):
            # Get the current username from session_state
            username = st.session_state.user_name

            # Convert date to datetime for MongoDB
            training_date = datetime.combine(date, datetime.min.time())

            # connect to the database collection
            db_name = "streamlit"
            collection_name = "cross_country_skiing_user_database"
            collection = connect_to_collection(db_name, collection_name)

            # create training session document
            document = {"username": username,
                        "training_date": training_date,
                        "training_duration": duration,
                        "training_feeling": feeling,
                        "training_comments": comments,
                        "training_distance": distance,
                        "training_created_at": datetime.now()}

            # insert the document into the database
            collection.insert_one(document)

            # add success message for user
            #https: // docs.streamlit.io / develop / api - reference / status / st.success
            st.success("Training session saved successfully!", icon="✅")


    # function to display previous training sessions
    def previous_trainings():
        st.subheader(f"Hi {st.session_state.user_name}! You can see your previous training sessions here")

        # connect to MongoDB and retrieve data (training sessions) for current user
        collection = connect_to_collection("streamlit", "cross_country_skiing_user_database")
        username = st.session_state.user_name
        user_trainings = list(collection.find({"username": username}))

        # check if there are already training sessions safed
        if not user_trainings:
            # if not
            st.write("You didn't save (more) training sessions yet.")
        else:
            # sort data (newest date first), code line done with ChatGPT
            user_trainings = sorted(user_trainings, key=lambda x: x.get('training_date', datetime.min),reverse=True)

            for training in user_trainings:
                # Safely retrieve training_date
                training_date = training.get("training_date")
                if training_date:
                    # get training data
                    # Ensure training_date is a datetime object for formatting
                    # https://www.w3schools.com/python/ref_func_isinstance.asp
                    if isinstance(training_date, datetime):
                        training_date_display = training_date.strftime('%Y-%m-%d')
                        training_duration = training.get("training_duration")
                        training_distance = training.get("training_distance")
                        training_feeling = training.get("training_feeling")
                        training_comments = training.get("training_comments")

                        # display training sessions in expander
                        # https://docs.streamlit.io/develop/api-reference/layout/st.expander
                        with st.expander(f"Training on {training_date_display}"):
                            st.write(f"**Duration:** {training_duration}")
                            st.write(f"**Distance:** {training_distance} km")
                            st.write(f"**Feeling:** {training_feeling}")
                            st.write(f"**Comments:** {training_comments}")

                else:
                     st.write("You didn't save (more) training sessions yet.")


    # function to set up the "Progress" page which includes save_training_progress_page and previous_training_progress_page
    def training_sessions():
        st.header("Training sessions")
        st.write("Use this section to save your training session to keep a better track about your progress.  \n"
                 "Just some examples what you could add: date, duration, distance, pace and how you felt. Also use this opportunity to reflect about your technical abilities. Reflection is key when it comes to learning something new!")

        # create tabs for new and previous sessions
        tabs1, tabs2 = st.tabs(['New Training', 'Previous training '])

        # tab to add a new training session
        with tabs1:
            st.title("Add a new training sessions")
            new_training()

        # tab to display a previous training session
        with tabs2:
            st.title("Previous training sessions")
            previous_trainings()


    # create a placeholder variable, so I can delete the form widget after using it
    placeholder = st.empty()

    # function for the registration page
    def registration_page():
        # creating a form to collect information
        with placeholder.form("registration_form"):
            st.subheader("Register user")

            # input for user
            user_name = st.text_input("Enter username")
            password = st.text_input("Password", type="password")
            repeat_password = st.text_input("Repeat password", type="password")
            name = st.text_input("Enter your name")
            age = st.number_input("Enter your age", step=1, min_value=0)

            # submit registration data
            submit_button = st.form_submit_button("Register")

        # if submit button clicked
        if submit_button:
            # connect to collection
            db_name = "streamlit"
            collection_name = "cross_country_skiing_user_database"
            collection = connect_to_collection(db_name, collection_name)

            # reading data about the users
            user_data = pd.DataFrame(list(collection.find()))
            user_names = list(user_data.username)

            # add some validation
            if len(password) < 1 and len(user_name) < 1:
                st.error("Enter a username and a password", icon="🔥")
            elif password != repeat_password:
                st.error("Passwords do not match", icon="🔥")
            elif user_name in user_names:
                st.error("Username already exists", icon="🔥")
            # if everything is fine, save user (input) information into document
            else:
                document = {"username": user_name, "password": password, "name": name, "age": age,
                            "created_at": datetime.now()}

                # save data from document to collection
                collection.insert_one(document)

                # store username
                st.session_state.user_name = user_name

                placeholder.empty()
                training_sessions()


    def login_page():
        with placeholder.form("Login"):
            st.header("Training sessions")
            # use HTML to change text style
            st.write(f"<p style='font-size: 22px'><strong>Use this section to save your training session to keep a better track about your progress.</strong></p>", unsafe_allow_html=True)
            st.write(f"<p style='font-size: 18px'>Please enter your log in information to get access to your personal data."
                        f"<br>Click on the Register Button if you aren't registered yet.</p>",
                        unsafe_allow_html=True)

            # input for username and password if already registered
            user_name = st.text_input("Username", placeholder="Please enter your user name")
            password = st.text_input("Password", placeholder="Please enter your password", type="password")

            # login and register button
            login_button = st.form_submit_button("Login")
            register_button = st.form_submit_button("Go to registration")

        # if login button clicked
        if login_button:
            # connect to collection
            db_name = 'streamlit'
            collection_name = 'user_registration_data'
            collection = connect_to_collection(db_name, collection_name)

            # read the data from the collection and identify usernames
            user_data = pd.DataFrame(list(collection.find()))
            user_names = list(user_data.username)

            # check if the username is already in database
            # if yes...
            if user_name in user_names:
                # this selects the password of the user that is entering information
                registered_password = list(user_data[user_data.username == user_name].password)[0]

                # does the password from database match with the password input from user
                # if yes..
                if password == registered_password:
                    st.session_state.credentials_check = True
                    # store username
                    st.session_state.user_name = user_name
                # if not...
                else:
                    st.error("The username/password is not correct")
            # if username not in database
            else:
                st.error("Please provide correct user name or click on register as new user")

        # if register button clicked
        if register_button:
            # switch to registration page
            st.session_state.count = 1
            placeholder.empty()

    # main logic that determines which page is shown
    if st.session_state.count == 0:
        login_page()
    if st.session_state.count == 1:
        registration_page()
    if st.session_state.credentials_check:
        placeholder.empty()  # clear everything
        training_sessions()

