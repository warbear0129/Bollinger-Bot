import pandas as pd
from utils import *

class Bollinger(object):

    def __init__(self, config):
        self._long_margin = config["longmargin"]
        self._short_margin = config["shortmargin"]
        self._bb_length = config["bb_length"]
        self._bb_std = config["bb_std"]

    def _get_bb(self, chart_Data):
        data_list = []

        for cd in chart_Data:
            data_list.append({"high": cd["high"], "low": cd["low"], "price": cd["close"]})

        df = pd.DataFrame(data_list)

        df["std_high"] = df["high"].rolling(window=10).std()
        df["sma_high"] = df["high"].rolling(window=10).mean()
        df["upper_band"] = df["sma_high"] + (df["std_high"] * 2)

        df["std_low"] = df["low"].rolling(window=10).std()
        df["sma_low"] = df["low"].rolling(window=10).mean()
        df["lower_band"] = df["sma_low"] - (df["std_low"] * 2)

        return df.tail(1).to_dict(orient='records')[0]

    def create_order(self, chart_Data):
        bb = self._get_bb(chart_Data)
        current_price = float(bb["price"])
        dict_opening_order = {}
        
        opening_rate_short = float(bb["upper_band"]) * self._short_margin
        opening_rate_long = float(bb["lower_band"]) * self._long_margin

        delta_short = getDelta(opening_rate_short, current_price)
        delta_long = getDelta(opening_rate_long, current_price)

        if delta_long <= delta_short:
			dict_opening_order["rate"] = opening_rate_long
			dict_opening_order["delta"] = delta_long
			dict_opening_order["type"] = "LONG"

        else:
            dict_opening_order["rate"] = opening_rate_short
            dict_opening_order["delta"] = delta_short
            dict_opening_order["type"] = "SHORT"

        return dict_opening_order

        

    