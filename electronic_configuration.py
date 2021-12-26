sort_of_subshells = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']

noble_gases = {
	"He": ['1s2'],
	"Ne": ['1s2', '2s2', '2p6'],
	"Ar": ['1s2', '2s2', '2p6', '3s2', '3p6'],
	"Kr": ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6'],
	"Xe": ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6'],
	"Rn": ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f14', '5d10', '6p6'],
	"Og": ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f14', '5d10', '6p6', '7s2', '5f14', '6d10', '7p6']
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
		subshells.append(subshell + str(subshells_with_values[subshell[1]] - element_num))
		element_num -= subshells_with_values[subshell[1]] - element_num
		# subshells.sort(key=Afunc)
		# print("".join(subshells))
		# exit()
	else:
		element_num -= subshells_with_values[subshell[1]]
		subshells.append(subshell + str(subshells_with_values[subshell[1]]))

subshells.sort(key=Afunc)
print(" ".join(subshells))


last_noble_gas = None
for noble_gas in noble_gases:
	status = True
	for noble_gas_subshell in noble_gases[noble_gas]:
		if noble_gas_subshell in subshells:
			pass
		else:
			status = False
	if status :
		last_noble_gas = noble_gas

# print(last_noble_gas)

for Asubshell in subshells:
	if Asubshell in noble_gases[last_noble_gas]:
		subshells.remove(Asubshell)

print(f"[{last_noble_gas}]", (" ".join(subshells)))
