import numpy as np
from traffic import *
from traffic_light import Traffic_Light, __init__
#Class contains all default values"
class Setup:
    def __init__(self, traffic):
        traffic[0].number_of_traffic = np.random.randint(0,10)
        traffic[1].number_of_traffic = np.random.randint(0,10)
        traffic[2].number_of_traffic = np.random.randint(0,10)
        traffic[3].number_of_traffic = np.random.randint(0,10)
        self.traffic_size = traffic[0].number_of_traffic + traffic[1].number_of_traffic + traffic[2].number_of_traffic + traffic[3].number_of_traffic



if __name__ == '__main__':
    for i in range(4):
        traffic_up = Traffic_Light("up")
        traffic_left = Traffic_Light("left")
        traffic_right = Traffic_Light("right")
        traffic_down = Traffic_Light("down")
    traffic = [traffic_up, traffic_left, traffic_right, traffic_down]
    setup = Setup(traffic)
    test = Traffic.display(traffic)
 

