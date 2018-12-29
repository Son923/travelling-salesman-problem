
class Node:
    def __init__(self, city_info):
        self.__name = city_info[0]
        self.__node_position = (city_info[1], city_info[2])

    def get_pos(self):
        return self.__node_position

    def get_name(self):
        return self.__name
