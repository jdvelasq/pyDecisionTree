"""
Spyder Graph

"""

import matplotlib.pyplot as plt
from operator import itemgetter

from numpy import exp


def spyder_graph(sensitivities: dict):

    for key in sensitivities.keys():
        values = sensitivities[key].branch_values_
        base_value = sensitivities[key]._base_value
        values = [100 * (value - base_value) / base_value for value in values]
        expected_values = sensitivities[key].expected_values_
        plt.gca().plot(values, expected_values, label=key)

    plt.gca().spines["bottom"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().set_ylabel("Expected values")
    plt.gca().set_xlabel("Change in input (%)")
    plt.gca().legend()

    plt.grid()