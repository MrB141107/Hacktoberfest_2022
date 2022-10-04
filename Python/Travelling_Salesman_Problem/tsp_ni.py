'''
Python implementation for the Nearest  Heuristic for the Travelling Salesman Problem, visualized using Python Turtle.
Author: D1Dayer99
'''

import turtle
import random
import math
import time

'''
Algorithm Description:
1. Choose random two point as the starting point
2. Finds the closest point closest to the path that is not already in the path
3. Insert the point between whichever two points that would cause the resulting path to be the shortest possible.
4. Repeat until no more insertions remain
'''


class TSP_NI:

    def __init__(self):

        self.t = turtle.Turtle()
        self.p = turtle.Turtle()
        turtle.tracer(10)
        # self.t.speed(50)
        # self.p.speed(50)
        self.contained_vertices = []
        self.pts = self.gen_points()
        self.distances = self.get_all_distances()
        self.cycle = self.get_cycle()

    def gen_points(self) -> list:
        '''
        Generating n (100) cooredinates within the specified range, the range is set to -300 < x < 300
        Visualizing each point using Python Turtle
        '''
        points = [((random.randint(-300, 300)), random.randint(-300, 300))
                  for i in range(100)]
        for coord in points:
            self.p.penup()
            self.p.goto(coord)
            self.p.pendown()
            self.p.dot(10)
            self.p.write(coord)
        self.p.penup()
        self.p.hideturtle()
        return points

    def get_all_distances(self) -> list:
        '''
        For every point, calculate the distnace between each point using Pythagoras' Theorem and append to distances list
        The list is then sorted
        '''
        distances = []
        current_point = self.pts[0]
        pts = self.pts[::]
        pts.remove(current_point)
        while pts:
            for coords in pts:
                distance = self.calc_distance(coords, current_point)
                distances.append((distance, (current_point), (coords)))
            current_point = pts[0]
            pts.remove(current_point)
        distances.sort()
        return distances

    def calc_distance(self, coord1, coord2) -> float:
        '''
        Pythagoras Theorem
        a^2 + b^2 = c^2
        '''
        a = coord1[0] - coord2[0]
        b = coord1[1] - coord2[1]
        return math.sqrt((a**2)+(b**2))

    def get_insertion_metric(self, node, coord_A, coord_B) -> float:
        '''
        Insertion metric used for determining where to insert the point
        '''
        metric = self.calc_distance(node, coord_A)
        + self.calc_distance(node, coord_B)
        - self.calc_distance(coord_A, coord_B)
        return metric

    def get_next_node(self, cycle):
        for coords in self.distances:
            if coords[1] in cycle:
                next_node = coords[2]
                break
            elif coords[2] in cycle:
                next_node = coords[1]
                break
        self.distances.remove(coords)
        return next_node

    def get_cycle(self) -> list:
        '''
        While all the points are NOT included in the path, get the closest node to the path
        '''
        cycle = []
        idx = 0
        cycle.append(self.distances[0][1])
        cycle.append(self.distances[0][2])
        self.contained_vertices.append(self.distances[0][1])
        self.contained_vertices.append(self.distances[0][2])
        self.distances.remove(self.distances[0])
        flag = True
        while flag:
            if all(i in self.contained_vertices for i in self.pts) == False:
                next_node = self.get_next_node(cycle)
                self.contained_vertices.append(next_node)
                min_metric = 123456787654323456787432
                for i in range(len(cycle)-1):
                    metric = self.get_insertion_metric(
                        next_node, cycle[i], cycle[i+1])
                    if metric < min_metric:
                        idx = i
                        min_metric = metric
                cycle.insert(idx+1, next_node)
                self.t.clear()
                self.connect_points(cycle, next_node)
            else:
                flag = False
                # print(cycle)
                return cycle

    def connect_points(self, cycle, next_node):
        '''
        Visualize the path using turtle
        '''
        turtle.tracer(len(cycle))
        self.t.penup()
        self.t.goto(cycle[0])
        for coords in cycle:
            if coords == next_node:
                self.t.color("red")
            else:
                self.t.color("black")
            self.t.pendown()
            self.t.goto(coords)
        self.t.pendown()
        self.t.goto(cycle[0])
        time.sleep(1/24)


tsp1 = TSP_NI()
turtle.done()
