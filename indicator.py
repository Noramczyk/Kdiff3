import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import pandas as pd
import finnhub
import time

begin = 1691415000
end = 1691436600
stock = 'MOS'

bTime = "730"

x,y,oX,oY, eX, eY = [],[],[],[],[],[]

cnt = 7

#ENVKEY/key.txt
with open('ENVKEY/key.txt') as file:
    key = file.read()
finnhub_client = finnhub.Client(api_key = key) 

# READ START FROM BUY      
with open('SINGLE/beginTimeMulti.txt') as file:
    strStart = file.read()
dateStart = datetime.strptime(strStart, '%Y-%m-%d %H:%M:%S.%f')

print(dateStart)

print("unix_timestamp from File => ",
      (time.mktime(dateStart.timetuple())))

start = time.mktime(dateStart.timetuple())
print(start)

# CURRENT TIME NOW !!
now = datetime.now()

print("unix_timestamp time now => ",
      (time.mktime(now.timetuple())))
end = time.mktime(now.timetuple())

 
# assigned regular string date
#date_time = datetime.datetime(2021, 7, 26, 21, 20)
 
# print regular python date&time
#print("date_time =>",date_time)
 
# print("unix_timestamp => ",
#       (time.mktime(date_time.timetuple())))

j = finnhub_client.technical_indicator(symbol=stock, resolution='5', 
                                       _from=start, to=end, 
                                       indicator='macd', 
                                       indicator_fields={"timeperiod": 3})

i = finnhub_client.technical_indicator(symbol=stock, resolution='5', 
                                       _from=start, to=end, 
                                       indicator='wma', 
                                       indicator_fields={"timeperiod": 5})


# k = finnhub_client.technical_indicator(symbol=stock, resolution='5', 
#                                        _from=begin, to=end, 
#                                        indicator='ema', 
#                                        indicator_fields={"timeperiod": 3})

# l = finnhub_client.technical_indicator(symbol=stock, resolution='5', 
#                                        _from=begin, to=end, 
#                                        indicator='ema', 
#                                        indicator_fields={"timeperiod": 3})

# WMA to file
iStr = str(i['wma'])
writeRunning = open("Indicator/wma.txt", "w")
writeRunning.write(iStr)                      
writeRunning.close()

for vals in i['wma']:
    intI = int(bTime)
    intI += 5
    mod = intI % 100

    if mod == 60:
        intI += 40

    bTime = str(intI)
    a = pd.to_datetime(bTime, format = '%H%M')
    tot = a.hour + (0.01 * a.minute)

    x.append(tot)
    y.append(vals)

for oVal in l['c']:
    oY.append(oVal)

for eVal in k['ema']:
    eY.append(eVal)

# print(x)
# print(y)
# Plotting both the curves simultaneously
plt.plot(x, y, color='r')
plt.plot(x, oY, color='g')
plt.plot(x, eY, color='b')

plt.title('Line Graph using CSV')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

print(y[-1])
print(oY[-1])
print(eY[-1])


# # MACD to file
# jStr = str(j['macd'])
# writeRunning = open("Indicator/macd.txt", "w")
# writeRunning.write(jStr)                      
# writeRunning.close()

# # EMA to file
# kStr = str(k['ema'])
# writeRunning = open("Indicator/ema.txt", "w")
# writeRunning.write(kStr)                      
# writeRunning.close()

# # CLOSE to file
# lStr = str(l['c'])
# writeRunning = open("Indicator/candle.txt", "w")
# writeRunning.write(lStr)                      
# writeRunning.close()

# print(i['c'])
# print(type(i['c']))
