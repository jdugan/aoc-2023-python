from src.day21.point import Point

class Garden:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, points):
        self.points = points


    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def reachable_points(self, steps):
        points = set([self.__origin().id])
        for step in range(1, steps+1):
            new_points = set()
            for pid in points:
                point = self.points[pid]
                aids  = [aid for aid in point.adjacent_ids() if aid in self.points]
                for aid in aids:
                    new_points.add(aid)
            points = new_points
        return len(points)

    def extremely_reachable_points(self, steps):
        remainder = steps % 2
        dx, dy    = self.__dimensions()
        oy, ox    = self.__origin().id
        memory    = { (oy, ox): 0 }
        points    = set([self.__origin().id])
        for step in range(1, steps+1):
            new_points = set()
            for (py, px) in points:
                point = Point(px, py, ".")
                for (ay, ax) in point.adjacent_ids():
                    if (ay, ax) not in memory:
                        aoid = self.__find_offset(ax, ay, dx, dy)
                        if aoid in self.points:
                            memory[(ay, ax)] = step
                            new_points.add((ay, ax))
                        else:
                            memory[(ay, ax)] = -1
            points = new_points
            if step % 1000 == 0:
                print(step, len(points))
        keys = [k for k, v in memory.items() if v % 2 == remainder]
        # print(keys)
        return len(keys)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __dimensions(self):
        x_size = max([p.x for p in self.points.values()]) + 1
        y_size = max([p.y for p in self.points.values()]) + 1
        return (x_size, y_size)

    def __find_offset(self, x0, y0, dx, dy):
        x1, y1 = (x0, y0)
        while x1 < 0 or x1 >= dx:
            if x1 < 0:
                x1 += dx
            else:
                x1 -= dx
        while y1 < 0 or y1 >= dy:
            if y1 < 0:
                y1 += dy
            else:
                y1 -= dy
        return (y1, x1)

    def __origin(self):
        points = [p for p in self.points.values() if p.value == "S"]
        return points[0]