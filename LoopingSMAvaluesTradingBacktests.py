
# GOOD ONE-
import pandas as pd

# Load historical forex data from CSV file - columns should be 'date_and_time',	'Open',	'High',	'Low', 'Close'
path = 'path to your file'
data = pd.read_csv(path, index_col=0)

# Define trading strategy
def simple_moving_average_strategy(data, short_window, long_window):
    # Compute simple moving averages
    data['short_sma'] = data['Close'].rolling(short_window).mean()
    data['long_sma'] = data['Close'].rolling(long_window).mean()

    # Generate buy/sell signals
    data['signal'] = 0
    data.loc[data['short_sma'] > data['long_sma'], 'signal'] = 1
    data.loc[data['short_sma'] < data['long_sma'], 'signal'] = -1

    # Compute returns based on signals
    data['returns'] = data['signal'] * data['Close'].pct_change()

    # Compute cumulative returns
    data['cumulative_returns'] = (1 + data['returns']).cumprod()

    return data['cumulative_returns'][-1]

# Function to track trades and calculate profits per trade
def track_trades(data):
    trades = []
    in_trade = False
    entry_price = 0
    for i in range(len(data)):
        if 'signal' not in data.columns:
            break
        if data['signal'][i] == 1 and not in_trade:
            in_trade = True
            entry_price = data['Close'][i]
            trades.append({'Entry': data.index[i], 'Entry Price': entry_price})
        elif data['signal'][i] == -1 and in_trade:
            in_trade = False
            exit_price = data['Close'][i]
            profit = exit_price - entry_price
            trades[-1]['Exit'] = data.index[i]
            trades[-1]['Exit Price'] = exit_price
            trades[-1]['Profit'] = profit

    return trades

# Loop through multiple SMA values and backtest trading strategy
results = []
for short_window in range(10, 300, 5):
    for long_window in range(305, 600, 5):
        if short_window < long_window:
            key = f'{short_window},{long_window}'
            cumulative_returns = simple_moving_average_strategy(data.copy(), short_window, long_window)
            trades = track_trades(data.copy())
            results.append({'SMA Short Period': short_window, 'SMA Long Period': long_window,
                            'Cumulative Returns': cumulative_returns, 'Trades': trades})

# Drop the 'Trades' column from the main results DataFrame
for result in results:
    result.pop('Trades')

# Convert results list to DataFrame and write to CSV file
results_df = pd.DataFrame(results)
results_df.to_csv(r'C:\Users\badar\Downloads\EURUSDH4_out.csv', index=False)


# Print results
for result in results:
    print(f"SMA Short Period: {result['SMA Short Period']}, SMA Long Period: {result['SMA Long Period']}, "
          f"Cumulative Returns: {result['Cumulative Returns']}")

print("\nTrade Details:")
