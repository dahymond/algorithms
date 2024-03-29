#Problem
#You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to make this as efficient as possible.

#For example, if you were given the list of stock prices:

#prices = [12,11,15,3,10]

#Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).


def profit(stock_prices):
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with a profit of zero
    max_profit = 0
    
    for price in stock_prices:
        
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
        # Check the current price against our minimum for a profit 
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        
        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)
        
    return max_profit  


print profit([23,12,3,10,25])

#Currently we're finding the max profit in one pass O(n) and in constant space O(1)

def profit2(stock_prices):
    
    # Check length
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with an initial max profit
    max_profit = stock_prices[1] - stock_prices[0]
    
    # Skip first index of 0
    for price in stock_prices[1:]:
        
        
        # NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING
        
        # Check the current price against our minimum for a profit 
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        
        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)
        
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
        
        
        
        
    return max_profit

print profit2([23,12,3,10,25])