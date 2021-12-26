sort_of_subshells = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']

noble_gases = {
	"He": ['1s'],
	"Ne": ['1s', '2s', '2p'],
	"Ar": ['1s', '2s', '2p', '3s', '3p'],
	"Kr": ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p'],
	"Xe": ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p'],
	"Rn": ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p'],
	"Og": ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
}

element_num = int(input("Number of The Element: "))
subshells_with_values = {
	's': 2,
	'p': 6,
	'd': 10,
	'f': 14
}

def Afunc(e):
	return e[0] , subshells_with_values[e[1]]

subshells = []
n = 0
while element_num > 0:
	subshell = sort_of_subshells[n]
	n += 1

	if subshells_with_values[subshell[1]] >= element_num:
		subshells.append(subshell + str(subshells_with_values[subshell[1]] - element_num) + " ")
		element_num -= subshells_with_values[subshell[1]] - element_num
		# subshells.sort(key=Afunc)
		# print("".join(subshells))
		# exit()
	else:
		element_num -= subshells_with_values[subshell[1]]
		subshells.append(subshell + str(subshells_with_values[subshell[1]]) + " ")

subshells.sort(key=Afunc)
print("".join(subshells))



last_noble_gas = None
for noble_gas in noble_gases:
	print(noble_gases[noble_gas])
	print(subshells)

	state = True
	for x in subshells:
		if not x[:-2] in noble_gases[noble_gas]:
			state = False
	# if all(x in noble_gases[noble_gas] for x in subshells):
	# 	last_noble_gas = noble_gas
	if state == True:
		last_noble_gas = noble_gas

print(last_noble_gas)

for subshell in subshells:
	if last_noble_gas == None:
		print("".join(subshells))
		exit()
	elif subshell[:-2] in noble_gases[last_noble_gas]:
		subshells.remove(subshell)
	else:
		print(subshell[:-2])
		print(noble_gases[noble_gas])

print("".join(subshells))