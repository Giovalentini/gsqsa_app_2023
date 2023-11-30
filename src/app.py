import pandas as pd
import streamlit as st

# Function to load data
def load_data():
    path = 'db/games.csv'
    return pd.read_csv(path, sep=";", low_memory=False)

# Custom function for styling
def style_games(df):
    # Define the styling function
    def apply_row_styling(row):
        if row['at_home'] == 1:
            return ['background-color: rgba(255, 165, 0, 0.1)']*len(row)  # Orange with low opacity for the entire row
        else:
            return ['background-color: rgba(255, 255, 255, 0.1)']*len(row)  # White with low opacity for the entire row

    return df.style.apply(apply_row_styling, axis=1)

# Load the data
games = load_data()
styled_games = style_games(games.drop(columns="id"))

# Title of the app
st.title("GSQSA Basket Team Stats 2023/2024")

# Show the dataframe without the index
st.markdown(styled_games.to_html(), unsafe_allow_html=True)

# KPI calculation
st.subheader("Averages")

# User selection for filtering
filter_option_home = st.selectbox(
    "Select the games based on home/away:",
    ("All Games", "At Home", "Away")
)
filter_option_win = st.selectbox(
    "Select the games based on win/loss:",
    ("All Games", "Wins", "Losses")
)


# Create an ordered list of unique team names
unique_teams = games['team'].drop_duplicates().tolist()

# Slider for selecting team name range
selected_teams = st.select_slider(
    "Select the range of team names:",
    options=unique_teams,
    value=(unique_teams[0], unique_teams[-1])
)

# Determine the range of game IDs for the selected teams
selected_games = games[games['team'].isin(selected_teams)]
min_id = selected_games['id'].min()
max_id = selected_games['id'].max()

# Apply filters to the DataFrame
filtered_games = games[(games['id'] >= min_id) & (games['id'] <= max_id)]


#filtered_games = games

if filter_option_home != "All Games":
    home_value = 1 if filter_option_home == "At Home" else 0
    filtered_games = filtered_games[filtered_games["at_home"] == home_value]

if filter_option_win != "All Games":
    win_value = 1 if filter_option_win == "Wins" else 0
    filtered_games = filtered_games[filtered_games["win"] == win_value]

# Calculate the averages
avg_points_gsqsa = filtered_games["points_gsqsa"].mean()
avg_points_opponent = filtered_games["points_opponent"].mean()

# Create columns for each KPI
col1, col2 = st.columns(2)

# Custom HTML and CSS for KPIs
kpi1_html = f"<div style='text-align: center; color: green;'><span style='font-size: 1.2em;'>Average Points GSQSA</span><br><span style='font-size: 2.5em;'>{avg_points_gsqsa:.2f}</span></div>"
kpi2_html = f"<div style='text-align: center; color: red;'><span style='font-size: 1.2em;'>Average Points Opponent</span><br><span style='font-size: 2.5em;'>{avg_points_opponent:.2f}</span></div>"

# Display the KPIs in their respective columns
col1.markdown(kpi1_html, unsafe_allow_html=True)
col2.markdown(kpi2_html, unsafe_allow_html=True)