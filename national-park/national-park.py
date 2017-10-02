# Analyzing National Park visitor data from 2016 from here: https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year)

import numpy as np
import pandas as pd

# Read in the data

parks = pd.read_table('csv/nps-2016.txt')

# Get ready to ask our first question: what is the average number of visits to a National Park in 2016?

# Filter out just the value column, and store it as a numpy array so that we can ask questions of it. 
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




##nps_mean = np.mean(nps_visits)
##print(nps_mean)
##nps = pd.read_table('csv/nps-2016.txt')

# np_baseball is available


# Create np_height from np_baseball
##np_height = np.array(np_baseball [:,0])

# Print out the mean of np_height
##print(np.mean(np_height))

# Print out the median of np_height
##print(np.median(np_height))

##nps_visits_mean = nps["Value"].mean()
##print(nps_visits_mean)


