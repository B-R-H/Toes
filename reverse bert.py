def reverse_bert(string):
	n = 0
	lower_string = string.lower()
	start_of_berts=[]
	while n<len(string):
		if lower_string[n]=="b":
			if lower_string[n:n+4] == "bert":
				start_of_berts.append(n)
				n+=4
				continue
		n+=1
	if len(start_of_berts)<2:
		return ""
	else:
		ret_string=string[start_of_berts[0]+4:start_of_berts[-1]]
		return ret_string[::-1]