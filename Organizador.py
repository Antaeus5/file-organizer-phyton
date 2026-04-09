import os
import shutil

extensiones ={
    'Images':['.jpg', '.png', '.gif'],
    'Documents':['.pdf', '.docx', '.txt'],
    'Videos':['.mp4', '.avi'],
    'Others':[]
}

carpeta  = input("Enter the folder path to organize: ")

if not os.path.exists(carpeta):
    print("The path does not exist")
    exit()


for nombre_carpeta in extensiones.keys():
    ruta = os.path.join(carpeta, nombre_carpeta)
    if not os.path.exists(ruta):
        os.makedirs(ruta)

for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, archivo)

    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        movido = False

        for carpeta_destino, exts in extensiones.items():
            if extension in exts:
                destino = os.path.join(carpeta, carpeta_destino, archivo)

                if os.path.exists(destino):
                    nombre, exts = os.path.splitext(archivo)
                    contador = 1
                    while os.path.exists(destino):
                        destino = os.path.join(
                            carpeta,
                            carpeta_destino,
                            f"{nombre}_{contador}{exts}"
                        )
                        contador += 1

                shutil.move(ruta_archivo, destino)
                movideo = True
                break
        
        if not movido:
            destino = os.path.join(carpeta, 'Others', archivo)
            shutil.move(ruta_archivo, destino)

print("Files organized successfully")