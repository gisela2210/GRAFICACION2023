"""Redimensionar imagenes a 38x46"""
import os

import cv2

# Cargamos las imagenes de la carpeta: C:\Users\Mtro Israel\Downloads\CamCap\imagen
path = 'C:/Users/Mtro Israel/Downloads/CamCap/imagen'
# Guardamos las imagenes en: C:\Users\Mtro Israel\Downloads\CamCap\imagen\p
path2 = 'C:/Users/Mtro Israel/Downloads/CamCap/imagen/p'

# Creamos una lista con los nombres de las imagenes
listaImagenes = os.listdir(path)

# Recorremos la lista de imagenes
for imagen in listaImagenes:
    # Cargamos la imagen
    img = cv2.imread(path + '/' + imagen)
    # Redimensionamos la imagen
    img = cv2.resize(img, (38, 46))
    # Renombramos a objeto_[numero].jpg y Guardamos la imagen
    cv2.imwrite(path2 + '/objeto_{}.jpg'.format(imagen), img)

    print('Imagen redimensionada: ', imagen)

print('Proceso terminado')
