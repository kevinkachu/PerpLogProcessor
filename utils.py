import datetime as dt
import itertools
import re
import os
import pandas as pd

def remove_tz(this_dt):
    if this_dt.tzinfo is None:
        return this_dt
    else:
        return this_dt.replace(tzinfo=None)

def read_file_ts(file_path):
    for k1, k2, k3 in itertools.product([1, 2], [1, 2], [1, 2]):
        match = re.search(r'\d{4}-\d{' + str(k1) + '}-\d{' + str(k2) + '}-\d{' + str(k3) + '}', file_path)
        if match is not None:
            break
    return dt.datetime.strptime(match.group(), '%Y-%m-%d-%H')

def get_dune_data():
    filenames = get_filenames('d:/python/data/crypto/dune/', 'dune_perp_trade_info_gas')
    df_dune = pd.concat([pd.read_csv(file, parse_dates=[16]) for file in filenames]).reset_index(drop=True)
    df_dune['block_time'] = df_dune.apply(lambda row: remove_tz(row['evt_block_time']), axis=1)
    return df_dune

def get_filenames(data_directory, filter):
    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(data_directory):
        for file in filenames:
            if filter in file:
                list_of_files += [os.path.join(dirpath, file)]
    return list_of_files