# Analyzing National Park visitor data from 2016 from here: https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year)

## First, import the numpy package and pandas. We haven't used pandas yet, but we'll get to it very soon, and it's soooo much more user friendly for reading in data, compared with numpy.

import numpy as np
import pandas as pd

# Read in the data (using pandas)
# Note, reading in the data may fail if you haven't set the working directory to be able to find the file. On the top menu above, click Python or Spyder (item just right of the apple icon), then preferences.  Select global or current working director, and set the folder to national-park.
parks = pd.read_table('data/nps-2016.txt')

## If you want to see the data in a spreadsheet form, go to the window just above the console and click the "variable explorer" button.  Then double click on the parks item.  It should come up as a spreadsheet.

# Filter to remove everything but the "Value" column, which has the visit data.
parks_visits = parks.filter(['Value'])

#Now store the visit column as an array that numpy understands.
parks_visits_array = parks_visits.values

# Calculate the mean visits for all parks using numpy.

# Calculate the mean for the largest parks over 5 million using numpy. 
