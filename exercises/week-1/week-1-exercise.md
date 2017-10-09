# Week 1 exercise

Your editor has assigned you to do a story about visitation at the nation's national parks.  She's asked you to answer two questions, using Python.

1. What was the mean number of visits at all National Parks in 2016?
2. What was the mean number of visits at the most popular National Parks, with more than 5 million visitors, in 2016?

## Getting Started

To get started, download the ZIP file, [national-park.zip](national-park.zip). Unzip it on your Desktop. It contains the contents of the "data" folder -- a text file ([nps-2016.txt](data/nps-2016.txt)) with a count of visits to each National Park in 2016 -- and the contents of the "files" folder -- two python files, [national-park.py](files/national-park.py) and [national-park-answers.py](files/national-park-answers.py).    

## Importing libraries and reading in the data.

In Spyder, open the file national-park.py.  Unless you want to cheat, don't open national-park-answers.py, because it contains, you guessed it, answers!

In Spyder, open the file national-park.py.  This is code to get you to a point where you can calculate the answers the questions require.  Essentially, we are importing numpy; importing pandas (which we haven't used yet, but is a much nicer way to read in data); reading in the data as a pandas data.frame; isolating the column with visit numbers; and transforming the pandas data.frame into a numpy array.

After you do that, write some functions to calculate the mean for all parks, and the mean for parks with more than 5 million visitors.  
