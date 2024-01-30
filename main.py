
import streamlit as st
from trymap import generate_google_maps_embed

st.set_page_config(layout="wide")

def copy_to_clipboard(text):
    js = f"""
    navigator.clipboard.writeText('{text}').then(() => {{
      st.experimental_rerun();  // Refresh the app to display success message
    }}, () => {{
      console.error('Failed to copy text: ', error);
    }});
    """
    st.write(js, unsafe_allow_html=True)
def generate_itinerary(start_place, end_place, must_see, max_km, budget,
                       num_days, start_date, selected_pois, selected_accommodation):
    # Validate
    if not start_place or not end_place:
        # or not terms_checkbox.isChecked():
        st.echo("Error", "Invalid input")
        return

    my_pois_list = selected_pois
    st.echo(my_pois_list)
    num_of_columns = "7"

    user_message = "Generate a table with the following: Plan an itinerary for my upcoming trip:\n"
    round_trip = start_place == end_place
    if round_trip:
        user_message += f', I want to have a round trip  by car. start at  {start_place}  and end at {start_place}\n'
    else:
        user_message += f'from {start_place} to {end_place} by car. '
        user_message += f'I do not want to come back to {start_place} at the end of the trip.\n '

    if len(must_see) > 2:
        user_message += f'At some point during the trip, I must see {must_see} . Not necessarily in the same order. '
        user_message += "You may add additional POIs that you think I might like.\n "
    user_message += "Please OMIT any introductory lines or prefix.\n "
    user_message += "I want to get an itinerary that follow the next rules: \n"
    user_message += "- You can choose the itinerary that you think is the best for me. \n"
    user_message += "- I don't want to arrive to the same place twice, unless it is at the last day of a round trip. \n"
    user_message += f'- The trip will start on {str(start_date)}  . \n'
    user_message += f'- The trip is going to last {str(num_days)} days \n'
    user_message += (f'- It is imperative that I do not drive more than  {str(max_km)} kilometers on any given day'
                     f'-This is a MUST! \n')
    user_message += (f'- Please distribute driving distances and activities evenly across the days of the trip, '
                     f'avoiding excessive driving on any single day.\n ')
    if my_pois_list:
        user_message += f'- My favorites POIs are:  {str(my_pois_list)} .\n '

    user_message += f'- I do not want to visit in {start_place} . \n'
    user_message += ("- I want to visit 3 or 4 sites every day, total time around 5 to 7 hours per day "
                     "(Depending on the average spending time in each site). \n")
    user_message += "- if there are some POIs on the way, I would like to visit them as well.\n "
    user_message += (f'- My favorite type of accommodation {selected_accommodation}  '
                     f'Accommodations with a budget not exceeding {str(budget)} dollars per night,\n ')

    user_message += "- Please check the availability of the accommodation before you add them to the itinerary.\n "
    user_message += ("- Provide distinct itinerary for each day of the journey. "
                     "The lines of the table are for the days, \n")
    user_message += "(please separate between the days with a" + r'''\n).'''
    user_message += f' The columns ({str(num_of_columns)}) are: '
    user_message += "- Day date (call the column 'Day'). \n"
    user_message += ("- Driving from and driving to (in the same row, "
                     "separate them with ' to ' include just the cities names, WITHOUT the country name) "
                     "(call the column 'Way'), ")
    # user_message += ("if we stay in same place DON'T add anything, just write the name of the place, "
    #                 "refrain from including any character or word before or after.\n ")
    user_message += "- Actual Driving distance (call the column 'Km').\n "
    user_message += "- What to do in the morning (with average time in each site) (call the column 'Morning') "
    user_message += "if the average time is not integer, round it to the nearest integer. "
    user_message += ("if there are more than one thing to do in the morning, separate them with a '|'. "
                     "Refrain from including any additional commas to the sites names. \n")
    user_message += "- What to do in the afternoon (with average time in each site) (call the column 'Afternoon') "
    user_message += "if the average time is not integer, round it up to the nearest integer. "
    user_message += ("if there are more than one thing to do in the afternoon, separate them with a '|'. "
                     "Refrain from including any additional commas to the sites names. \n")
    if my_pois_list:
        user_message += ("- If there is nothing to do in the morning or in the afternoon, "
                         "(that match my favorite POIs), please find other POIs\n")

    user_message += "- Hotel name (call the column 'Hotel'). \n"
    user_message += "- Budget (call the column 'Budget'). \n "
    user_message += "- SEPARATE between columns with a ',' \n"

    user_message += ("- I also need that the first line of the table will be: Day, Way, Km,"
                     " Morning, Afternoon, Hotel, Budget \n")

    user_message += "- At the end of the table, please provide a clickable Google Maps link for the itinerary."
    user_message += ("- Please format the link as an HTML anchor tag with the URL beginning with"
                     " 'https://www.google.com/maps/dir/'.")
    user_message += ("- Include the city names and their corresponding countries separated by '+' "
                     "for each destination within the link. \n")
    user_message += ("- Please REFRAIN from any unnecessary characters before or after the link. "
                     "So the link will be, for instance:")
    hyper_example = f'=HYPERLINK("https://www.google.com/maps/dir/Paris+France/Fontainebleau+France)"'
    user_message += hyper_example
    user_message += (" \n- Generate a CSV file with the above table, "
                     "including the link to the Google maps")
    prompt = user_message
    st.write(prompt)
    st.write("-------------ZZZZZZ------------------")
    return prompt


