def elegir_metodo_pago():
    metodos_pago = ["Tarjeta de crédito", "PayPal", "Transferencia bancaria","Efecetivo en la caja"]
    print("Métodos de pago disponibles:")
    for i, metodo in enumerate(metodos_pago):
        print(f"{i+1}. {metodo}")

    metodo_elegido = int(input("Seleccione el número del método de pago que desea: "))
    metodo_pago = metodos_pago[metodo_elegido-1]
    return metodo_pago

def comprar():
    personas = []
    for persona in personas:
            print(f"{persona.nombre}")
            print(f"Menú elegido: {menus[persona.menu_elegido-1]}")
            print(f"Hora de entrega: {persona.hora_elegida}")
            metodo_pago = elegir_metodo_pago()
            print(f"Método de pago: {metodo_pago}")
    print()
