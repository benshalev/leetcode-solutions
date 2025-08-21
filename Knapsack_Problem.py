# Given n items where each item has some weight and profit associated with it and also given a bag with capacity W
# [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits
# associated with them is the maximum possible.

#Note: The constraint here is we can either put an item completely into the bag or cannot put it at all
# [It is not possible to put a part of an item into the bag].

class Solution:
    def knapsack(self, vals , weight, limits):
        table = [[0 for weight in range(limit + 1)]]



    v = [10, 40, 30, 50]
    w = [1, 4, 8, 3, 2]
    l = 10
    assert knapsack(v,w,l)

