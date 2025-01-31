"""
BANCO DE MASCOTAS
Crear una clase llamada Mascota con los atributos: nombre, especie y edad.
Agregar un método hablar que imprima un mensaje dependiendo de la especie (por ejemplo, "guau" para perros).
Generar tres objetos de tipo Mascota y describirlos.
"""

# Diccionario de onomatopeyas según la especie animal
onomatopeyas = {
    'Perro': 'Woof woof',
    'Gato': 'Meow',
    'Conejo': 'Coui coui',
    'Pájaro': 'Tweet'
}

# Clase Mascota con los atributos: nombre, especie, edad
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre.capitalize()
        self.especie = especie.capitalize()
        self.edad = edad
    
# Función para que la mascota "hable" en caso de poseer onomatopeya
    def hablar(self):
        sonido = onomatopeyas.get(self.especie)
        if self.especie in onomatopeyas:
            print(f'{self.nombre} hace "{sonido}~".')
        else:
            print(f'La especie "{self.especie}" no posee un sonido en particular.\n')
    
# Función para describir a la mascota (nombre, especie y edad)
    def describir(self):
        return f'\n{self.nombre} es de la especie "{self.especie}" y tiene {self.edad} año(s).'
    
# Función para traer los objetos de tipo Mascota en una lista con su respectiva descripción
def listado_mascotas():
    print('\nBienvenido al "Banco de Mascotas" 🐾\nEstas son las mascotas que poseemos:')
    return [
        Mascota('Onur', 'Perro', 5),
        Mascota('Samantha', 'Gato', 16),
        Mascota('Sparkle', 'Conejo', 2),
        Mascota('Artemis', 'Pájaro', 1),
        Mascota('Squalo', 'Tiburón', 10)
    ]

# Bucle que recorre los objetos dentro de la función, imprime su descripción y su respectiva onomatopeya
for mascota in listado_mascotas():
    print(mascota.describir())
    mascota.hablar()

# Mensaje de cierre
print('Esta ha sido la lista de mascotas del "Banco de Mascotas", y espero que les haya gustado. ¡Chau! 👋\n')
