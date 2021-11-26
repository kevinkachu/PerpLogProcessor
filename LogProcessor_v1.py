import config

import datetime as dt
import numpy as np
import pandas as pd
import pytz
import os
import dateutil.parser as dparser
import re
import itertools
from utils import *

class PerpBotLogProcessor():
    def __init__(self, wallet_alias, data_directory='D:/botlogs/txs/'):
        self.wallet_alias = wallet_alias
        self.address = config.wallet_aliases[wallet_alias]['address']
        self.data_directory = data_directory
        self.list_of_files = self.get_filenames(config.data_directory, config.wallet_aliases[self.wallet_alias]['file_string'])
        # self.log_groups = {}
        # self.df = pd.DataFrame()
        self.trades = None
        # self.reset_trades_dfs()
        # self.netliq = pd.DataFrame()
        # self.transfers = transfers

    def get_filenames(self, data_directory, filter):
        list_of_files = []
        for (dirpath, dirnames, filenames) in os.walk(data_directory):
            for file in filenames:
                if filter in file and not self.old_file(file):
                    list_of_files += [os.path.join(dirpath, file)]
        return list_of_files

    def import_files(self, start_dt = dt.datetime(2021,11,14)):
        #Need to filter for wallet address
        self.df = pd.concat(map(self.process_log_csv, self.list_of_files)).reset_index(drop=True)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'].astype(float), unit='ms')
        self.df = self.df.loc[self.df['timestamp'] >= start_dt]
        self.df['binance_ts'] = pd.to_datetime(self.df['binance ts'].astype(float), unit='ms')
        self.df['perp_ts'] = pd.to_datetime(self.df['perpetual ts'].astype(float), unit='ms')
        self.df['quote asset reserve'] = self.df['quote asset reserve'].astype(float) / 10 ** 18
        self.df = self.df.sort_values(by=['timestamp'], ignore_index=True).drop(columns = ['binance ts', 'perpetual ts'])

    def compute_trades(self):
        trades = self.df.loc[np.isin(self.df['type'], ['open end']) | self.df['type'].str.contains('open failed')].copy()
        trades['trade_size'] = trades['trade amt'] / trades['open price']
        trades['total_price_impact'] = trades['perpetual mark price'] * trades['trade amt'] / trades[
            'quote asset reserve'] * 2
        trades['maximum_edge'] = (trades['binance price'] * (1 + trades['neutral level']) - trades[
            'perpetual mark price'] - trades['total_price_impact'] / 2) * \
                                 trades['trade amt'] / (
                                             trades['perpetual mark price'] + trades['total_price_impact'] / 2)
        trades['realized_edge'] = (trades['binance price'] * (1 + trades['neutral level']) - trades['open price']) * \
                                  trades['trade_size']
        slc_failed_trade = trades['type'].str.contains('open failed')
        trades.loc[slc_failed_trade, 'realized_edge'] = 0
        self.trades = pd.merge_asof(trades,
                                  self.df.loc[self.df['type'] == 'x_threshold'].rename(columns={'timestamp': 'trigger_ts'})[
                                      ['trigger_ts']],
                                  left_on='timestamp', right_on='trigger_ts', direction='backward', suffixes=('', ''))

    @staticmethod
    def old_file(file_path):
        ts = read_file_ts(file_path)
        return True if ts < dt.datetime(2021, 11, 14) else False

    @staticmethod
    def process_log_csv(file_path):
        df_temp = pd.read_csv(file_path, sep='[|]')
        for n in range(len(df_temp)):
            if ',' in str(df_temp.loc[n, 'timestamp']):
                splitted_str = str.split(df_temp.loc[n, 'timestamp'], ',', maxsplit=1)
                df_temp.loc[n, 'timestamp'], df_temp.loc[n, 'comment'] = splitted_str[0], splitted_str[1]
        df_temp['wallet address'] = df_temp['wallet address'].fillna(method='ffill').fillna(method='bfill')
        # There are some files that don't have wallet addresses because it's all errors
        #         print(len(df_temp.loc[pd.isna(df_temp['wallet address'])]), file_path)
        return df_temp.sort_values(by='timestamp')



def calc_expected_spread(spread, anchor, slope):
    if np.abs(spread) < anchor:
        return spread
    else:
        return np.sign(spread) * (anchor + slope * (np.abs(spread) - anchor))