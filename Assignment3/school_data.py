# school_data.py
# Braden Tink
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
school_dictionary = {
    0 : ("Centennial High School" , "1224"),
    1 : ("Robert Thirsk School" , "1679"),
    2 : ("Louise Dean School" , "9629"),
    3 : ("Queen Elizabeth High School" , "9806"),
    4 : ("Forest Lawn High School" , "9813"),
    5 : ("Crescent Heights High School" , "9815"),
    6 : ("Western Canada High School" , "9816"),
    7 : ("Central Memorial High School" , "9823"),
    8 : ("James Fowler High School" , "9825"),
    9: ("Ernest Manning High School" , "9826"),
    10 : ("William Aberhart High School" , "9829"),
    11 : ("National Sport School" , "9830"),
    12 : ("Henery Wise Wood High School" , "9836"),
    13 : ("Bowness High School" , "9847"),
    14 : ("Lord Beaverbrook High School" , "9850"),
    15 : ("Jack James High School" , "9856"),
    16 : ("Sir Winston Churchill High School" , "9857"),
    17 : ("Dr. E. P. Scarlett High School" , "9858"),
    18 : ("Jown G Diefenbaker High School" , "9860"),
    19 : ("Lester B. Pearson High School" , "9865")

}


#List contain all the base data given to us for the assignment
year_list = [[year_2013], [year_2014], [year_2015], [year_2016],
             [year_2017], [year_2018], [year_2019], [year_2020],
             [year_2021], [year_2022]] 


