# Patriot
# Program: Hydro
# Prototype 2 Final

# (1) This imports the built-in functions that will assist us in analyzing and organize the data
import csv
import pandas as pd

#------------------------------------------------------------------------------------------------------------------------------------

# (2) This reads our excel file with our categorized data

# Reading the csv file
df = pd.read_csv('Water_Quality_Data_2019.csv', encoding = 'utf-8-sig')

#------------------------------------------------------------------------------------------------------------------------------------

# (3) If our lines are unorganized, this will group them and will make it easier to compute

# Group by State (If we have more states, but for now it is just Virginia as Sample)
state_group = df.groupby('State')

#------------------------------------------------------------------------------------------------------------------------------------

# (4) User prompts to ask for their location

#Prompt the user for their state of residence
user_state = str(input("State of resisdence?: "))

#Prompt the user for their city of residence in their State
user_city = str(input("City of residence in {0}?: ".format(user_state)))

#------------------------------------------------------------------------------------------------------------------------------------

# (5) Filters our data based on the user's location and make a filtered file for the data and read the new file

filtered_df2 = (df['City'] == user_city)
df2 = df[filtered_df2]

#make new csv based on user inputs
df2.to_csv('just_user_city.csv')
df2 = pd.read_csv('just_user_city.csv', encoding = "utf-8-sig")

#------------------------------------------------------------------------------------------------------------------------------------

# (6) In some cases there are multiple utilities for one city so we have code here to count how many utilities there are

#this code finds all duplicates of that city not definite if this works (confused on this part, trying to get one value for the duplicate count)
count_city = len(df2['City'])

#------------------------------------------------------------------------------------------------------------------------------------

# (7) We assign variables that will have just the data in one column to be able to ask the user which utility they use to get tap water
#so we can get the exact number from columns
col_utility = df2['Utility Name']
col_cont_num = df2['Total Number of Contaminants']

#------------------------------------------------------------------------------------------------------------------------------------

# (8) A function that will rate the water contamination level on a scale, in user-friendly and universal format, color!

#Function that rates the contamination level in that water system
def rating(num):
	if (num >= 0) and (num <= 13): #0-13 is Green level
		return 'Green'
	elif (num >= 14) and (num <= 20): #14-20 Yellow level
		return 'Yellow'
	elif (num >= 21): #21 above is Red level
		return 'Red'

#------------------------------------------------------------------------------------------------------------------------------------

# (9) If the city the user lives in has multiple water systems. this portion will help identify the user water system in their city by user response of Yes or No.

#locator of utility based on user responses and final output
if count_city > 1:
	answer = str(input("There are {0} number of Utilites in {1}.\nIs this your utility water system name?: {2}\n(Y/N)\n ".format(count_city,user_city,col_utility[0])))

	if answer == "Y":
		print("The total number of water contaminants found in the chosen utility in your city is...\n{0}\nLevel: {1}".format(col_cont_num[0],rating(int(col_cont_num[0]))))

	elif answer == "N":

		for i in range(1,len(col_utility)):
			answer = input("Is this your utility water system name?: {0}\n(Y/N)\n ".format(col_utility[i]))

			if answer =='Y':
				print("The total number of water contaminants found in the chosen utility in your city is...\n{0}\nLevel: {1}".format(col_cont_num[i],rating(int(col_cont_num[i]))))
				break

			elif answer == 'N':
				continue

#------------------------------------------------------------------------------------------------------------------------------------

# If there is one water system in their city it makes it simpler for us to give them their total number of contaminants and rating

elif count_city == 1:

	print("The total number of water contaminants found in the utility ({0}) in your city ({1}) is...\n{2}\nLevel: {3}".format(col_utility[0],user_city,col_cont_num[0],rating(int(col_cont_num[0]))))

# If we have an invalid input then we get an error and they must restart the program to get their desired information.

else:
	print("error: restart program")

