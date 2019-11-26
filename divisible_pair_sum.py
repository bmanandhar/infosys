#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:04:30 2019

@author: bijayamanandhar
"""
"""Question number 1

Given an array of n elements and a number m, 
we need to find all distinct pairs existing 
in the array whose pair sum is divisible by 
the given number m and then print the total 
number of such pairs. Distinct pairs means 
(1, 2) and (2, 1) are the same."""


class Solution:
    
    def divisible_pair_sum(self, n, m):
        
        result = []
        for i in range(len(n) - 1):
            if n[i] not in result:
                first = n[i]
                list_for_second = n[i+1:]
                for j in range(len(list_for_second)):
                    second = list_for_second[j]
                    if second not in result:
                        if (first + second) % m == 0:
                            result.append(first)
                            result.append(second)
        return len(result)//2
    
if __name__ == '__main__':
    
    n = [4, 0, 1, 5, 2, 6, 7, 9]
    m = 4
    S = Solution()
    print(S.divisible_pair_sum(n, m) == 3) # [[4, 0], [1, 7], [2, 6]] 

    
    