#Creation of an array class and variables to be be used throughout the program
class Array:
    def __init__(self, given_data: list):
        self.given_data = given_data
        self.year_list = []
        self.final_list = []
        self.tmp_array = np.array 
        self.final_array = np.array
        self.index = 0
        self.school_key = 0
        self.num_grades = 3
        self.school_details = "Empty"
    #Reshape method that takes in one of the year list and reshapes it 
    #Then appends it to the final list 
    def array_reshape(self):
        
        #Set the tmp_array to the index list item as an array
        #Reshape the 1D array to a 2D array 
        #Hold the resulting array in a fianl list 
        self.tmp_array = np.array(self.given_data[self.index])
        array_length = int(self.tmp_array.size / self.num_grades)
        self.tmp_array = self.tmp_array.reshape(array_length,self.num_grades)
        self.final_list.append(self.tmp_array)
    
    #Create the final array using the np.dstack taking the 
    #in the final list as the argument 
    def array_concat(self):
        #set the final 3D array using the np.dstack method taking in the final list as the argument
        self.final_array = np.dstack(self.final_list)
        
    #User method that gets compred to the values in the dictionary 
    #If found continue else raise a value error and ask for another value
    def user_input(self):
        temp_bool = False
        while temp_bool == False:
            self.user_input = input("Please enter either a school name or code ")
            
           #Try statement looking for value 
            try:
                for key in school_dictionary:
                    #check user input agaisnt the list inside the dictionary   
                    temp_list = school_dictionary[key]
                    for list_elements in temp_list:
                        if list_elements == self.user_input:
                            self.school_key = key
                            temp_bool = True
                            print("You entered a valid school name or code")
                            self.school_details = school_dictionary[key]
                            break
                if temp_bool == True:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("You must enter a valid school name or code")

        
        
        
    #Requested school Statistics for a given school
    def calculate_statistics(self):
        print("**** Requested School Statistics ****")
        print("")


        #print School info
        print("Selected School and code: " + (str(self.school_details)))
        #print(self.school_key)
        #print(len(self.final_array))

        #Mean Enrollment 10 over all years
        #Loop through all 10 years and find the mean enrollment for grade 10
        tmp_output = 0
        count = 0 
        i = 0
        while i < 10:
            #self.tmp_array = self.final_array[self.school_key, 0, 1][np.logical_not(np.isnan(self.final_array[self.school_key, 0, i]))]
            #tmp_output = tmp_output + self.final_array[self.school_key, 0, i]

            self.tmp_array = self.final_array[self.school_key, 0, i][np.logical_not(np.isnan(self.final_array[self.school_key, 0, i]))]
            if self.tmp_array.size > 0:
                tmp_output = tmp_output +self.tmp_array[0]
                count += 1
            i += 1
        tmp_output = int(tmp_output) // count
        print("Mean Enrollment Grade 10: " + str(tmp_output))
        
        #Mean Enrollment 11 over all years
         #Loop through all 10 years and find the mean enrollment for grade 11
        count = 0
        tmp_output = 0 
        i = 0
        while i < 10:
            #tmp_output = tmp_output + self.final_array[self.school_key, 1, i]
            self.tmp_array = self.final_array[self.school_key, 1, i][np.logical_not(np.isnan(self.final_array[self.school_key, 1, i]))]
            if self.tmp_array.size > 0:
                tmp_output = tmp_output +self.tmp_array[0]
                count += 1
            i += 1
        tmp_output = int(tmp_output) // count
        print("Mean Enrollment Grade 11: " + str(tmp_output))
        
            
        #Mean Enrollment 12 over all years 
         #Loop through all 10 years and find the mean enrollment for grade 12
        count = 0
        tmp_output = 0 
        i = 0
        while i < 10:
            #tmp_output = tmp_output + self.final_array[self.school_key, 2, i]
            self.tmp_array = self.final_array[self.school_key, 2, i][np.logical_not(np.isnan(self.final_array[self.school_key, 2, i]))]
            if self.tmp_array.size > 0:
                tmp_output = tmp_output +self.tmp_array[0]
                count += 1
            i += 1
        tmp_output = int(tmp_output) // count
        print("Mean Enrollment Grade 12: " + str(tmp_output))
       
        #Set tmp_array to the selected school key array
        #from the final array split it so we grab a single array out of the 3d array repersenting 1 school
        self.tmp_array = self.final_array[self.school_key][np.logical_not(np.isnan(self.final_array[self.school_key]))]
        
        #Max Enrollment all years
        print("Max Enrollment For Each Grade: " + str(int(np.floor(np.max(self.tmp_array))))) 
      
        #Min Enrollment all years
        print("Min Enrollment For Each Grade: " + str(int(np.floor(np.min(self.tmp_array)))))
        
        #Enrollment Totals years
        print("Total Enrollment Per Year")
        self.tmp_array = self.final_array[self.school_key][np.logical_not(np.isnan(self.final_array[self.school_key]))]
        array_length = int(self.tmp_array.size / self.num_grades)
        self.tmp_array = self.tmp_array.reshape(self.num_grades, array_length)
        self.tmp_array = np.transpose(self.tmp_array)
        context_year = 2013
        total = 0
        i = 0
        while i < 10:
            print
            if ( i < array_length):
                print("Total Enrollment for " + str(context_year) + ": " + str(int(np.sum(self.tmp_array[i]))))
            else: 
                print("Total Enrollment for " + str(context_year) + ": " + "0")
            context_year += 1
            i += 1
        
        print("Total Enrollment: " + str(int(np.sum(self.tmp_array))))

        print("Mean Enrollment: " + str(int(np.sum(self.tmp_array) / 10)))

        #All enrollment over 500
        self.tmp_array = self.final_array[self.school_key][np.logical_not(np.isnan(self.final_array[self.school_key]))]
        array_length = int(self.tmp_array.size / self.num_grades)
        self.tmp_array = self.tmp_array.reshape(self.num_grades,array_length)
        self.tmp_array = np.transpose(self.tmp_array)
        tmp_output = 0
        i = 0

        self.tmp_array = (self.tmp_array[self.tmp_array > 500])

    
        if self.tmp_array.size == 0:
            print("No enrollemnts over 500")
        else:
            tmp_output = tmp_output / array_length
            print("All enrollment over 500 mean: " + str(int(np.median(self.tmp_array))))

    #General statistics over all schools
    def general_statistics(self):
        print("**** General School Statistics ****")
        #print the mean for 2013
        print("Mean Enrollment 2013: " + str(int(np.mean(year_2013)))) 
       
        #print the mean for 2022 and remove all nan from the arrays
        print("Mean Enrollment 2022: " + str(int(np.mean(year_2022[np.logical_not(np.isnan(year_2022))]))) )
       
        #Total 2022 grad class
        self.tmp_array = year_2022[np.logical_not(np.isnan(year_2022))]
        array_length = int(self.tmp_array.size / self.num_grades)
        self.tmp_array = self.tmp_array.reshape(array_length,self.num_grades)
        self.tmp_array = np.sum(self.tmp_array,axis=0)[2]
        print("Graduate total:" + str(int(self.tmp_array))) 
       
        #Highest enrollment over all schools excluding nan
        print("Highest enrollment: " + str(int(np.max(self.final_array[np.logical_not(np.isnan(self.final_array))]))))
        #Lowest enrollment over all schools excluding nan
        print("Lowest enrollment: " + str(int(np.min(self.final_array[np.logical_not(np.isnan(self.final_array))]))))
    
#Def main function  
def main():  
    print("ENSF 592 School Enrollment Statistics")
    #Create a array object
    array_obj = Array(year_list)
    #From the list go through and reshape all the arrays to 20x3

    #Index throught the given data list holding each item in a tmp array as well as the current index in an int
    #pass the array_obj into the reshape method
    for index, item in enumerate(array_obj.given_data):
        array_obj.tmp_array = array_obj.given_data[index]
        array_obj.index = index
        Array.array_reshape(array_obj)
    
    #After reshapping pass the array_obj into the concat method to bring all the data into one 3D array
    Array.array_concat(array_obj)

    #print(array_obj.final_array)
    print("Shape of full data array: " + str(array_obj.final_array.shape))
    print("Dimesions of full array: " + str(array_obj.final_array.ndim))
   
    #Call user input and pass in array object
    Array.user_input(array_obj)
    
    #Call calculate_statistics and pass in the array object 
    Array.calculate_statistics(array_obj)

    #Call general_statistics and pass in the array object 
    Array.general_statistics(array_obj)


if __name__ == '__main__':
    main()

