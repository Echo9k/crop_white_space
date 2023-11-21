from multiprocessing import Pool


def execute_in_parallel(function, data, num_processes=None):
    with Pool(processes=num_processes) as pool:
        results = pool.map(function, data)
    return results