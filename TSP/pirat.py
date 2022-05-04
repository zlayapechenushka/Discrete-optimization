import numpy as np


def road_cost(island_1, island_2, p):
    distance = np.sqrt(np.sum((island_1[:2] - island_2[:2])**2))
    return distance*p


def road_profit(island_1, island_2, p):
    cost = road_cost(island_1, island_2, p)
    return island_2[2] - cost


class Pirat:
    p, k, M = p, k, M

    def __init__(self, name):
        self.current_island = np.array([386, 780, 0])
        self.path = [1]
        self.travelling = True

    def travel(self, islands):
        global traveled
        islands_to_travel = sorted(islands, key=lambda x: -road_profit(self.current_island, np.array(x), self.p))
        for island in islands_to_travel:
            if self.can_travell(islands, island):
                self.path.append(island[3])
                self.current_island = np.array(island[:3])
                traveled.append(island[3])
                break
        else:
            self.travelling = False

    def can_travell(self, islands, island):
        global traveled
        last_k_islands = self.path[-k + 1:]
        for i in range(len(last_k_islands)):
            last_k_islands[i] -= 1
        last_k_stolen = np.sum(islands[last_k_islands], axis=0)[2]
        return last_k_stolen + island[2] <= M and road_profit(self.current_island, island, p) >= 0 and island[3] not in traveled