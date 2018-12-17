
class Node:
    def __init__(self, city_info):
        self.node_name = city_info[0]
        self.node_position = (city_info[1], city_info[2])
    
    def get_position(self):
        return self.node_position
    