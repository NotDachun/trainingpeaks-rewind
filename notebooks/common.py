import pandas as pd
from pyfonts import load_font

TRAINING_YEARS = [2021, 2022, 2023, 2024]
WORKOUT_TYPES = ["Bike", "Run", "Swim", "Strength"]

def read_workout_dfs():
    dfs = {}
    for year in TRAINING_YEARS:
        df = pd.read_csv(f"../data/workouts_{year}.csv")
        dfs[year] = df[df["WorkoutType"].isin(WORKOUT_TYPES)]
    return dfs

# Fonts
def load_racing_sans_one_font():
    racing_sans_one_font = load_font(
    font_url="https://github.com/google/fonts/blob/dc35a4fdb3854d5388b53df489e6fc8ab8ccaab6/ofl/racingsansone/RacingSansOne-Regular.ttf?raw=true"
    )
    return racing_sans_one_font

def load_roboto_condensed_font():
    roboto_condensed_font = load_font(
    font_url="https://github.com/google/fonts/blob/dc35a4fdb3854d5388b53df489e6fc8ab8ccaab6/ofl/robotocondensed/RobotoCondensed%5Bwght%5D.ttf?raw=true"
    )
    return roboto_condensed_font

# Colors
MY_COLORS = {
    'Dark Midnight Blue': '#002347', 
    'Slightly Lighter Midnight Blue': '#003366', 
    'Medium Midnight Blue': '#003F7D', 
    'Light Blue': '#8ecae6', 
    'Bright Orange': '#F6A600', 
    'Slightly Darker Orange': '#FD7702', 
    'Vivid Red-Orange': '#FF5003', 
    'Vivid Red': '#FF3200'
}
