\sort_of_subshells = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']
element_num = int(input("Number of The Element: "))
subshells_with_values = {
	's': 2,
	'p': 6,
	'd': 10,
	'f': 14
}

string = ""
n = 0
while element_num != 0:
	subshell = sort_of_subshells[n]
	n += 1

	if subshells_with_values[subshell[1]] > element_num:
		string += subshell + str(subshells_with_values[subshell[1]] - element_num)
		print(string)
		exit()
	else:
		element_num -= subshells_with_values[subshell[1]]
		string += subshell + str(subshells_with_values[subshell[1]]) + " "
	
print(string)
