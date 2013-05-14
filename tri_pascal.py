def tri_pascal(num):
	if num == 0:
		return [1]
	else:
		f_correcta = []
		for contador in range(num+1):
			if contador == 0 or contador == num:
				f_correcta = f_correcta + [1]
			else:
				f_correcta = f_correcta + [tri_pascal(num-1)[contador-1] + tri_pascal(num-1)[contador]]

	return f_correcta


contador = 0
num = int(input("Ingrese el numero de fila que desea ver: "))
while contador <= num:
	print(tri_pascal(contador))
	contador = contador+1
