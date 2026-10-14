# and
age = 25
licensed = True

if age >= age and license:
    print("Puede manejar")

# or
is_student = False
membership = True

if is_student or membership:
    print('puedes entrar')

# not
is_admin = False
if not is_admin:
    print("Acceso denegado")

# short Circuiting
# cuando encuentra el name evalua que es false Y se corta ALLI por eso no da error
# cuando uso upper() en un boleano porque deberia dar error si no lo corcocircuitaba
name = False
print(name and name.upper())
