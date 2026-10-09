def verificar(*args):
    mensaje = "Error: no pasaste suficientees argumentos" if len(args)< 2 else f"Perfecto, pasaste {len(args)} argumentos"
    print(mensaje)

verificar()
verificar(10, 15, 25,)
verificar(10, 15, 25, 30, 50)