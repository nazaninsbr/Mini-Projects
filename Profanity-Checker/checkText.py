import urllib
def readFile():
	dest = open("/Users/User/Desktop/uni/profanity editor/movie.txt")
	contents = dest.read()
	print(contents)
	dest.close()
	checkProfanity(contents)

def checkProfanity(text_to_check):
	myurl = "http://www.wdylike.appspot.com/?q="
	connection = urllib.urlopen(myurl+text_to_check)
	answer = connection.read()
	print(answer)

readFile()