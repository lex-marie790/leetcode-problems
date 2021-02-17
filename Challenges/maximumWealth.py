"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100"""


"""
Understand: 

accounts = [[1,2,3],[3,2,1,1]]
Output: 6

accounts = [[1,2,3],[3,2,100]]
Output: 105

accounts = [[1,2,3],[3,2,1]]
Output: 6

accounts = [[1,2,3]
Output: 6


Plan
Keep track of highest wealth seen
Go through accounts using two for loops.
Sum up all wealth current customer has
If sum of weather is greater than what we've seen, update highest wealth seen
Return highest wealth seen

"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for cust in accounts:
            currentWealth = 0
            for bankAccount in cust:
                currentWealth += bankAccount
            if currentWealth > wealth:
                wealth = currentWealth
        return wealth

        # slightly different method
        # wealth = 0
        # for cust in accounts:
        #     currentWealth = sum(cust)
        #     if currentWealth > wealth:
        #         wealth = currentWealth
        # return wealth