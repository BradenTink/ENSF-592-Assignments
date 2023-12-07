# input_processing.py
# Braden Tink, ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 git repository.
# You must include the code provided below but you may delete the instructional comments.
# You maybnm,. add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    #Method called at the start of main intilzing the valeus of my object
    #sensor_obj is passed in as the argument 
    def __init__(self):
        self.color = "green"
        self.person = "no"
        self.car = "no"
        self.user_array= [0,1,2,3]
        #self.user_argument = "no"

    """
    #update status method gets called which asks the user for the two arguments that this code need
    #Method will get passed in my sesnor object 
    #Method will then assign two user inputs to user_input, and user_argument
    #Based on the first input the user_argument gets set to its according value
    """

    def update_status(self):
        
        #First user input will get assinged to the sensor_obj user_input variable
        temp_bool = False

        #While loop looking at temp_bool varaiable when set to true loop stops
        #Loop ensures the user inout is one of the options
        while temp_bool == False:
            print("Are any changes detected in the vision sensor")
            self.user_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            
            #Try to cast the user input to an int if fails ask for another input and loop continues 
            try:
                self.user_input = int(self.user_input)
                #check if the user_inout is inside the user_array if true then end the while loop by setting tempbool to true 
                #Else the temp_bool is still set to false and we raise a value error
                if self.user_input in self.user_array:
                    temp_bool = True
                else:  
                    raise ValueError
            except ValueError:
                print("You must select 0, 1, 2, 3")
                print()

        
        #if the user enters 0 then if statement skips to the next user input
        #if a none 0 value is called then run the appropriate set
        if (self.user_input != 0):
            temp_bool = False
            #While loop implemented to make sure the second argument is one of the correct vision entries
            #If input is not one of the 5 choices ask the user for another input
            while temp_bool == False:
                self.user_argument = input("What change has been identified? ")

                #Based on the first user input set corresponding variable
                if self.user_input == 1 and (self.user_argument == "green" or self.user_argument == "red" or self.user_argument == "yellow"): 
                    self.color = self.user_argument
                    temp_bool = True
                    print()
                elif self.user_input == 2 and (self.user_argument == "yes" or self.user_argument == "no"):
                    self.person = self.user_argument
                    temp_bool = True
                    print()

                elif self.user_input == 3 and (self.user_argument == "yes" or self.user_argument == "no"):
                    self.car = self.user_argument      
                    temp_bool = True
                    print()
                else: 
                    print("Invalid vision change.")
                    print()
            

#Method takes in sensor_obj as an argument 
#Based on the current status of Color,Person,Car method show how the user should proceed
#3 outputs include proceed,caution,STOP
def print_message(sensor):

    if (sensor.color == "green" and sensor.person == "no" and sensor.car == "no"):
        print("Proceed")
        print()

    elif (sensor.color == "yellow" and sensor.person == "no" and sensor.car == "no"):
        print("Caution")
        print()

    else: 
        print("STOP")
        print()

    #Output the current status of the object
    print("Light = " + sensor.color + " , Pedestrian = " + sensor.person + " , Vehicle = " + sensor.car + ".")        
    print()

#Main function creates the ovject that runs a while loop until the user enters a 0 to stop the loop
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")
    
    #Creating a new obect sensor_obj from the Sensor class
    sensor_obj = Sensor()

    #While loop that will run infinitly until break statement is hit inside the loop  
    while True:
        
        #Call the update status method passing in my sensor method 
        Sensor.update_status(sensor_obj)

        #if statement looking for user_input to be 0 
        #if user_input of the object is 0 then break the while else
        #call the print_message method passing in my object
        if (sensor_obj.user_input == 0):
            break
        else:
            print_message(sensor_obj)

    
# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
