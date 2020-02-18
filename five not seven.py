counter = 2000
string = ""
while counter < 3201:
	if counter%7!=0:
		string += str(counter)+","
	counter += 5
string = string[:-1]
print(string)