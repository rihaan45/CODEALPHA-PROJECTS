import json
import yfinance as yf

def load_portfolio():
    try:
        with open("portfolio_data.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_portfolio(portfolio):
    with open("portfolio_data.json", "w") as file:
        json.dump(portfolio, file)

def get_stock_price(symbol):
    try:
        stock_data = yf.Ticker(symbol).history(period="1d")
        return round(stock_data["Close"].iloc[-1], 2)
    except:
        return None

def add_stock(portfolio):
    symbol = input("Enter stock symbol (e.g. AAPL): ").upper()
    shares = int(input("Number of shares: "))
    purchase_price = float(input("Purchase price per share: $"))
    
    portfolio.append({
        "symbol": symbol,
        "shares": shares,
        "purchase_price": purchase_price
    })
    save_portfolio(portfolio)
    print(f"\n{symbol} added successfully!")

def remove_stock(portfolio):
    symbol = input("Enter stock symbol to remove: ").upper()
    updated_portfolio = [s for s in portfolio if s["symbol"] != symbol]
    save_portfolio(updated_portfolio)
    print(f"\n{symbol} removed successfully!")
    return updated_portfolio

def view_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty!")
        return
    
    print("\n{:<6} {:<8} {:<12} {:<12} {:<12}".format(
        "SYMBOL", "SHARES", "COST", "CURRENT", "PROFIT/LOSS"))
    print("-" * 50)
    
    total_invested = 0
    total_current = 0
    
    for stock in portfolio:
        current_price = get_stock_price(stock["symbol"])
        if current_price is None:
            print(f"{stock['symbol']}: Price data unavailable")
            continue
            
        cost = stock["shares"] * stock["purchase_price"]
        current_value = stock["shares"] * current_price
        profit_loss = current_value - cost
        
        print("{:<6} {:<8} ${:<11.2f} ${:<11.2f} ${:<11.2f}".format(
            stock["symbol"],
            stock["shares"],
            stock["purchase_price"],
            current_price,
            profit_loss))
        
        total_invested += cost
        total_current += current_value
    
    print("-" * 50)
    print("TOTAL INVESTED: ${:.2f}".format(total_invested))
    print("CURRENT VALUE:  ${:.2f}".format(total_current))
    print("NET PROFIT/LOSS: ${:.2f}".format(total_current - total_invested))

def main():
    portfolio = load_portfolio()
    
    while True:
        print("\nSTOCK PORTFOLIO TRACKER")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            portfolio = remove_stock(portfolio)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()