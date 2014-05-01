__author__ = 'hok1'

import numpy as np

default_sum_wealth = 100.0

def normalize_wealth(sum_wealth, nums):
    return nums * sum_wealth / np.sum(nums)

def sample_absuniform_wealth(sum_wealth=default_sum_wealth, size=100):
    nums = np.repeat(1, size)
    return normalize_wealth(sum_wealth, nums)

def sample_communist_wealth(sum_wealth=default_sum_wealth, size=100, mean=10, sigma=0.1):
    nums = np.random.normal(loc=mean, scale=sigma, size=size)
    return normalize_wealth(sum_wealth, nums)

def sample_poisson_wealth(sum_wealth=default_sum_wealth, size=100, lam=1.0):
    nums = np.random.poisson(lam=lam, size=size)
    return normalize_wealth(sum_wealth, nums)

def sample_pareto_wealth(sum_wealth=default_sum_wealth, size=100, xm=1, alpha=1.161):
    uninums = np.random.uniform(size=size)
    nums = np.power(1-uninums, -1./alpha) / xm
    return normalize_wealth(sum_wealth, nums)