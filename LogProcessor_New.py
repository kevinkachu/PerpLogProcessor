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
    def __init__(self, wallets, transfers, fee_ratio=0.001, data_directory='D:/botlogs/txs/'):
        self.data_directory = data_directory
        self.list_of_files = self.get_all_filenames()
        self.log_groups = {}
        self.df, self.df_dune = pd.DataFrame(), pd.DataFrame()
        self.trades = {}
        self.reset_trades_dfs()
        self.netliq = pd.DataFrame()
        self.fee_ratio = fee_ratio
        self.transfers = transfers

    def import_files(self):
        self.df = pd.concat(map(self.process_log_csv, self.list_of_files)).reset_index(drop=True)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'].astype(float), unit='ms')
        self.df['binance_ts'] = pd.to_datetime(self.df['binance ts'].astype(float), unit='ms')
        self.df['perp_ts'] = pd.to_datetime(self.df['perpetual ts'].astype(float), unit='ms')
        # self.df.loc[pd.isna(self.df['binance_ts']), 'binance_ts'] = self.df['timestamp']
        # self.df.loc[pd.isna(self.df['perp_ts']), 'perp_ts'] = self.df['timestamp']
        self.df = self.df.sort_values(by=['wallet address', 'timestamp'], ignore_index=True)



    def get_all_filenames(self):
        list_of_files = []
        for (dirpath, dirnames, filenames) in os.walk(self.data_directory):
            for file in filenames:
                if not self.old_file(os.path.join(dirpath, file)):
                    list_of_files += [os.path.join(dirpath, file)]
        return list_of_files

    @staticmethod
    def old_file(file_path):
        ts = read_file_ts(file_path)
        return True if ts < dt.datetime(2021, 10, 25) else False

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

    def reset_trades_dfs(self):
        self.trades = {}
        for wallet in config.wallets.keys():
            self.trades[wallet] = pd.DataFrame()



def compute_trades_info(df, wallet):
    k = config.liquidity[config.wallets[wallet]]
    df = trades_adjust_transfers_single(df, wallet)
    mask_restart = df['type'].str.contains('init_close_end',na=False)
    df.loc[mask_restart, ['position size', 'margin amount', 'open notional']] = 0, 0, 0
    df['gas_fee'] = -0.2
    df['prev_size'] = df['position size'].shift(1)
    df['observed_edge_pct'] = df['pct diff']-df['neutral level']
    df['expected_edge_pct'] = df.apply(lambda row: calc_expected_spread(row['observed_edge_pct'], config.anchor, config.slope), axis=1)
    df['trade_amount'] = df['open price'] * (df['position size'] - df['prev_size'])
    df['volume'] = np.abs(df['trade_amount'])
    df['raw_edge'] = -(df['perpetual mark price'] - df['binance price']*(1 + df['neutral level']))*(df['position size'] \
                            - df['prev_size'])
    df['expected_edge'] = -(df['binance price']*(df['expected_edge_pct'] + df['trade_amount']/k))*(df['position size'] \
                           - df['prev_size']) - np.abs(df['trade_amount']) * config.trading_fee_pct
    df['executed_edge'] = -(df['open price'] - df['binance price']*(1 + df['neutral level']))*(df['position size'] - df['prev_size'])- np.abs(df['trade_amount']) * config.trading_fee_pct
    df.loc[df['type'] == 'close end', 'executed_edge' ] = -(df['close price'] - df['binance price']*(1 + df['neutral level']))*(df['position size'] - df['prev_size'])- np.abs(df['trade_amount']) * config.trading_fee_pct
    df['delta_quality'] = df['prev_size']*(df['binance price']*(1+df['neutral level'])-df['binance price'].shift(1)*(1+df['neutral level'].shift(1)))
    df.loc[mask_restart, 'delta_quality'] = 0
    return df

def calc_expected_spread(spread, anchor, slope):
    if np.abs(spread) < anchor:
        return spread
    else:
        return np.sign(spread) * (anchor + slope * (np.abs(spread) - anchor))

def fix_df_start(df):
    mask_open = df['trade type'].str.contains('open', na=False)
    mask_flip = df['trade type'].str.contains('flip', na=False)
    mask_close = df['trade type'].str.contains('close', na=False)
    while df.index[0] in df[mask_flip | mask_close | mask_open].index:
        df = df.iloc[1:].reset_index(drop=True)
        mask_open = df['trade type'].str.contains('open', na=False)
        mask_flip = df['trade type'].str.contains('flip', na=False)
        mask_close = df['trade type'].str.contains('close', na=False)
    return df

def trades_adjust_transfers_single(df, wallet):
    df['usdc_adj'], df['xdai_adj'] = 0, 0
    for transfer in config.transfers:
        transfer_coin, transfer_time, currency, amount = transfer
        if config.wallets[wallet] == transfer_coin:
            df.loc[df['timestamp'] >= transfer_time, currency + '_adj'] = \
            df[currency + '_adj'] - amount
    return df