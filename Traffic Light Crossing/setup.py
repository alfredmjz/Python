import numpy as np
from traffic import *
from traffic_light import Traffic_Light, __init__

class Setup:
    '''
    This class initialize random default value for the environment of the 4-way traffic intersection.
    Running this will start the program.
    '''
    def __init__(self, traffic):
        '''
        Precondition:   Takes a list of exactly 4 Traffic_Light objects. Objects cannot be null
        Postcondition:  Each intersection will have a randomize number of traffic
                        Total traffic size is recorded
        '''
        traffic[0].number_of_traffic = np.random.randint(0,10)
        traffic[1].number_of_traffic = np.random.randint(0,10)
        traffic[2].number_of_traffic = np.random.randint(0,10)
        traffic[3].number_of_traffic = np.random.randint(0,10)
        self.traffic_size = traffic[0].number_of_traffic + traffic[1].number_of_traffic + traffic[2].number_of_traffic + traffic[3].number_of_traffic
    


if __name__ == '__main__':
    #Construct instances of Traffic_Light object for 4-way traffic intersection
    traffic_up = Traffic_Light("up")
    traffic_left = Traffic_Light("left")
    traffic_right = Traffic_Light("right")
    traffic_down = Traffic_Light("down")
    #Appends objects into list and intialize the environment
    traffic = [traffic_up, traffic_left, traffic_right, traffic_down]
    setup = Setup(traffic)

    #Initialize the state of all drivers (Refer cars.py for states)
    cars_up = traffic[0].initialize_cars()
    cars_left = traffic[1].initialize_cars()
    cars_right = traffic[2].initialize_cars()
    cars_down = traffic[3].initialize_cars()

    # for i in range(len(cars_up) - 1):
    #     print(cars_up[i].state)

    #test = Traffic.display(traffic)
 

