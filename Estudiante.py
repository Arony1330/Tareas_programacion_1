class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        if not isinstance(nota, (int, float)):
            raise ValueError("La nota debe ser un número")
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61


if __name__ == "__main__":
    estudiante = Estudiante("Cesar Tello", "20250123", "Programación 1")
    estudiante.agregar_nota(75)
    estudiante.agregar_nota(58)
    estudiante.agregar_nota(63)

    print(f"Nombre: {estudiante.nombre}")
    print(f"Carnet: {estudiante.carnet}")
    print(f"Carrera: {estudiante.carrera}")
    print(f"Notas: {estudiante.notas}")
    print(f"Promedio: {estudiante.promedio():.2f}")
    print(f"Aprobado: {estudiante.aprobado()}")
