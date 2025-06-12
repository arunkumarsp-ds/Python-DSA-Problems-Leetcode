
"""
Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7. """


"""
!) We are told that we can buy and sell multiple times, but we can buy the next time only after selling the stock we already bought.

2) So this becomes very easy — always try to draw the line chart of prices for better understanding.

3) By looking at the chart:

   * If the next day's price is greater than the current day, then sell it — so we can make the profit.

4) Since we are allowed to buy and sell multiple times, we just keep adding the profits by buying and selling whenever the next day's price is greater than the current day.
  This way, we will get the maximum profit possible.

5) Run the loop from the first to the (n-1)th index, so that we can compare like:
prices[i+1] > prices[i] """

def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

""" Time:O(N)
    Space:O(1) """




