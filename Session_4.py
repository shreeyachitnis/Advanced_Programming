import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sb  # optional to set plot theme

sb.set_theme()  # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data
        #pass

    def calc_returns(self, df):
        df['change'] = df['Close'].diff()
        df['instant_return'] = np.log(df['Close']).diff().round(4)
        #pass

    def plot_return_dist(self):
        # Plot histogram of instantaneous returns
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['instant_return'].dropna(), bins=30, color='skyblue', edgecolor='black')
        plt.title('Distribution of Instantaneous Returns')
        plt.xlabel('Instantaneous Return')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
        #pass

    def plot_performance(self):
        percent_change = (self.data['Close'] - self.data['Close'].iloc[0]) / self.data['Close'].iloc[0] * 100

        # Plot stock's performance
        plt.figure(figsize=(10, 6))
        plt.plot(percent_change, color='green')
        plt.title('Stock Performance')
        plt.xlabel('Date')
        plt.ylabel('Percent Gain/Loss')
        plt.grid(True)
        plt.show()
        #pass


def main():
    # uncomment (remove pass) code below to test
    stock_symbol = "INFY"
    test = Stock(symbol=[stock_symbol]) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()



if __name__ == '__main__':
    main()