from src.day21.garden import Garden
from src.day21.point import Point
from src.utility.reader import Reader

class Day21:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 21

    def puzzle1(self):
        garden = self.__garden()
        return garden.reachable_points(64)

    def puzzle2(self):
        garden = self.__garden()
        return garden.extremely_reachable_points(500)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __data(_):
        return Reader().to_lines("data/day21/input.txt")

    def __garden(self):
        points = {}
        for y, row in enumerate(self.__data()):
            for x, col in enumerate(row):
                if col != "#":
                    points[(y, x)] = Point(x, y, col)
        return Garden(points)