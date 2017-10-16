#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:35:12 2017

@author: smussend
"""
# An exercise in using pandas to analyze data, using the 2016 Maryland state employees salary data, via Baltimore Sun. Data link: https://github.com/baltimore-sun-data/maryland-salaries. Interactive database link: http://data.baltimoresun.com/salaries/state/cy2016/.

# Do your best to work with pandas as much as possible here, as it's the standard for working with tabular data. The DataCamp lesson due next week goes into detail on pandas. Keep in mind that may be multiple ways to answer the question; find one that works!

# Four resources you may find useful, in addition to DataCamp:
# Pandas cheat sheet: https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
# Pandas documentation: https://pandas.pydata.org/pandas-docs/stable/basics.html
# Pandas tutorials: https://pandas.pydata.org/pandas-docs/stable/tutorials.html
# And, of course, Google

# Important note about the data: though this data was published by the Baltimore Sun, it's not totally clean.  Typically, before beginning our analysis, we'd walk through a series of steps to prepare the data, searching for flaws that could compromise our analysis.  And as we analyze the data and uncover other problems, we'd update our cleaning scripts. Because the purpose of this exercise is to get a little more familiar with the basics of pandas -- and not an exercise in data cleaning -- we're going to work with it even though we haven't done a robust cleaning yet.  We'll do that in future exercises.


# First, import the numpy and pandas packages.

import numpy as np
import pandas as pd

# Use pandas to read in the data and store the dataframe as a variable. Note, reading in the data may fail if you haven't set the working directory.

salary = pd.read_csv('../data/state-cy-2016.csv')

# Question 1: Can you produce a list of all the column names?
# Answer 1: One way to do it is to use .info() to get column names and a count of values in each column.

salary.info()

# Question 2: What was the highest YTD_gross_earnings for an employee in 2016? Hint: you can use one short bit of code to get the answers to question 2 through 5.
# Answer 2: $2.67 million.

salary.describe()

# describe() gives summary statistics - mean, standard deviation, min, max, and the values at the 25th, 50th and 75th quartiles -- in addition to a count of records.

# Question 3: What was the lowest YTD_gross_earnings for an employee in 2016?
# Answer 3: $0

# Question 4: What was the average (mean) salary (YTD_gross_earnings) in 2016?
# Answer 4: $39,315

# Question 5: What was the median (50th percentile) salary (YTD_gross_earnings) in 2016?
# Answer 4: $35,000

# Question 6: How much did the state spend on employee salaries (YTD_gross_earnings) in 2016?
# Answer 6: $5.67 billion.

salary['ytd_gross_earnings'].sum()

# Question 7: Can you produce a list of all the organizations represented in the data set? After you generate it, closely review the list.  What problem do you see that might hinder your ability to ask questions about some organizations?  Think about how you might correct the problem you've identified (no need to write code at this point, just think about it).
# Answer 7: Store as a DataFrame the organizations in the state, by using unique(), is one way to do it.

organizations = pd.DataFrame(salary.organization.unique())

# Question 8: Which 10 employees got the most money (YTD_gross_earnings) from a single organization in 2016, and how much did each of them make? What do they have in common?

topemployees = pd.DataFrame(salary.sort_values(by='ytd_gross_earnings', axis=0, ascending=False), columns=['first_name', 'last_name', 'organization', 'ytd_gross_earnings'])

# Answer 8: They're all University of Maryland employees.
# first_name	last_name	organization	ytd_gross_earnings
# RANDY	EDSALL	UNIVERSITY OF MARYLAND	2673000
# MARK	TURGEON	UNIVERSITY OF MARYLAND	2649000
# DANIEL	DURKIN	UNIVERSITY OF MARYLAND	2406000
# BRENDA	FRESE	UNIVERSITY OF MARYLAND	1103000
# STEPHEN	BARTLETT	UNIVERSITY OF MARYLAND	957000
# JAY	PERMAN	UNIVERSITY OF MARYLAND	929000
# JOHN	OLSON	UNIVERSITY OF MARYLAND	878000
# EDWARD	REECE	UNIVERSITY OF MARYLAND	822000
# BARTLEY	GRIFFITH	UNIVERSITY OF MARYLAND	792000
# JOSEPH	FRIEDBERG	UNIVERSITY OF MARYLAND	780000


# Question 9: Who was the highest paid non-University of Maryland employee?
# Answer 9: David Wilson, Morgan State.

topemployeesnoumd = topemployees[topemployees.organization != 'UNIVERSITY OF MARYLAND']

# Question 10: What was the mean salary (YTD_gross_earnings) for University of Maryland employees? How does that compare to the mean for St. Mary’s College of Maryland employees?
# UMD - 51,948.9
# SMC - 15,145.16

organizationmeans = ( salary
    .groupby('organization')['organization', 'ytd_gross_earnings']
    .agg('mean')
    .sort_values(by='ytd_gross_earnings', axis=0, ascending=False)
     )

# Question 12: How many employees does the Maryland Department of the Environment have in the dataset?
# Answer 12: 34,774

organizationcount = salary['organization'].value_counts()

# Question 13: What other questions can you come up with to ask of this data?
