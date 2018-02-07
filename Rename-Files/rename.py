import os
for filename in os.listdir("/Users/User/Desktop/uni/change file names"):
	if filename.startswith("cheese_"):
		os.rename(filename, filename[7:])