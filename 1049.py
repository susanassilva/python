palavra1=str(input())
palavra2=str(input())
palavra3=str(input())
if palavra1 == "vertebrado":
	if palavra2=="ave":
		if palavra3=="carnivoro":
			print("aguia")
		else:
			print("pomba")
	elif palavra2=="mamifero":
		if palavra3 == "onivoro":
			print("homem")
		else:
			print("vaca")
elif palavra1 =="invertebrado":
	if palavra2=="inseto":
		if palavra3=="hematofago":
			print("pulga")
		else:
			print("lagarta")
	elif palavra2=="anelideo":
		if palavra3 == "hematofago":
			print("sanguessuga")
		else:
			print("minhoca")