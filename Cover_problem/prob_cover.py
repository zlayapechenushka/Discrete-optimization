import numpy as np
from scipy.optimize import linprog


if __name__ == '__main__':
    n_columns, n_rows = map(int, input().split())
    weights = []
    inc_matrix = np.zeros((n_rows, n_columns))
    for i in range(n_rows):
        inp = list(map(int, input().split()))
        weights += [inp[0]]
        for inc in inp[1:]:
            inc_matrix[i][inc-1] = 1
    # Arrays for scipy.optimize linpog
    b_ub = [-1 for i in range(n_columns)]
    A_ub = -inc_matrix.transpose()
    bounds = [(0, 1) for i in range(n_rows)]
    # Find opt
    opt = linprog(c=weights, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    # Sorting for algorithm
    x = sorted([(x, i) for i, x in enumerate(opt.x)], key=lambda x: -x[0])
    answer = np.zeros((n_rows, 1))
    for v, i in x:
        answer[i] = 1
        if (A_ub@answer <= -1).all():
            break
    print(*[i+1 for i, x in enumerate(answer) if x])
