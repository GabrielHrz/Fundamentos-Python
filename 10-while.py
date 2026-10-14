
counter = 0

while counter < 6:
    print(f"number {counter}")
    counter += 1
else:
    print('Fin')


response = ''
while response.lower() != 'bye':
    response = input('escribe bye para salir : ')
else:
    print('Fin')
