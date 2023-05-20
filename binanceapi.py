#1setup
apikey='Binance Api Key'
secret='Binance Secret Key '
!pip install pandas 
!pip install xlsxwriter

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import xlsxwriter

#Authenticate
client=Client(apikey, secret)
#get tickers
tickers=client.get_all_tickers()
ticker_df=pd.DataFrame(tickers)

ticker_df.set_index('symbol',inplace=True)
ticker_df.loc['BTCUSDT']

y=ticker_df.loc['BTCUSDT']
x=ticker_df.loc['ETHUSDT']

#get historical data bearish seasons 3 Months
historical=client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2022','1 Apr  2022')
hist_df=pd.DataFrame(historical)
hist_df.columns=["Open Time "," Open", "High ","Low", "Close", "Volume","Close Time","Quote Assets Volume", " Number of Trades", "TB Base Volume ", " TB Quote Vole","Ignore"]

btc=client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2022','1 Apr 2022')
z=pd.DataFrame(btc)
z.columns=["Open Time "," Open", "High ","Low", "Close", "Volume","Close Time","Quote Assets Volume", " Number of Trades", "TB Base Volume ", " TB Quote Vole","Ignore"]

writer=pd.ExcelWriter("ethbearish.xlsx",engine="xlsxwriter")
hist_df.to_excel(writer, sheet_name="Sheet 1")

writer.close()

writer=pd.ExcelWriter("btcbearish.xlsx",engine="xlsxwriter")
z.to_excel(writer, sheet_name="Sheet 1")

writer.close()

# and ıf you want to different cryptocurrency you can change ticker_df.loc !
#if you want a,different time interval yoou can change to client kline interval days !
