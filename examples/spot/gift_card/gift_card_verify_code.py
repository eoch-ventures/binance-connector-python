#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)

logger = logging.getLogger(__name__)

response = client.gift_card_verify_code("<the_reference_number_to_verify")
logger.info(response)
