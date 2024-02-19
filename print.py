def imprimir_contenido_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
ruta_del_archivo = 'ruta/del/archivo.txt' 
imprimir_contenido_archivo(ruta_del_archivo)
