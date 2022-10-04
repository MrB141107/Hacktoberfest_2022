'''
Python implementation for the Nearest Neighbours Heuristic for the Travelling Salesman Problem, visualized using Python Turtle.
Author: D1Dayer99
'''

import turtle
import random
import math

t = turtle.Turtle()
# turtle.tracer(100)
t.speed(100)

'''
Algorithm Description:
Greedy algorithm
1 . Randomly select point as the root.
2. Find the point that is closest to the current position but is not yet part of the route, and add it into the route.
3. Repeat until the route includes each vertex.
'''


class TSP_NN:

    def __init__(self):
        self.points = self.gen_points()
        self.destinations = self.get_destinations()
        self.connect_points()

    def gen_points(self):
        '''
        Generating n (50) cooredinates within the specified range, the range is set to -300 < x < 300
        Visualizing each point using Python Turtle
        '''
        self.pts = [((random.randint(-300, 300)), random.randint(-300, 300))
                    for i in range(50)]
        for coords in self.pts:
            t.penup()
            t.goto(coords[0], coords[1])
            t.pendown()
            t.dot(10)
            t.write(coords)
        print(self.pts)
        t.penup()

    def get_destinations(self) -> list:
        '''
        Starting with one point, the distance between every points are culculated using Pythagoreas' Theorem and is compared to previous values.
        The nearest point is then added to the list of destinations
        '''
        self.start_point = self.pts[0]
        destinations = []
        min_distance = 123467897383
        current_point = self.start_point
        self.pts.remove(current_point)
        while len(self.pts) != 0:
            for coords in self.pts:
                a = coords[0] - current_point[0]
                b = coords[1] - current_point[1]
                c = math.sqrt((a**2)+(b**2))
                if c < min_distance:
                    min_distance = c
                    x_coord, y_coord = coords
            destinations.append((x_coord, y_coord))
            current_point = (x_coord, y_coord)
            min_distance = 34567898765
            self.pts.remove(current_point)

        return destinations

    def connect_points(self):
        '''
        For every destination, draw a line to it. Once all popints are visited, return back to the starting point
        '''
        t.penup()
        t.goto(self.start_point)
        for i in range(len(self.destinations)):
            t.pendown()
            t.goto(self.destinations[i][0], self.destinations[i][1])
        t.goto(self.start_point)


tsp1 = TSP_NN()
turtle.done()
