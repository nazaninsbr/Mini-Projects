import os
for filename in os.listdir("/Users/User/Desktop/uni/change file names/workedOn"):
	path = os.getcwd()
	os.chdir("/Users/User/Desktop/uni/change file names/workedOn")
	result = "".join([i for i in filename if not i.isdigit()])
	os.rename(filename, result)
	os.chdir(path)