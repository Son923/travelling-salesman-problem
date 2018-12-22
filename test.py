def abc(self,index,FirstDistance):
    SecondDistance = []
    for x in range(0,len(FirstDistance)):
        if x == index:
            SecondDistance.append(FirstDistance[index])
        else:
            SecondDistance.append(FirstDistance[index] + self.distance(self.nodes[index],self.nodes[x]))
        IndexMin = list(sorted(SecondDistance))[1]
        return (index,SecondDistance.index(IndexMin),IndexMin)


def Heuristic(self):
    start = self.nodes[0]
    path = [start]
    display_path = []
    self.nodes.remove(start)
    while self.nodes:
        FirstDistance = [self.distance(path[-1],node) for node in self.nodes]
        ListMin = {}
        if len(FirstDistance) == 1:
            path.append(nodes[0])
            self.nodes.remove(nodes[0])
        else:
            for x in range(0,len(self.nodes)):
                something = self.abc(x,FirstDistance)
                ListMin[(something[0],something[1])] = something[2]
            Minst319 = min(d, key=d.get)
            path.append(Minst319[0])
            path.append(Minst319[1])
            self.nodes.remove(Minst319[0])
            self.nodes.remove(Minst319[1])
    for node in path:
        display_path.append(node.name)
    return (path, display_path)
               