left_col, mid_col, right_col = st.columns([6, 1, 2])

# with main_col:
with left_col:

    st.title("Trip Planner")

    # Input fields
    # Set the width of the input fields
    input_width = 400  # Adjust the width as needed

    # Apply custom CSS to set the width of the input fields

    st.markdown(
        f"""
        <style>
            .stTextInput, .stNumberInput, .stDateInput, .stMultiselect {{ width: {input_width}px; }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Create text input fields
    start_place = st.text_input("Start Place", key="start_place")
    end_place = st.text_input("End Place", key="end_place")

    must_see = st.text_input("Must See")

    # Use beta_expander to create a container for the number input
    # Create a sidebar for additional settings
    st.sidebar.header("Settings")
    max_km = st.sidebar.number_input("Max Km/Day", min_value=150, max_value=300, step=10)
    budget = st.sidebar.number_input("Budget Per Night", min_value=150, max_value=1000, step=10)
    num_days = st.sidebar.number_input("Number of Days", min_value=1, max_value=15, step=1)
    start_date = st.sidebar.date_input("Start Date")

    poi_options = ["Museums", "Parks & Gardens", "Architecture", "Art Galleries", "Local festivals",
                   "Zoos & Aquariums", "Wineries", "Science Centers", "Local Markets"]

    selected_pois = st.sidebar.multiselect("Preferred POIs", poi_options)

    accommodation_options = ["3-star hotel", "4-star hotel", "5-star hotel", "Hostels ", "B&Bs",
                             "Campgrounds", "Resorts"]

    selected_accommodation = st.sidebar.multiselect("Preferred Accommodation", accommodation_options)

    terms_checkbox = st.checkbox("I agree to the terms and conditions")

    if st.button("Enter Data"):
        with st.spinner("Please wait..."):
            # generate a map from start_place to end_place
            # Empty placeholder in mid-column
            with mid_col:
                map_placeholder = st.empty()

            google_maps_embed = generate_google_maps_embed(start_place, end_place)
            with right_col:
                map_placeholder.markdown(google_maps_embed, unsafe_allow_html=True)
            prompt = generate_itinerary(start_place, end_place, must_see, max_km, budget,
                               num_days, start_date, selected_pois, selected_accommodation)

            # write the prompt to the Clipboard
        import os

        # def write_to_clipboard(text):
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QGuiApplication

    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Set the text to be copied to the clipboard

    clipboard = QGuiApplication.clipboard()
    clipboard.setText(prompt)

    # Copy the text to the clipboard
    clipboard.copy()

    # Exit the application
    QApplication.quit()


