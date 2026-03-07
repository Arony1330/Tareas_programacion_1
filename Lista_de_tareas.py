tareas = []
while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append({"nombre": tarea, "completada": False})
        print("✅Tarea agregada.")
    elif opcion == "2":
        if tareas:
            for i, t in enumerate(tareas, 1):
                estado = "✅" if t["completada"] else "❌"
                print(f"{i}. {estado} {t['nombre']}")
        else:
            print("No hay tareas.")
    elif opcion == "3":
        if tareas:
            idx = int(input("# de tarea a marcar completada: "))
            if 1 <= idx <= len(tareas):
                tareas[idx - 1]["completada"] = True
                print("✅Tarea marcada como completada.")
            else:
                print("Número inválido.")
        else:
            print("No hay tareas.")
    elif opcion == "4":
        if tareas:
            idx = int(input("# de tarea a eliminar: "))
            if 1 <= idx <= len(tareas):
                tareas.pop(idx - 1)
                print("✅Tarea eliminada.")
            else:
                print("Número inválido.")
        else:
            print("No hay tareas.")
    elif opcion == "5":
        break