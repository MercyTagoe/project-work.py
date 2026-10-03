# Grade Book

# Create a dictionary called grades with at least 5 student
students = {
     "Nana Kofi": 93,
     "Fortune":  93,
 }

# Class Averagre
# Use a for loop to add up all the scores in grades.values()
total = 0
# your loop here

# Divide total by the number of students to get the average
 average = ?
 print the average (use :.1f to show one decimal place)

# High and Low
# Use max() with key=grades.get to find the top student's name
 Use min() with key=grades.get to find the bottom student's name
 Print both names and their scores

# Student Search
# Ask the user to type a student name using input()
# Use grades.get(name, None) to look up their score
 If found print the score
 If not found print a friendly "not found" message