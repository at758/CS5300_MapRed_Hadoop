#!/usr/bin/python
import os.path
f = open('edges.txt', 'r')
x = f.readlines()
sub_array = x[0].split()
print ("This is just a test",sub_array[2])

fromNetID = 0.857; 
rejectMin = 0.9 * fromNetID;
ctr = 0;
rejectLimit = rejectMin + 0.01;

if(os.path.isfile("./filtered_edges.txt")):
	os.remove("./filtered_edges.txt")
	print("truethatbi")

for item in x:
    sub_array = item.split()
    #print(sub_array[2]) //Run this for debug
    if((float(sub_array[2]) >= rejectMin) and (float(sub_array[2]) < rejectLimit)):
	with open("filtered_edges.txt", "a") as myFile:
    		myFile.write(str(sub_array))
        #print(sub_array)
        ctr = ctr + 1;

print("Total records ",ctr)

if(os.path.isfile("./filtered_edges.txt")):
        bashCommand = "aws s3 cp ./filtered_edges.txt s3://edu-cornell-cs-cs5300s16-at758/ --acl public-read"
	import subprocess
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	
