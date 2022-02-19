import yfinance as yf
import plotext as plt

plt.datetime.set_datetime_form(date_form='%d/%m/%Y')

start = plt.datetime.string_to_datetime("11/07/2020")
end = plt.datetime.today.datetime
data = yf.download('goog', start, end)

prices = list(data["Close"])
dates = [plt.datetime.datetime_to_string(el) for el in data.index]
print(type(prices))
print(type(dates))
#plt.plot_date(dates, prices)

#plt.title("Google Stock Price")
#plt.xlabel("Date")
#plt.ylabel("Stock Price $")
#plt.show()