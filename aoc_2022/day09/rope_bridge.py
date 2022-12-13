'''
Day 9: Rope Bridge

Austin Equitz
austin.equitz@gmail.com
'''
import itertools

import matplotlib.pyplot as plt
import numpy as np

GRID_ON = False

class RopeKnot():

    perimeter_offsets = [x for x in list(itertools.product([-1, 0, 1], repeat=2))]

    def __init__(self, name: str, init_coords: list[int]) -> None:
        self.name = name
        self.curr_coords = init_coords
        self.x_coord = init_coords[0]
        self.y_coord = init_coords[1]
        self.last_coords = init_coords
        self.coords_visited = []
        self.__saveCoordsVisited(init_coords)

    def __saveLastCoords(self, coords: list[int]):
        self.last_coords = coords

    def __saveCoordsVisited(self, coords: list[int]):
        self.coords_visited.append(coords)

    def setCoords(self, new_coords: list[int]):
        self.__saveLastCoords(self.curr_coords)
        self.curr_coords = new_coords
        self.__saveCoordsVisited(new_coords)

    def setXCoord(self, x_coord: int):
        self.__saveLastCoords(self.curr_coords)
        self.x_coord = x_coord
        self.curr_coords = [x_coord, self.y_coord]
        self.__saveCoordsVisited(self.curr_coords)

    def setYCoord(self, y_coord: int):
        self.__saveLastCoords(self.curr_coords)
        self.y_coord = y_coord
        self.curr_coords = [self.x_coord, y_coord]
        self.__saveCoordsVisited(self.curr_coords)

    def getUniqueCoordsVisited(self):
        return set(tuple(coords) for coords in self.coords_visited)

    def perimeterCoords(self) -> list[list[int, int]]:
        perimeter_coords = [
            [x + self.x_coord, y + self.y_coord] for x,y in RopeKnot.perimeter_offsets
        ]

        return perimeter_coords


class Grid():
    def __init__(self, plot_pause: int) -> None:
        self.plot_pause = plot_pause
        plt.ion()

    def updateGrid(self, points: list[list[int]], names: list[str]):
        plt.clf()
        points = np.array(points)
        x, y = points.T

        plt.plot(*zip(*points), marker='o', color='r', ls='')
        plt.xlim([-50, 50])
        plt.ylim([-50, 50])

        for idx, name in enumerate(names):
            plt.annotate(name, (x[idx], y[idx]))

        plt.draw()
        plt.pause(self.plot_pause)

if __name__ == '__main__':
    with open('rope_motions.txt', 'r') as fin: rope_input = fin.read().splitlines()

    rope_motions = [[line.split()[0], int(line.split()[1])] for line in rope_input]

    high_knot = RopeKnot('H', [0, 0])
    low_knot = RopeKnot('L', [0, 0])

    if GRID_ON:
        names = [high_knot.name, low_knot.name]
        coords = [high_knot.curr_coords, low_knot.curr_coords]
        grid = Grid(plot_pause=0.00001)
        grid.updateGrid(coords, names)

    for idx, [direction, num_moves] in enumerate(rope_motions):
        for move in range(num_moves):

            if direction == 'U':
                high_knot.setYCoord(high_knot.y_coord + 1)

            elif direction == 'D':
                high_knot.setYCoord(high_knot.y_coord - 1)

            elif direction == 'L':
                high_knot.setXCoord(high_knot.x_coord - 1)

            elif direction == 'R':
                high_knot.setXCoord(high_knot.x_coord + 1)

            high_perimeter_coords = high_knot.perimeterCoords()
            if low_knot.curr_coords not in high_perimeter_coords:
                low_knot.setCoords(high_knot.last_coords)

            if GRID_ON:
                coords = [high_knot.curr_coords, low_knot.curr_coords]
                grid.updateGrid(coords, names)

    unique_coords_last_knot = len(low_knot.getUniqueCoordsVisited())
    print(f'Unique coordinates visited: {unique_coords_last_knot}')
