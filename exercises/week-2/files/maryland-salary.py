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

# Use pandas to read in the data and store the dataframe as a variable you can call later. Note, reading in the data may fail if you haven't set the working directory.

# Question 1: Can you produce a list of all the column names?

# Question 2: What was the highest YTD_gross_earnings for an employee in 2016? Hint: you can use one short bit of code to get the answers to question 2 through 5.

# Question 3: What was the lowest YTD_gross_earnings for an employee in 2016?

# Question 4: What was the average (mean) salary (YTD_gross_earnings) in 2016?

# Question 5: What was the median (50th percentile) salary (YTD_gross_earnings) in 2016?

# Question 6: How much did the state spend on employee salaries (YTD_gross_earnings) in 2016?

# Question 7: Can you produce a list of all the organizations represented in the data set? After you generate it, closely review the list.  What problem do you see that might hinder your ability to ask questions about some organizations?  Think about how you might correct the problem you've identified (no need to write code at this point, just think about it).

# Question 8: Which 10 employees got the most money (YTD_gross_earnings) from a single organization in 2016, and how much did each of them make? What do they have in common?

# Question 9: Who was the highest paid non-University of Maryland employee?

# Question 10: What was the mean salary (YTD_gross_earnings) for University of Maryland employees? How does that compare to the mean for St. Mary’s College of Maryland employees?

# Question 11: What other questions can you ask of this dataset?
