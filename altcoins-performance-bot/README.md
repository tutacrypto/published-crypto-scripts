# Getting the best performing coins in BTC for the last 24h to 7 days.
## Introduction

The motivation behind this is to screen constantly (daily) the altcoins market to get info about which coins are performing the best in bitcoin terms. These are the ones I want to look at and potentially invest in.

The idea is to get a list of those, and to trigger an event to receive alerts either by email or on Slack.

In the notebook named 'best_winners_top100_24h_7d', I programmed a script to get the list with price changes in bitcoin for the last 24h and 7d.

We have a table with the price change percentage for 24h and 7 days. We can sort rows to get the best performing coins. 

Now we could build a bot that runs the script every day and send the results through Slack, email, etc ...
