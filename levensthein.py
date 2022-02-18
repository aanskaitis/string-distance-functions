import numpy as np


def calc_levenshtein_distance(s1: str, s2: str) -> int:
    """Returns the Levenshtein distance between two strings using
    Wagner-Fischer algorithm.

    Distance defined as: minimum cost of converting one string to another
    using insertions, deletions and subtitutions.

    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: Levenshtein distance between two strings
    """

    if type(s1) != str or type(s2) != str:
        raise TypeError("Function arguments can only be of type str.")

    distance_matrix = np.zeros((len(s1) + 1, len(s2) + 1))

    for i in range(1, len(s1) + 1):
        distance_matrix[i, 0] = i

    for j in range(1, len(s2) + 1):
        distance_matrix[0, j] = j

    for j in range(1, len(s2) + 1):
        for i in range(1, len(s1) + 1):

            if s1[i - 1] == s2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            distance_matrix[i, j] = min(distance_matrix[i - 1, j] + 1,
                                        distance_matrix[i, j - 1] + 1,
                                        distance_matrix[i - 1, j - 1] + substitution_cost)

    return int(distance_matrix[len(s1), len(s2)])