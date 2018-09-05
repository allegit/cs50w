import urllib.request
import time

StocksToPull = 'goog','celg'

def pullData(stocks):
    try:
        urlToVisit = 'https://finance.yahoo.com/quote/GOOG?p=GOOG'
        sourcecode = urllib.request.urlopen(urlToVisit).read().decode('utf-8')
        #print(sourcecode)
        splitSource = sourcecode.split("\n")

        #print ('splitSource', splitSource)
        f = open("stockfile.txt", "a")

        for eachLine in splitSource:
            splittedLine = eachLine.split(",")
            f.write(str(splittedLine))

        print ('Pulled', stocks)
        time.sleep(1)

    except Exception as e:
        print('main loop', str(e))
        print(traceback.format_exc())

for eachStock in StocksToPull:
    pullData(eachStock)
