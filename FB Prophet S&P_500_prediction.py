# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:30:24 2021

@author: Collin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SPdata = pd.read_csv(r"\Users\Collin\Documents\collins documents\Python Projects at home\project 9 stock price prediction\S&P500.csv")

SPdata.describe() 

SPdf = SPdata[['Date','Close']]

SPdf

SPdf = SPdf.rename(columns = {'Date':'ds','Close':'y'})

from fbprophet import Prophet as fbp

x = fbp(daily_seasonality = True)

x.fit(SPdf)

future = x.make_future_dataframe(periods=2000)

prediction = x.predict(future)

x.plot(prediction)

plt.title("Prediction of the S&P Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()