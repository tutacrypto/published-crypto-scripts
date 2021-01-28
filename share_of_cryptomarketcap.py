import pandas as pd
import plotly.graph_objects as go

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

crypto_100 = cg.get_coins_markets(vs_currency='usd')

df = pd.DataFrame(crypto_100, columns=['id', 'symbol', 'market_cap'])

total_market_cap = df['market_cap'].sum()
df['share_market_cap'] = (df['market_cap'] / total_market_cap)*100
df['share_alts_market_cap'] = (df['market_cap'] / (total_market_cap - df.loc[0]['market_cap']))*100

# splitting total market and alts (crypto market without BTC)
total = df
total2 = df.loc[1:]

# Share of Total Market Cap
total = go.Figure(
    data=[go.Bar(x=total['symbol'], y=total['share_market_cap'])],
    layout_title_text="Share of Crypto MarketCap"
)
total.show()

# Share of ALts Market Cap
total2 = go.Figure(
    data=[go.Bar(x=total2['symbol'], y=total2['share_alts_market_cap'])],
    layout_title_text="Share of Alts MarketCap"
)
total2.show()

