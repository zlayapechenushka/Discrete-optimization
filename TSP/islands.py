import numpy as np


def reading_txt(path):
    data = open(path, 'r')
    lines = data.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i][:-1]

    n, p, k, M = map(int, lines[0].split())

    islands = [np.array([386, 780, 0, 1])]
    for i in range(2, len(lines)):
        islands.append(list(map(int, lines[i].split()))+[i])

    for i in range(len(islands)):
        islands[i] = np.array(islands[i])
    islands = np.array(islands)
