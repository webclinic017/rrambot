#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_kline_1m_with_unicorn_fy.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2021, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# %%
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import (
    BinanceWebSocketApiManager,
)
import time
import os

# %%

# create instance of BinanceWebSocketApiManager
binance_websocket_api_manager = BinanceWebSocketApiManager(
    exchange="binance.com", output_default="UnicornFy"
)

btc_id = binance_websocket_api_manager.create_stream(
    "kline_1m", "btcusdt", stream_label="UnicornFy", output="UnicornFy"
)
# %%
# binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="dict", output="dict")

# binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="raw_data", output="raw_data")
c = 0
while True:
    if binance_websocket_api_manager.is_manager_stopping():
        exit(0)
    oldest_stream_data_from_stream_buffer = (
        binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
    )
    if oldest_stream_data_from_stream_buffer is False:
        time.sleep(0.01)
    else:
        if oldest_stream_data_from_stream_buffer is not None:
            try:
                if (
                    oldest_stream_data_from_stream_buffer["event_time"]
                    >= oldest_stream_data_from_stream_buffer["kline"][
                        "kline_close_time"
                    ]
                ):
                    # print only the last kline
                    print(f"UnicornFy: {oldest_stream_data_from_stream_buffer}")
            except KeyError:
                print(f"dict: {oldest_stream_data_from_stream_buffer}")
            except TypeError:
                print(f"raw_data: {oldest_stream_data_from_stream_buffer}")
    c += 1

# %%
