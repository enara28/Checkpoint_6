# Ejercicio práctico Checkpoint 6

class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

objeto = Usuario("enara", "contraseña")
print(objeto.usuario)
print(objeto.contraseña)