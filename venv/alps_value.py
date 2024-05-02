#!/usr/bin/python
# -*- coding: Shift-JIS -*-

import yfinance as yf

data_alps = yf.download('4641.T', period = '15d', interval = '1d')

#環境によって出力の見え方が異なる？
#Google Colabratory = print文が不要
#VSCode = print文が必要
print(data_alps)