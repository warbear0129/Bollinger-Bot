import time
from colorama import init, Fore, Style

def printHeader(msg):
    print Fore.CYAN + str(msg) + Style.RESET_ALL


def printInfo(msg):
    print Fore.YELLOW + str(msg) + Style.RESET_ALL


def printSuccess(msg):
    print Fore.GREEN + str(msg) + Style.RESET_ALL


def printError(msg):
    print Fore.RED + str(msg) + Style.RESET_ALL

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

def getAmount(total, rate):
	if total == 0 or rate == 0:
		return -1

	return round(float(str(total)) / float(str(rate)), 8)

def getDelta(x, y):
	if x == 0 or y == 0:
		return 99999999999
	
	numList = [float(x), float(y)]
	return abs( (( max(numList) / min(numList) ) - 1 ) * 100 )

init()
