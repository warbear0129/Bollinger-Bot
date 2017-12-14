import time
import pandas as pd
from colorama import init, Fore, Style

def printHeader(msg):
    print Fore.CYAN + str(msg) + Style.RESET_ALL


def printInfo(msg):
    print Fore.YELLOW + str(msg) + Style.RESET_ALL


def printSuccess(msg):
    print Fore.GREEN + str(msg) + Style.RESET_ALL


def printError(msg):
    print Fore.RED + str(msg) + Style.RESET_ALL

def log(pair, msg):
    filename = "./logs/%s.log" % pair
    with open(filename, "a") as f:
            f.write(msg + "\t\n")

def formatFloat(f):
	return '{0:.8f}'.format(float(f))

def do(f, *args):
	time.sleep(0.2)

	result = None
	while result == None:
		try:
			result = f(*args)

		except Exception, e:
			printError("Error: %s" % e.message)
			time.sleep(0.2)

	return result

def getBB(chart_Data, length, std):
	data_list = []

	for cd in chart_Data:
		data_list.append({"price": cd["close"]})

	df = pd.DataFrame(data_list)

	df["std"] = df["price"].rolling(window=int(length)).std()
	df["sma"] = df["price"].rolling(window=int(length)).mean()
	df["upper_band"] = df["sma"] + (df["std"] * int(std))
	df["lower_band"] = df["sma"] - (df["std"] * int(std))

	return df.tail(1).to_dict(orient='records')[0]

def getAmount(total, rate):
	if total == 0 or rate == 0:
		return -1

	return round(float(str(total)) / float(str(rate)), 8)

def getDelta(x, y):
	if x == 0 or y == 0:
		return 99999999999
	
	numList = [float(x), float(y)]
	return (( max(numList) / min(numList) ) - 1 ) * 100

init()
