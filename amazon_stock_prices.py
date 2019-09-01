def profit(stock_prices):
    min_stock_price = stock_prices[0]

    max_profit = 0

    for price in stock_prices:

        min_stock_price = min(min_stock_price, price)

        comparison_profit = price - min_stock_price  

        max_profit = max(max_profit, comparison_profit)

    return max_profit    


print profit([23,12,3,10,25])


