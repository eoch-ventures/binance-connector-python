#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

spot_client = Client(api_key, api_secret)
logging.info(
    spot_client.sub_account_futures_asset_transfer_history(
        email="",
        futuresType=1,  # 1:USDT-maringed Futues，2: Coin-margined Futures
    )
)
