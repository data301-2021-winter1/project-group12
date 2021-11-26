import pandas as pd
import numpy as np

def load_and_process(csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(csv_file)
        .rename(columns={"Car": "Team", "Pos": "Position"})
        .fillna("Independant")
        .replace(["Kimi RÃ¤ikkÃ¶nen RAI"],"Kimi Räikkönen RAI")
        
        )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .assign(Driver_ID = df1["Driver"].str[-3:],Driver2 = df1["Driver"].str[:-3])
        .drop(columns=["Driver"])
        .rename(columns={"Driver2": "Driver"})
        [["Driver", "Driver_ID", "Team", "Nationality", "Points", "Position", "Year"]]
      )

    # Make sure to return the latest dataframe
    
    return df2  