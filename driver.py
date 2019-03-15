from solution import Solution
import matplotlib.pyplot as plt
import sys


def tabu_search(max_iter, tabu_tenure, neighbor_size=1000, init='No'):

    tabu = dict()
    sol = Solution()
    if init == 'NN':
        sol.nearest_neighborhood_initialization()
    for i in range(sol.number_of_nodes):
        for j in range(sol.number_of_nodes):
            tabu[(i,  j)] = 0

    obj = []
    count = 0

    best_obj = sys.float_info.max
    while count <= max_iter:

        pair = sol.best_neighbor_w_tabu_aspiration(neighbor_size, tabu, best_obj)
        tabu[pair] += tabu_tenure
        for i in range(sol.number_of_nodes):
            for j in range(sol.number_of_nodes):
                if tabu[(i, j)] > 0:
                    tabu[(i, j)] -= 1
        sol.swap_operation(pair[0], pair[1])
        obj.append(sol.get_obj_func_value())
        count += 1

        if sol.get_obj_func_value() < best_obj:
            best_obj = sol.get_obj_func_value()

    print('incumbent value: ', str(best_obj))
    plt.plot(list(range(len(obj))), obj)
    plt.xlabel('Iteration No')
    plt.ylabel('Objective Function Value')
    plt.title('Tabu Search')
    plt.show()


if __name__ == '__main__':

    import time
    s = time.time()
    tabu_search(1000, 100, init='NN')
    e = time.time()
    print('cpu time: ', str(e-s))
