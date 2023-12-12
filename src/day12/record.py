import re

class Record:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, id, springs, pattern):
        self.id      = id
        self.springs = springs
        self.pattern = pattern


    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def possible_arrangements(self):
        perms = {}
        perms[(0, 0)] = 1
        for s in self.springs:
            new_perms = {}
            if s in ["#", "?"]:
                for p, count in perms.items():
                    mi = p[0]
                    sl = p[1] + 1
                    if p[0] < len(self.pattern):
                        if p[1] < self.pattern[p[0]]:
                            k = (p[0], p[1] + 1)
                            if k not in new_perms:
                                new_perms[k] = 0
                            new_perms[k] = new_perms[k] + count
            if s in [".", "?"]:
                for p, count in perms.items():
                    if p[1] == 0:
                        k = p
                        if k not in new_perms:
                            new_perms[k] = 0
                        new_perms[k] = new_perms[k] + count
                    else:
                        if p[0] < len(self.pattern):
                            if self.pattern[p[0]] == p[1]:
                                k = (p[0] + 1, 0)
                                if k not in new_perms:
                                    new_perms[k] = 0
                                new_perms[k] = new_perms[k] + count
            perms = new_perms

        total = 0
        for p, count in perms.items():
            match_idx  = p[0]
            spring_len = p[1]
            t1 = match_idx == len(self.pattern) - 1 and spring_len == self.pattern[match_idx]
            t2 = match_idx == len(self.pattern)     and spring_len == 0
            if t1 or t2:
                total += count
        return total


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    # def __match_pattern(self):
    #     space_pattern  = "(\.+)"
    #     spring_pattern = "(#{N})"
    #     match_pattern  = [spring_pattern.replace("N", p) for p in self.pattern]
    #     match_pattern  = space_pattern.join(match_pattern)
    #     match_pattern  = "\A" + space_pattern + match_pattern + space_pattern + "\Z"
    #     return match_pattern

    # def __spring_permutations(self):
    #     perms = ["."]
    #     for s in self.springs:
    #         new_perms = []
    #         match s:
    #             case "?":
    #                 new_chars = ["#", "."]
    #             case _:
    #                 new_chars = [s]
    #         for p in perms:
    #             for nc in new_chars:
    #                 new_perms.append(p + nc)
    #         perms = new_perms
    #     perms = [p + "." for p in perms]
    #     return perms