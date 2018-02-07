def readFile():
	dest = open("/Users/User/Desktop/uni/profanity editor/movie.txt")
	contents = dest.read()
	print(contents)
	dest.close()

readFile()