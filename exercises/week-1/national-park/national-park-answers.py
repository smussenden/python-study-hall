# Analyzing National Park visitor data from 2016 from here: https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year)

## First, import the numpy package and pandas (which we haven't used yet)

import numpy as np
import pandas as pd

# Read in the data (using pandas)

parks = pd.read_table('data/nps-2016.txt')

# Filter out just the value column, and store it as a numpy array so that we can ask questions of it.  You can use variable explorer in the right window to look at the data.
parks_visits = parks.filter(['Value'])
print(parks_visits)
parks_visits_array = parks_visits.values
print(parks_visits_array)

# Calculate the mean. 
parks_visits_mean = np.mean(parks_visits_array)
print(parks_visits_mean)

# Calculate the mean for the largest parks
parks_visits_xl = parks_visits_array[parks_visits_array > 5000000]
parks_visits_xl_mean = np.mean(parks_visits_xl)
print(parks_visits_xl_mean)