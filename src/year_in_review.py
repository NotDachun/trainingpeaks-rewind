import sys
import pandas as pd

def year_in_review(fp):
    df = pd.read_csv(fp)

    workout_types = [
        "Bike",
        "Run",
        "Swim",
        "Strength"
    ]
    df_filt = df[df["WorkoutType"].isin(workout_types)].copy()
    df_filt["DistanceInMiles"] = df_filt["DistanceInMeters"] / 1000 * .61
    df_year = df_filt.groupby("WorkoutType").agg({"DistanceInMiles": "sum", "TimeTotalInHours": "sum"})

    print("Total Time and Distance")
    print(df_year.sort_values("TimeTotalInHours", ascending=False))


    df_filt["month"] = df_filt["WorkoutDay"].apply(lambda date: date.split("-")[1])
    df_month = df_filt.groupby("month", as_index=False).agg({"DistanceInMiles": "sum", "TimeTotalInHours": "sum"})

    print("-" * 60)
    print("Time and Distance by Month")
    print(df_month.sort_values("month"))

    print("-" * 60)
    df_swim = df_filt[df_filt["WorkoutType"] == "Swim"].sort_values("DistanceInMeters", ascending=False)
    print("Biggest Swim")
    print(df_swim[["WorkoutDay", "DistanceInMeters", "TimeTotalInHours"]].iloc[0])
    df_bike = df_filt[df_filt["WorkoutType"] == "Bike"].sort_values("DistanceInMiles", ascending=False)
    print("Biggest Bike")
    print(df_bike[["WorkoutDay", "DistanceInMiles", "TimeTotalInHours"]].iloc[0])
    df_run = df_filt[df_filt["WorkoutType"] == "Run"].sort_values("DistanceInMiles", ascending=False)
    print("Biggest Run")
    print(df_run[["WorkoutDay", "DistanceInMiles", "TimeTotalInHours"]].iloc[0])



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python year_in_review.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    year_in_review(file_path)