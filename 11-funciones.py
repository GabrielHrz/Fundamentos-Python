# Le envio los parametros message, name
def saludar(message="Hola", name="Invitado"):
    print(f'{message}, {name}')


# Le mandamos los argumentos
saludar('Hola', 'Gabriel')
saludar()
saludar(message='Que onda', name='Invitado')


