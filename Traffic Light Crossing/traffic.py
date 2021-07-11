import numpy as np
from setup import *


class Traffic:

    def display(traffic):
        '''
        Takes list of traffic object and prints the number of traffic on each intersection and the map of the road

        >>> display(list_of_traffic)

                |        |
                |   1    |
        ________|        |________

        0                      3
        ________          ________
                |        |
                |        |
                |        |

        '''

        print("\t| \t |\t",
            "\t| \t |\t",
            f"\t|   {traffic[0].number_of_traffic}\t |\t",
            sep="\n")
        print("________|\t |________",
            "\t\t\t",
            f" {traffic[1].number_of_traffic}\t\t\t{traffic[2].number_of_traffic}",
            "________\t  ________",
            sep="\n")
        print("\t| \t |\t",
            f"\t|   {traffic[3].number_of_traffic}\t |\t",
            "\t| \t |\t",
            "\t| \t |\t",

            sep="\n")

    #TODO
    def startTrafficLight(self, num_of_rotation):
        self.traffic[0:4].status = None

        while(self.traffic[4] != num_of_rotation):
            if(self.traffic[0].elapsed_red_light == 8):
                self.traffic[0:1].elapsed_red_light = 0
                self.traffic[0:1].status = "Green"

            elif(self.traffic[2].elapsed_red_light == 8):
                self.traffic[2:3].elapsed_red_light = 0
                self.traffic[2:3].status = "Green"

            elif(self.traffic[0].elapsed_green_light == 6):
                self.traffic[0:1].elapsed_green_light = 0
                self.traffic[0:1].status = "Red"

            elif(self.traffic[2].elapsed_green_light == 6):
                self.traffic[2:3].elapsed_green_light = 0
                self.traffic[2:3].status = "Red"

            self.traffic[0:1].red_light_timer += 1
