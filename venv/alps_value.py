#!/usr/bin/python
# -*- coding: Shift-JIS -*-

import yfinance as yf

data_alps = yf.download('4641.T', period = '15d', interval = '1d')

#���ɂ���ďo�͂̌��������قȂ�H
#Google Colabratory = print�����s�v
#VSCode = print�����K�v
print(data_alps)