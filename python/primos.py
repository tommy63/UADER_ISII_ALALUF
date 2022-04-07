# prime number calculator: find all primes up to n
def MostrarNumerosPrimos (total = 100):
	primeList = []
	#for loop for checking each number
	for x in range(2, total + 1):
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
	print(primeList)

def MostrarCantidadNumerosPrimos (cantidad = 20):
	#-------------------------------------------------------------
	# prime number calculator: find the first n primes
	primeList = []
	x = 2
	while len(primeList) < cantidad:
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
		x += 1
	print(primeList)


opciones = input('vuoi inserire i dati?? (s/n): ')

if opciones == 's':
	valor1 = int(input('trova i numeri primi fino a quale numero?: '))
	valor2 = int(input('Quanti numeri primi vuoi trovare?: '))
else:
	valor1 = 100
	valor2 = 20

MostrarNumerosPrimos(valor1)

MostrarCantidadNumerosPrimos(valor2)
