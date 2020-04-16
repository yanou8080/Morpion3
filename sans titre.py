Tour = 0
list1 = ["","",""]
list2 = ["","",""]
list3 = ["","",""]
T = 0
while Tour <= 9:
	Tour = Tour + 1
	if T == 0:
		print("le joueur 1 commence")
		T = T + 1
		list_choisit = input("Qu'elle liste chosit tu? Tu ne peux choisir que entre 1 et 3.")
		list_choisit = int(list_choisit)
		if list_choisit == 1:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list1 = ["X","",""]
			elif case_choisit == 2:
				list1 = ["","X",""]
			elif case_choisit == 3:
				list1 = ["","","X"]
		elif list_choisit == 2:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list2 = ["X","",""]
			elif case_choisit == 2:
				list2 = ["","X",""]
			elif case_choisit == 3:
				list2 = ["","","X"]
		elif list_choisit == 3:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list3 = ["X","",""]
			elif case_choisit == 2:
				list3 = ["","X",""]
			elif case_choisit == 3:
				list3 = ["","","X"]
			print(list1)
			print(list2)
			print(list3)

	else:
		print("le joueur 2 commence")
		T = T - 1
		list_choisit = input("Qu'elle liste chosit tu? Tu ne peux choisir que entre 1 et 3.")
		list_choisit = int(list_choisit)
		if list_choisit == 1:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list1 = ["O","",""]
			elif case_choisit == 2:
				list1 = ["","O",""]
			elif case_choisit == 3:
				list1 = ["","","O"]
		elif list_choisit == 2:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list2 = ["O","",""]
			elif case_choisit == 2:
				list2 = ["","O",""]
			elif case_choisit == 3:
				list2 = ["","","O"]
		elif list_choisit == 3:
			case_choisit = input ("Qu'elle case chosit tu? Tu ne peux choisir que entre 1 et 3.")
			case_choisit = int(case_choisit)
			if case_choisit == 1:
				list3 = ["O","",""]
			elif case_choisit == 2:
				list3 = ["","O",""]
			elif case_choisit == 3:
				list3 = ["","","O"]
			print(list1)
			print(list2)
			print(list3)

