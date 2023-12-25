from src.day24.particle import Particle
from src.day24.storm import Storm
from src.utility.reader import Reader

class Day24:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 24

    def puzzle1(self):
        storm = self.__storm()
        return storm.sample_size(200000000000000, 400000000000000)

    def puzzle2(self):
        return -2


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __data(_):
        return Reader().to_lines("data/day24/input.txt")

    def __storm(self):
        particles = {}
        for id, line in enumerate(self.__data()):
            coords, deltas = line.split(" @ ")
            x, y, z        = coords.split(", ")
            dx, dy, dz     = deltas.split(", ")
            particle       = Particle(id, int(x), int(y), int(z), int(dx), int(dy), int(dz))
            particles[id]  = particle
        return Storm(particles)