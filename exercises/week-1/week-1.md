# Week 1 - Merrill Python Data Study Hall
#### Oct. 9, 2017
#### Builds on first course in [Python for Data Science](https://www.datacamp.com/tracks/data-scientist-with-python) track: [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science).

## Agenda for Week 1

### Openers

Welcome to Merrill Python Data Study Hall!  

There are four main collaborative platforms we'll be using to learn. If you're confused about any of these, message Sean Mussenden (smussend@umd.edu) or @seanm on Slack.
* The *Slack channel*, where we can share information and help each other solve problems.
* The *DataCamp group*, where we'll learn Python by completing online courses.
* This *GitHub repo*, which we'll use to share data sets, tutorials, in-person study hall agendas, and more.
* The *in-person study hall* (not required, but encouraged) in 3210 Knight Hall Mondays from 11 a.m. - 1 p.m. If you can't make it, do your best to follow along with the weekly coursework and in-person agenda.

### Questions/Reminders about Slack Channel

* Please get in the habit of checking the Slack channel. Would it be useful to send a daily email digest of Slack activity?
* Even during in-person meetings, please try to post your questions/problems to the Slack channel. This helps people who can't make it stay involved.

### Study Hall Structure

*Discussion question:* How does completing a new course every other week sound?

*Discussion question:* How should we use our in-person sessions?

*Here's one proposal:* during "on weeks" -- a week when a course is scheduled for completion -- we work collaboratively on a mini-project to reinforce coursework.  During "off weeks," we work on the online courses, learn helpful coding tools (like GitHub), and discuss/prepare future mini-projects.

### Installing Python 3
There are two main versions of Python in use: Python 2 and Python 3.

We will use Python 3. To make sure you have the latest version of Python 3, download it [here](https://www.python.org/downloads/), double click on the downloaded package, and follow the steps.

Test that it's installed.  Open "Terminal" on a Mac or "Command Prompt" on Windows. Type "python3" to enter the python environment.  

Try printing "Hello, World" by typing `print("Hello,World")`.

To exit python, type `exit()`   

### Installing Anaconda
[Anaconda](https://www.anaconda.com/what-is-anaconda) is a popular platform for using python to do data journalism and data science. It bundles together thousands of useful python packages, and comes pre-installed with several Integrated Development Environments (IDEs), including the one we'll be using, Spyder.

Download the version for Python 3 [here](https://www.anaconda.com/download/#macos) and install it.

### Running Spyder

Launch Anaconda Navigator.  Then launch Spyder, an Integrated Development Environment for python.

On the left side of the screen is a sample script file, where we'll write some sample code.  The results of our code will run in the iPython console on the lower right.

And when we load in data, we'll be able to review it using the variable explorer in the upper right.

### Exercise for Today

Your editor has assigned you to do a story about visitation at the nation's National Parks.  They've asked you to answer two question.

1. What was the mean number of visits at all National Parks in 2016?
2. What was the mean number of visits at the most popular National Parks, with more than 5 million visitors, in 2016?

To get started, download the ZIP file, national-park.zip, and put it on your Desktop.  In Spyder, open the file national-park.py.  Run the first 16 lines to load numpy, load pandas, read in the data, and transform the column we care about into a numpy array. Then, find the answers to the two questions.  

If you get stuck, the file national-park-answers.py has answers. 
