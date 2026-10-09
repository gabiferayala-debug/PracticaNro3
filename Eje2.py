def buscar(palabra, *lista):
    mensaje = "Aca estoy" if palabra in lista else "No Estoy disponible"
    print(mensaje)
buscar("hola", "adios", "hola", "Chauu", "Aca estoy")