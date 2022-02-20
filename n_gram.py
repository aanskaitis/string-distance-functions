import math


def calc_n_gram_distance(s1: str, s2: str, n: int) -> float:
    """Returns the distance between two strings using
    n-gram (sometimes called Q-gram) sets.

    Distance defined as: d(s1, s2) = sqrt(sum([x1 to xn] abs(cnt(x, s1) - cnt(x, s2))))
    Where cnt(x, s) is the number of occurrences of n-gram x in s
    and [x1 to xn] is the union of n-gram set for s1 and n-gram set for s2.

    Args:
        s1 (str): first string
        s2 (str): second string
        n (int): size of n-gram

    Returns:
        float: distance between two strings
    """

    if type(s1) != str or type(s2) != str or type(n) != int:
        raise TypeError("""Functions arguments can only be of type 
            str (args: s1, s2), int (args: n).""")

    if n > len(s1) or n > len(s2) or n < 1:
        raise ValueError("""Argument n value has to be in range:
        0 < n <= min(len(s1), len(s2)).""")

    s1_n_gram_set = set()
    s2_n_gram_set = set()

    for i in range(len(s1) - n + 1):
        s1_n_gram_set.add(s1[i:i + n])

    for j in range(len(s2) - n + 1):
        s2_n_gram_set.add(s2[j:j + n])

    s1_n_diff_s2 = len(s1_n_gram_set.difference(s2_n_gram_set))
    s2_n_diff_s1 = len(s2_n_gram_set.difference(s1_n_gram_set))

    return math.sqrt(s1_n_diff_s2 + s2_n_diff_s1)