import json
import yfinance as yf

class PortfolioTracker:
    def __init__(self):
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        try:
            with open("portfolio_data.json", "r") as file:
                return json.load(file)
        except:
            return []

    def save_portfolio(self):
        with open("portfolio_data.json", "w") as file:
            json.dump(self.portfolio, file)

    def get_stock_price(self, symbol):
        try:
            stock_data = yf.Ticker(symbol).history(period="1d")
            return round(stock_data["Close"].iloc[-1], 2)
        except:
            return None

    def add_stock(self):
        symbol = input("Enter stock symbol (e.g. AAPL): ").upper()
        shares = int(input("Number of shares: "))
        purchase_price = float(input("Purchase price per share: $"))
        
        self.portfolio.append({
            "symbol": symbol,
            "shares": shares,
            "purchase_price": purchase_price
        })
        self.save_portfolio()
        print(f"\n{symbol} added successfully!")

    def remove_stock(self):
        symbol = input("Enter stock symbol to remove: ").upper()
        self.portfolio = [s for s in self.portfolio if s["symbol"] != symbol]
        self.save_portfolio()
        print(f"\n{symbol} removed successfully!")

    def view_portfolio(self):
        if not self.portfolio:
            print("\nYour portfolio is empty!")
            return
        
        print("\n{:<6} {:<8} {:<12} {:<12} {:<12}".format(
            "SYMBOL", "SHARES", "COST", "CURRENT", "PROFIT/LOSS"))
        print("-" * 50)
        
        total_invested = 0
        total_current = 0
        
        for stock in self.portfolio:
            current_price = self.get_stock_price(stock["symbol"])
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

    def run(self):
        while True:
            print("\nSTOCK PORTFOLIO TRACKER")
            print("1. Add Stock")
            print("2. Remove Stock")
            print("3. View Portfolio")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                self.add_stock()
            elif choice == "2":
                self.remove_stock()
            elif choice == "3":
                self.view_portfolio()
            elif choice == "4":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    tracker = PortfolioTracker()
    tracker.run()