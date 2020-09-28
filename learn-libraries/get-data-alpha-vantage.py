# ----- Tutorial from https://github.com/RomelTorres/alpha_vantage -----

# ----- Import libraries -----
import os
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# ----- Get the API KEY (It is free, we can get it from Alpha Vantage website) -----
# ----- I add it to my Environment variables, so I read it from there -----
API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')


# ----- Get TimeSeries for Microsoft, and set its format as Panda format -----
ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')

# ----- Plot Close Price Only for Microsoft stock code -----
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
