# TrainingPeaks Rewind

Your training data, visualized.

## How to Use

1. Download your TrainingPeaks data following the instructions [here](https://help.trainingpeaks.com/hc/en-us/articles/204985370-Data-Export)
   - Make sure to download the "Workout Summary". For each year (Jan 1st - Dec 31st), you should get a CSV file. Save them into the `data` directory as `workouts_{year}.csv`, for example `data/workouts_2024.csv`.
   - Create a `events.csv` file in the `data` directory. This file should contain a list of events that you have completed. The format should be:
     ```
     eventDate,name,eventType,eventDistance,result,resultSwim,resultBike,resultRun,resultLink
     2020-01-04,Perrigo Parkrun,RunningRoad,5K,0:21:23,,,,https://www.parkrun.us/perrigo/results/32/
     ...
     ```
2. Install the dependencies
   ```
   pip install -r requirements.txt
   ```
3. Run the [notebooks](notebooks) to create each info-graphic with your own data. Since there are elements of the code that are specific to my data, you may need to adjust the text content and placements.

## Contributing

If you have any suggestions for improvements, feel free to add your own notebook to the [notebooks](notebooks) directory.

## License

This project is open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details.
