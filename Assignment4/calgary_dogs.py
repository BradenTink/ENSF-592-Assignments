# calgary_dogs.py
# Braden
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

#Import both numpy and pandas as np and pd
import numpy as np
import pandas as pd

#Main function of code 
def main():

    # Import data from xlsx and store the data in all_data
    all_data = pd.read_excel(r"./CalgaryDogBreeds.xlsx", usecols = [0,1,2,3], index_col = [2,1])

    print("ENSF 592 Dogs of Calgary")
    # User input stage
    #Ask for user inout if not found print error
    #While true keep asking for user input
    #loop breaks when a entered dog breed is found 
    while (True):
        #Set dog_name equal to user inout
        dog_name = input("Please Enter a Dog Breed: " )
        #Set the user input to all upper case letters 
        dog_name = dog_name.upper()
        #Try statement where you look for the entered dog name is contianed in all_data      
        try:
            if (dog_name in all_data.index):         
                break
            else:
                #Rasie value error if its not in the all_data.index
                raise ValueError
        except ValueError:   
            print("Dog Breed was not found. Please try again.")
    
    
   
    #Year total of how many dogs registered of the full data set in 2021,2022,2023 
    year_2021_total = all_data.loc[all_data['Year'] == 2021, 'Total'].sum()
    year_2022_total = all_data.loc[all_data['Year'] == 2022, 'Total'].sum()
    year_2023_total = all_data.loc[all_data['Year'] == 2023, 'Total'].sum()
    
    #Creation of a slice based on the dog name 
    #From the clice then create the 2021,2022,2023 data set 
    dog_data = all_data.loc[dog_name]
    dog_data_2021 = dog_data.loc[dog_data['Year'] == 2021, 'Total'].sum()
    dog_data_2022 = dog_data.loc[dog_data['Year'] == 2022, 'Total'].sum()
    dog_data_2023 = dog_data.loc[dog_data['Year'] == 2023, 'Total'].sum()
    
   
    # Data anaylsis stage
    # Part 1
    #Find all year where dog is found using the groupby in pandas. If its over 1 then create a slice claled year_data
    year_data = (dog_data.groupby("Year").count() > 1)
    #Create a set from the year_data slice
    print("The " + dog_name + " was found in the top breeds for the years: " + str((set(year_data.index))).replace("{","").replace("}","").replace("'","").replace(",",""))
 
    # Part 2 The following print gets me the total dogs of that breed over all years
    dog_total = dog_data.sum()
    print("There have been " + str(dog_total.Total) + " " + dog_name + " dogs registered total.")
    
    #Part 3 
    #Calcualte the percentage of a type of dog agasint the total dogs that year to to 6 decimal places 
    print("The " + dog_name + " was " + str('{:.6f}'.format((dog_data_2021/year_2021_total) * 100)) + "% of the top breeds in 2021.")
    print("The " + dog_name + " was " + str('{:.6f}'.format((dog_data_2022/year_2022_total) * 100)) + "% of the top breeds in 2022.")
    print("The " + dog_name + " was " + str('{:.6f}'.format((dog_data_2023/year_2023_total) * 100)) + "% of the top breeds in 2023.")
    
    #Part 4
    #All_data get set to the sum of all data so the total cann be used when calcualte the total percentage of a breed over all years
    all_data = all_data.sum()
    #Print the percentage of a specific breed over all years to 6 decimal places
    print("The " + dog_name + " was " + str('{:.6f}'.format((dog_total.Total / all_data.Total) * 100)) + "%  of top breeds across all years.")
   
    #Part 5
    #Find the total count a single month shows up in the list store that in month_data
    #From month_data find the max value 
    #Using the max value create a mask where the month value must be equal to the max reassign month_data to that dataset
    #Print out the set of months from month_data showing all months that are equal to the max value 
    month_data = (dog_data.groupby("Month").count())
    max_value = (month_data.Total.max())
    month_data = (dog_data.groupby("Month").count() == max_value )
    month_data = month_data[month_data['Year'] == True]
    print("Most popular month(s) for the " + dog_name + " dogs: " + str(set(month_data.index)).replace("{","").replace("}","").replace("'","").replace(",",""))

if __name__ == '__main__':
    main()
