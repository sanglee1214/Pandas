# regex = "^b.tter"


#READING & PRINTING THE DATASET

#Let's use the csv module to read and then print our dataset
#The csv module implements classes to read and write tabular data in CSV format.

#Importing csv & re
import csv
import re

#Opening the file that contains our csv data in 'r' mode
f = open("2015-data.csv", 'r')

# Calling the reader()
# function within the csv module with the file object as input
# reader () returns a reader object which will iterate over lines in the given csvfile.
csvreader = csv.reader(f)

#Converting the result to a list
#this helps with slicing in a bit
posts_with_header = list(csvreader)

#Using the csv module to read and assign our dataset to posts_with_header.
#Using list slicing to exclude the first row, which represents the column names
posts = posts_with_header[1:]

#Use a for loop and string slicing to print the first 10 rows of the dataset.
#for post in posts[:10]:
    #print(post)

# Testing for Matches

#With re.search(regex, string), we can check if string is a match for regex.
#If it is, it will return a match object. If it isn't, it will return None

#I DO

#Count the number of posts in our dataset that match the regular expression
#"of Reddit".
#Assign the count to of_reddit_count.

 #of_reddit_count = 0
#
# for row in posts:
#     if re.search("of Reddit", row[0]) != None:
#         of_reddit_count += 1
#
# print of_reddit_count

#ACCOUNTING FOR INCONSISTINCIES

#In regular expressions, square brackets are used to
#indicate that any character within the square bracket can fill the space.
# We can account for the inconsistency of people writing "of Reddit" versus "of reddit"
# using square brackets.

# of_reddit_count = 0
# for row in posts:
#     if re.search("of [Rr]eddit", row[0]) != None:
#         of_reddit_count += 1
#
# print of_reddit_count


#Escaping characters

#In our dataset, there are a lot of posts that use the [Serious] tag
#We'd like to search through our dataset to see how many posts have this tag,
#but the regular expression "[Serious]" does not do what we are looking for
#since square brackets serve a special function within regular expressions

#"[Serious]" will match any string that contains "S", "e", "r", etc.

#To deal with this sort of problem, we need to escape special characters.
#In regular expressions, escaping a character means indicating that you don't want the character to do anything special,
#and that it should be treated as any other character would be.
#We use "\" (backslash) to escape characters in regular expressions.


#Escape the square bracket characters to count the number
#of posts in our dataset that contain the "[Serious]" tag

# serious_count = 0
# for row in posts:
#     if re.search("\[Serious\]", row[0]) != None:
#         serious_count += 1
#
# print serious_count


#More inconsistency

#YOU DO:Refine the code to count how many
#posts have either "[Serious]" or "[serious]" in their title.
#Assign the count to serious_count.(5 minutes)



#
# serious_count = 0
# for row in posts:
#     if re.search("\[[Ss]erious\]", row[0]) != None:
#         serious_count += 1
#
# print serious_count




#You Do: Refine the code to count how many posts are tagged as serious,
# using either square brackets or parenthesis.
# Assign the count to serious_count. (5 minutes)


#
#
# serious_count = 0
# for row in posts:
#     if re.search("[\[\(][Ss]erious[\]\)]", row[0]) != None:
#         serious_count += 1
# print serious_count



#Multiple Regular expressions

#To combine regular expressions, we use the "|" character.


#You Do: Use the "^" character to count how many posts have the serious tag at the beginning of their title.
#Assign this count to serious_start_count.
# Use the "$" character to count how many posts have the serious tag at the end of their title.
# Assign this count to serious_end_count.
# Use the "|" character to count how many posts have the serious tag at either the beginning or end of their title.
# Assign this count to serious_count_final.
# 5 minutes





serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) != None:
        serious_start_count += 1
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) != None:
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) != None:
        serious_count_final += 1

print serious_start_count
print serious_end_count
print serious_count_final
