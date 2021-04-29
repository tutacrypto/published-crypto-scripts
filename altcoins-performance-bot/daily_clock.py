import pandas as pd
import plotly.graph_objects as go
from pycoingecko import CoinGeckoAPI
from slackbot import Slackbot
import time
from tabulate import tabulate


#!/usr/bin/env python
from apscheduler.schedulers.blocking import BlockingScheduler

# Jobs scheduler
def scheduled_job():
    get_daily_data()


def get_daily_data() :
    cg = CoinGeckoAPI()

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    crypto_100 = cg.get_coins_markets(vs_currency='btc')
    df_top100 = pd.DataFrame(crypto_100, columns=['id', 'symbol', 'current_price', 'market_cap', 'market_cap_rank', 'price_change_percentage_24h'])

    df_top100_best24h = df_top100.sort_values('price_change_percentage_24h', ascending=False)

    ids_list = df_top100['id'].tolist()

    # df to which we'll append our coins
    df_top100_best7d = pd.DataFrame(columns=['id', 'price_change_percentage_7d'])

    for id in ids_list[:20]:
        # step 1
        coin_data7d = cg.get_coin_market_chart_by_id(id=id, vs_currency='btc', days=7)
        coin_data7d = pd.DataFrame(coin_data7d)
        coin_data7d = coin_data7d['prices']
        coin_data7d = coin_data7d.to_frame() # we get a df of one column with [timestamp, prices] at each row.
        # splitting it in two columns
        coin_data7d = pd.DataFrame(coin_data7d['prices'].to_list(), columns=['timestamp', 'prices'])

        # step 2
        oldest_day = coin_data7d.head(24)
        oldest_day_price_avg = oldest_day['prices'].mean()
        mostrecent_day = coin_data7d.tail(24)
        mostrecent_day_price_avg = mostrecent_day['prices'].mean()

        # step 3
        price_change_percentage_7d = ((mostrecent_day_price_avg - oldest_day_price_avg) / oldest_day_price_avg)*100

        # step 4: appending the data
        to_append = [[id, price_change_percentage_7d]]
        print(to_append)
        df_top100_best7d = df_top100_best7d.append(pd.DataFrame(to_append, columns=['id','price_change_percentage_7d']),ignore_index=True)
        time.sleep(1)

    df_top100_best7d = df_top100_best7d.sort_values('price_change_percentage_7d', ascending=False)

    df_top100 = pd.merge(df_top100_best24h, df_top100_best7d, on='id')

    df1 = df_top100.sort_values('price_change_percentage_24h', ascending=False)

    df7 = df_top100.sort_values('price_change_percentage_7d', ascending=False)

    df1 = df1[['symbol', 'market_cap_rank', 'price_change_percentage_24h', 'price_change_percentage_7d']]

    Slackbot(df1).send_slack()
if __name__ == '__main__':
    get_daily_data()
    #sched = BlockingScheduler(timezone="UTC")
    #sched.add_job(scheduled_job, trigger='cron', day_of_week='mon-fri', hour=19, minute=41)
    #sched.start()

