# Tablas de multiplicar del 1 al 12

for num in range(1, 13):   # bucle externo (tablas)
    print(f"\n--- Tabla del {num} ---")
    
    for i in range(1, 13):  # bucle interno (multiplicaciones)
        resultado = num * i
        print(f"{num} x {i:2d} = {resultado:3d}")

        #Salida para num = 7
        # --- Tabla  del 7 ---
        # 7 x  1 =   7
        # 7 x  2 =  14
        # ... 
        # 7 x 12 =  84