from itertools import combinations

class Storm:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, particles):
        self.particles = particles


    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def sample_size(self, lower, upper):
        count  = 0
        combos = combinations(self.particles.values(), 2)
        for p1, p2 in combos:
            (x, y), t1, t2 = p1.xy_intersection(p2)
            if x:
                if (x >= lower and x <= upper) and (y >= lower and y <= upper) and t1 > 0 and t2 > 0:
                    count += 1
        return count