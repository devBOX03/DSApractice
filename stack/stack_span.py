def clalculateStockSpan(stock_price:list) -> list:
    # brute force
    print(bruteForce(stock_price))
    # leverage space
    print(leverageSpace(stock_price))

    # optimize soln
    pass

def bruteForce(stock_price:list) -> list:
    pass
def leverageSpace(stock_price:list) -> list:
    stock_span = [0] * len(stock_price)
    max_stock_index_stack: list = []
    top = -1

    for index, price in enumerate(stock_price):
        # edge case for first element
        if len(max_stock_index_stack) == 0:
            max_stock_index_stack.append(index)
            stock_span[index] = 1
            continue
        # get previous max element
        while stock_price[max_stock_index_stack[-1]] <= price:
            max_stock_index_stack.pop()
        # get current day stock span
        stock_span[index] = index - max_stock_index_stack[top]
        max_stock_index_stack.append(index)

    return stock_span

if __name__ == '__main__':
    stock_prices = [100, 80, 60, 70, 60, 75, 85]
    clalculateStockSpan(stock_prices)