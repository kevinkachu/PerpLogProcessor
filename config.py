import datetime as dt

wallet_aliases = {'UNI':{'address':'0xf8Adb081e4871921B91f97e345F1244475369C5c',
                       'token':'UNI',
                       'file_string': 'bot_log_data_UNI'},
                  'AAVE':{'address':'0x234aA61d403D1Fd9908490116bd145400d890415',
                       'token':'AAVE',
                       'file_string': 'bot_log_data_AAVE'},
                  'SUSHI': {'address': '0xC3e5EA6587A52E0C424953E9eb1aa0559e257e89',
                           'token': 'SUSHI',
                           'file_string': 'bot_log_data_SUSHI'},
                  'ALPHA': {'address': '0xd22084C2444943dB47c6efF3084B087F5e8f77de',
                            'token': 'ALPHA',
                            'file_string': 'bot_log_data_ALPHA'},
                  'CRV': {'address': '0xee4cCf4bBEef453768D59e3c87947561Cbef18a1',
                            'token': 'CRV',
                            'file_string': 'bot_log_data_CRV'},
                  'GRT': {'address': '0x23F9402776c055E9fE3b60fA29AB01FE20EAFc5F',
                          'token': 'GRT',
                          'file_string': 'bot_log_data_GRT'},
                  'COMP': {'address': '0x579012092E587792ad3d27938A14Fe8A945b4339',
                          'token': 'COMP',
                          'file_string': 'bot_log_data_COMP'},
                  'ETH': {'address': '0xf1d27707324A58Bf332a367705D221C3b47EF00A',
                           'token': 'ETH',
                           'file_string': 'bot_log_data_ETH'},
                  }


wallets = {
    # '0x0E77505A596e4797CE80f877b2052C753341f154':'ALPHA2',
            '0x23F9402776c055E9fE3b60fA29AB01FE20EAFc5F':'GRT',
            '0x579012092E587792ad3d27938A14Fe8A945b4339':'COMP',
            # '0x5E4724D31080223C0620C7e125Ea886B7Ed0A201':'PERP2',
            '0x8E7D20f1f703B05f2817732Be25256a4d9aB27e8':'PERP',
            '0x940c3B8772FDfEd66eA165C2c0011C65c57Bea01':'BTC',
            '0xc5c1a28e9538958970aD3058923ecaC0dcf96a3a':'REN',
            '0xd22084C2444943dB47c6efF3084B087F5e8f77de':'ALPHA',
            '0xee4cCf4bBEef453768D59e3c87947561Cbef18a1':'CRV',
            '0xf1d27707324A58Bf332a367705D221C3b47EF00A':'ETH',
            '0xC3e5EA6587A52E0C424953E9eb1aa0559e257e89':'SUSHI',
            '0x7F0E846390a810df1cad8DEeF39769FcE4746E1a':'DOT',
           '0x234aA61d403D1Fd9908490116bd145400d890415':'AAVE',
           '0x1611e9D39B925D8856707456bbD9b9EeaA9AB2bD':'FTT',
           '0x79856232748b1a5131Ab1f727f04BC936D25e951':'LINK',
           '0xf8Adb081e4871921B91f97e345F1244475369C5c':'UNI',
           '0xe5c4521EC0F5D785c3e3B90512E607BaE926f5Ce':'SNX',
           '0x22879D85D08019984Fa7a54d0e4f4066d41a4ac3':'MKR',
           '0xc47148926fD60F3c04Ca36C4CB7C4471846F35FE':'CREAM',
           '0xbB63CE5242186728Bb0EBC5b62c6A76eEf647C35':'YFI'}

skip_wallets = ['0x0E77505A596e4797CE80f877b2052C753341f154']

