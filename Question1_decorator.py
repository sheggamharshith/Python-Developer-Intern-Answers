#  Write a timer function to be used as a decorator to time the execution of the following function - 

# def waste_time():
#     x=0
#     for i in range(0,1000):
#         x+=i

# importing time packages for this program
import time
# creation of decorator that takes a function and calculates the runtime of the function and prints the time 
# of the function 

def run_time_caluclator(input_function):

    """ This function takes input_as function and prints runtime execution  """

    # invoking the pref_counter method in time 
    # print("Timer has started its clock")
    starting_time = time.perf_counter()

    # input_function is invoked 
    input_function()
     
    #timer_object.stop()
    #print("timer has stopped its counting ")
    ending_time = time.perf_counter()

    #Calculating the time i.e final-initial and printing 
    print("Your wating time for the function is {:0.4f} seconds".format(ending_time-starting_time))
 

# calling the decerator
@ run_time_caluclator
def waste_time():
    x=0
    for i in range(0,1000):
        x+=i