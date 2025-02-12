prices = [120,200,300,50,240]

def filter_prices(prices):
    return [value for value in prices if value >= 200]

def total_sales(prices):
    print(f"Your total sales are : {sum(prices)}")
    
def average_sales(prices):
    print(f"Average sale is: {sum(prices) / len(prices):.2f}")
    

filter = filter_prices(prices)
print(filter)
total_sales(prices)
average_sales(prices)