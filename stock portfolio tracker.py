# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks")

for stock, price in stock_prices.items():
    print(stock, ": $", price)

stock = input("\nEnter Stock Name: ").upper()

if stock in stock_prices:
    quantity = int(input("Enter Quantity: "))

    total = stock_prices[stock] * quantity

    print("\nTotal Investment Value = $", total)

    file = open("investment.txt", "w")
    file.write("Stock: " + stock + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: $" + str(total))
    file.close()

    print("Result saved successfully in investment.txt")

else:
    print("Invalid Stock Name")