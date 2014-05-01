__author__ = 'kwan-yuetho'

import numpy as np

class GiniCoefficientCalculator:
    def lorentz_curve(self, wealths):
        curve_points = []
        sum_wealths = sum(wealths)
        population = len(wealths)

        cum_wealth = 0.0
        cum_pop = 0
        for wealth in sorted(wealths):
            cum_wealth += wealth
            cum_pop += 1
            curve_points.append((float(cum_pop)/population, cum_wealth/sum_wealths))

        return curve_points

    def area_under_curve(self, curve_points):
        xarray = np.array(map(lambda point: point[0], curve_points))
        yarray = np.array(map(lambda point: point[1], curve_points))
        return np.trapz(yarray, x=xarray)

    def gini_coef(self, wealths):
        curve_points = self.lorentz_curve(wealths)
        B = self.area_under_curve(curve_points)
        A = 0.5 - B
        return A / (A+B)