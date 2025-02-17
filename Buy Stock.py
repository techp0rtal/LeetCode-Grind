

"""
Thoughts:
1. you have to buy first. then sell. can't be on the same day. and can't be on a day before you buy
2. want to find the biggest negative we can if we do buy - sell (if u want to convert back to pos)


"""

# I'll start with the noob way and brute force it.
# My first attempt.
def maxProfit( prices: list[int]) -> int:
    profit_list = []
    final_profit = 0

    for buy in prices:
        for sell in prices:
            profit = sell - buy
            profit_list.append(profit)
    final_profit = max(profit_list)

    if final_profit <= 0:
        return 0
    else:
        return final_profit
print(maxProfit([7,1,5,3,6,4]))

# That was wrong though bc I counted days before the buy date. So it didn't make sense. Also I got a profit of 6 when I paid 7 and sold for one....
# here is the sliding window approach:
def maxProfit(prices):
    left = 0  # Buy pointer
    max_profit = 0  # Track max profit

    for right in range(1, len(prices)):  # Sell pointer
        if prices[right] < prices[left]:
            # Found a new lower price to buy
            left = right
        else:
            # Check if selling at current day gives better profit
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

    return max_profit










