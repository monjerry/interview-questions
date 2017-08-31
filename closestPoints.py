import copy
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'X: {}, Y: {}'.format(self.x, self.y)

class Node:

    def __init__(self, key, point):
        self.key = key
        self.point = point
        self.points = [point]
        self.right = None
        self.left = None
    
    def __str__(self):
        string = ''
        for p in self.points:
            string += ' ' + p.__str__()
        return '|Key: {}, Points {}|'.format(self.key, string)

class Map:
    def __init__(self):
        self.arrayOfPoints = []
        self.tree = None
    
    def addSetOfPoints(self, points):
        for point in points:
            self.addNode(point)

    def printAll(self):
        toVisit = [self.tree]
        while len(toVisit) > 0:
            tmp = []
            string = ''
            for visiting in toVisit:
                string += ' ' + visiting.__str__()
                if visiting.left is not None:
                    tmp.append(visiting.left)
                if visiting.right is not None:
                    tmp.append(visiting.right)
            print string
            toVisit = tmp

    def addNode(self, point):
        self.arrayOfPoints.append(point)
        if self.tree is None:
            node = Node('x', point)
            self.tree = node
        else:
            node = self.tree
            while True:
                if node.key == 'x':
                    if point.x < node.point.x:
                        if node.left is None:
                            node.left = Node('y', point)
                            return
                        else:
                            node = node.left
                    elif node.point.x == point.x:
                        node.points.append(point)
                        return
                    elif point.x > node.point.x:
                        if node.right is None:
                            node.right = Node('y', point)
                            return
                        else:
                            node = node.right
                else:
                    if point.y < node.point.y:
                        if node.left is None:
                            node.left = Node('x', point)
                            return
                        else:
                            node = node.left
                    elif node.point.y == point.y:
                        node.points.append(point)
                        return
                    elif point.y > node.point.y:
                        if node.right is None:
                            node.right = Node('x', point)
                            return
                        else:
                            node = node.right

mapa = Map()
mapa.addSetOfPoints([Point(7, 2), Point(5, 4), Point(9, 6), Point(2, 3), Point(4, 7), Point(8, 1), Point(2, 4)])
mapa.printAll()