transfers = [['ALPHA', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['ALPHA', dt.datetime(2021,10,1,0,0), 'usdc', 3500],
             ['BTC', dt.datetime(2021,10,1,0,0), 'xdai', 350],
             ['BTC', dt.datetime(2021,10,1,0,0), 'usdc', 6500],
             ['ETH', dt.datetime(2021,10,1,0,0), 'usdc', 10500],
             ['GRT', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['GRT', dt.datetime(2021,10,1,0,0), 'usdc', 3500],
             ['PERP', dt.datetime(2021,10,1,0,0), 'xdai', 100],
             ['PERP', dt.datetime(2021,10,1,0,0), 'usdc', 10000],
             ['PERP2', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['PERP2', dt.datetime(2021,10,1,0,0), 'usdc', 3500],
             ['REN', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['REN', dt.datetime(2021,10,1,0,0), 'usdc', 1500],
             ['CRV', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['CRV', dt.datetime(2021,10,1,0,0), 'usdc', 1500],
             ['ALPHA2', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['ALPHA2', dt.datetime(2021,10,1,0,0), 'usdc', 3500],
             ['COMP', dt.datetime(2021,10,1,0,0), 'xdai', 250],
             ['COMP', dt.datetime(2021,10,1,0,0), 'usdc', 1500],
            ['CRV', dt.datetime(2021,10,9, 5,40), 'usdc', 2000],
            ['COMP', dt.datetime(2021,10,9, 5,48), 'usdc', 2000],
            ['SUSHI', dt.datetime(2021,10,9,6,3), 'xdai', 250],
            ['SUSHI', dt.datetime(2021,10,9,6,3), 'usdc', 1500],
            ['PERP', dt.datetime(2021,10,11,5,32), 'xdai', 200],
            ['PERP2', dt.datetime(2021,10,12,5,54), 'xdai', 200],
            ['PERP', dt.datetime(2021,10,12,5,59), 'usdc', -2000],
            ['REN', dt.datetime(2021,10,12,6,4), 'usdc', 2000],
            ['DOT', dt.datetime(2021,10,12,6,8), 'xdai', 250],
            ['DOT', dt.datetime(2021,10,12,6,9), 'usdc', 1500],
            ['FTT', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['FTT', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['LINK', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['LINK', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['UNI', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['UNI', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['SNX', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['SNX', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['MKR', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['MKR', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['CREAM', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['CREAM', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['YFI', dt.datetime(2021,10,14,6,0), 'xdai', 250],
            ['YFI', dt.datetime(2021,10,14,6,0), 'usdc', 1500],
            ['PERP', dt.datetime(2021,10,13,15,10), 'usdc', -3000],
            ['PERP', dt.datetime(2021,10,13,15,10), 'xdai', 200],
            ['ETH', dt.datetime(2021,10,13,15,25), 'usdc', -1000],
            ['CRV', dt.datetime(2021,10,13,15,4), 'usdc', 2000],
            ['DOT', dt.datetime(2021,10,13,15,5), 'usdc', 2000],
            ['CRV', dt.datetime(2021,10,13,15,9), 'xdai', 200],
            ['AAVE', dt.datetime(2021,10,11,23,16), 'xdai', 250],
            ['AAVE', dt.datetime(2021,10,11,23,17), 'usdc', 1500],
             ['COMP', dt.datetime(2021, 10, 15, 1, 21), 'xdai', 200],
             ['COMP', dt.datetime(2021, 10, 15, 1, 21), 'usdc', 3000],
            ['DOT', dt.datetime(2021, 10, 15, 1, 27), 'usdc', 3000],
            ['REN', dt.datetime(2021, 10, 15, 1, 31), 'xdai', 100],
            ['REN', dt.datetime(2021, 10, 15, 1, 31), 'usdc', 1000],
            ['AAVE', dt.datetime(2021, 10, 15, 1, 34), 'usdc', 2000],
            ['SUSHI', dt.datetime(2021, 10, 15, 1, 34), 'usdc', 2000],
            ['ALPHA', dt.datetime(2021, 10, 15, 2, 21), 'xdai', 200],
            ['CRV', dt.datetime(2021, 10, 15, 14, 35, 30), 'usdc', 1000],
            ['BTC', dt.datetime(2021, 10, 15, 20, 25), 'usdc', 2000],
            ['PERP', dt.datetime(2021, 10, 15, 20, 43), 'usdc', -3000],
             ['LINK', dt.datetime(2021, 10, 15, 20, 36), 'usdc', 2000],
             ['YFI', dt.datetime(2021, 10, 15, 20, 44), 'usdc', 2000],
             ['GRT', dt.datetime(2021, 10, 16, 6, 11), 'usdc', -1500],
             ['GRT', dt.datetime(2021, 10, 16, 6, 14), 'xdai', 300],
             ['DOT', dt.datetime(2021, 10, 16, 7, 23, 25), 'xdai', 300],
             ['SUSHI', dt.datetime(2021, 10, 16, 6, 16), 'xdai', 200],
             ['UNI', dt.datetime(2021, 10, 17, 2, 27), 'usdc', 2000],
             ['SNX', dt.datetime(2021, 10, 17, 2, 28), 'usdc', 2000],
             ['MKR', dt.datetime(2021, 10, 17, 2, 28), 'usdc', 2000],
             ['CREAM', dt.datetime(2021, 10, 17, 2, 28), 'usdc', 2000],
             ['GRT', dt.datetime(2021, 10, 18, 00, 25), 'usdc', 2000],
             ['PERP', dt.datetime(2021, 10, 19, 4, 28), 'xdai', 300],
             ['FTT', dt.datetime(2021, 10, 21, 19, 28), 'usdc', 3523.78],
             ['FTT', dt.datetime(2021, 10, 21, 19, 22), 'xdai', 222],
             # ['ALPHA2', dt.datetime(2021, 10, 21, 12, 28), 'usdc', -3523.78],
             # ['ALPHA2', dt.datetime(2021, 10, 21, 12, 22), 'xdai', -222],
             ['LINK', dt.datetime(2021, 10, 21, 22, 4), 'xdai', 300],
             ['LINK', dt.datetime(2021, 10, 21, 22, 4), 'usdc', 1000],
             ['AAVE', dt.datetime(2021, 10, 21, 22, 4), 'xdai', 300],
             ['CRV', dt.datetime(2021, 10, 25, 6, 46), 'usdc', -2000],
             ['CRV', dt.datetime(2021, 10, 25, 6, 48), 'xdai', 500],
             ['PERP2', dt.datetime(2021, 10, 25, 6, 48), 'xdai', 500],
             ['REN', dt.datetime(2021, 10, 25, 6, 48), 'xdai', 500],
             ['SUSHI', dt.datetime(2021, 10, 27, 4, 15), 'usdc', 3500],
             ['GRT', dt.datetime(2021, 10, 27, 15, 32), 'xdai', 500],
             ['YFI', dt.datetime(2021, 10, 27, 18, 32), 'xdai', 250],
             ['CREAM', dt.datetime(2021, 10, 27, 18, 32), 'xdai', 250],
             ['PERP2', dt.datetime(2021, 10, 27, 18, 35), 'usdc', -3000],
             ['MKR', dt.datetime(2021, 10, 27, 18, 36), 'xdai', 250],
             ['SNX', dt.datetime(2021, 10, 27, 18, 36), 'xdai', 350],
             ['UNI', dt.datetime(2021, 10, 27, 18, 38), 'xdai', 300],
             ['ETH', dt.datetime(2021, 10, 27, 18, 39), 'xdai', 300],
             ['BTC', dt.datetime(2021, 10, 27, 18, 41), 'xdai', 300],
             ['SUSHI', dt.datetime(2021, 10, 28, 2, 53), 'usdc', -3500],
             ['SUSHI', dt.datetime(2021, 10, 28, 20, 19), 'xdai', 400],
             ['SUSHI', dt.datetime(2021, 10, 28, 20, 19), 'usdc', 2000],
             ['SUSHI', dt.datetime(2021, 10, 28, 20, 20), 'usdc', 500],
             ['CRV', dt.datetime(2021, 10, 31, 3, 21), 'xdai', 400],
             ['CRV', dt.datetime(2021, 10, 31, 3, 21), 'usdc', -2400],
             ['GRT', dt.datetime(2021, 11, 1, 14, 18), 'xdai', 400],

             ]

liquidity = {'ETH':29786591.066, 'BTC':17100000, 'YFI':5800000, 'DOT':8100000, 'SNX':3800000,
             'LINK':7850000, 'AAVE':7200000, 'SUSHI':6500000, 'COMP':6700000, 'REN':7800000,
             'PERP':12862408.598, 'PERP2':12862408.598, 'UNI':7900000, 'CRV':8000000, 'MKR':6000000, 'CREAM':8200000,
             'GRT':7900000, 'ALPHA':9000000, 'ALPHA2':9000000, 'FTT':10800000}

fee_ratio = 0.001

wallet_transitions = {'SUSHI':dt.datetime(2021, 10, 25, 14, 6),
                     'ALPHA':dt.datetime(2021, 10, 29, 4, 52),
                     'YFI':dt.datetime(2021, 10, 29, 19, 45),
                      'MKR':dt.datetime(2021, 10, 29, 22, 00),
                      'CREAM': dt.datetime(2021, 10, 30, 15, 40),
                      'SNX': dt.datetime(2021, 10, 30, 16, 3),
                      'CRV': dt.datetime(2021, 10, 31, 4, 56, 20),
                      'BTC': dt.datetime(2021, 11, 2, 17, 2),
                      'UNI': dt.datetime(2021, 11, 2, 17, 17),
                      'LINK': dt.datetime(2021, 11, 2, 17, 28),
                      'ETH': dt.datetime(2021, 11, 3, 17, 45),
                      'GRT': dt.datetime(2021, 11, 3, 17, 45),
                      'DOT': dt.datetime(2021, 11, 3, 17, 45),
                      'COMP': dt.datetime(2021, 11, 4, 21, 0),
                      'AAVE': dt.datetime(2021, 11, 4, 20, 50),
                      'REN': dt.datetime(2021, 11, 4, 22, 29),
                      'FTT': dt.datetime(2021, 11, 6, 16, 9),
                      'PERP': dt.datetime(2021, 11, 9, 17, 14),

                      }

trading_fee_pct = 0.001
anchor = 0.00125
slope = 0.6
# min_trading_level = 0.0018
# max_invest_amount = 4000
# k = 6500000
# max_price_impact = 0.00125
# max_trade_amount = k * max_price_impact
# gas_fee_dollars = 0.2
# min_edge_per_trade = 1.
# target_ratio = 0.45

data_directory='D:/botlogs/txs/'