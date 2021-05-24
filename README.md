# Python-Damas
Juego de damas en Python con Tkinter

## Requerimientos
Es necesario tener instalado Python 3.7 

## Para crear el ejecutable:
1) Instalar Pyinstaller
   <pre><code> pip3 install pyinstaller </code></pre>
   
2) Crear la distribucion
    -Para Windows: 
        <pre><code>pyinstaller --add-data "images;images" --icon=./images/icon.ico  main.py </code></pre>
    -Para Mac: 
        <pre><code>pyinstaller --add-data "images:images" --icon=./images/icon.ico  main.py </code></pre>
   
3) Encontrar el main.exe o el unix executable file en la carpeta \Damas\dist\main
