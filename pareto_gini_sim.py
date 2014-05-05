__author__ = 'hok1'

from ginicoef import gini_coef
import wealthdist as wsample
from multiprocessing import Pool
import numpy as np
import csv
from itertools import product

sum_wealth = 1e+12

populations = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
alphas = np.linspace(0.1, 3, num=61)

def cal_gini((population, alpha)):
    return gini_coef(wsample.sample_pareto_wealth(sum_wealth=sum_wealth, size=population, alpha=alpha))

if __name__ == '__main__':
    outf = open('ginicoef.csv', 'wb')
    writer = csv.writer(outf)
    headers = ['population', 'alpha', 'gini_coef']
    writer.writerow(headers)

    pairs = product(populations, alphas)
    for pair in pairs:
        p = Pool(processes=10)
        rep_pairs = [pair]*100
        results = p.map(cal_gini, rep_pairs)
        for ginival in results:
            writer.writerow([pair[0], pair[1], ginival])

    outf.close()