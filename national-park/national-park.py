# Analyzing National Park visitor data from 2016 from here: https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year)

import numpy as np
import pandas as pd

nps = pd.read_table('csv/nps-2016.txt')

print(nps.dtypes)

