# [Nopal-viTools en Linux!](https://github.com/Nopal-vi/Nopal-viTools-sh)
# Nopal-viTools 🌵
![GitHub](https://img.shields.io/github/license/nopal-vi/nopal-vitools?color=r&logo=i) ![GitHub followers](https://img.shields.io/github/followers/nopal-vi?color=r) ![GitHub all releases](https://img.shields.io/github/downloads/nopal-vi/nopal-vitools/total?color=r)
## ¿Como se utiliza?
### Windows:
**EXTERNO**: Para utilizar [Nopal-viTools](https://github.com/Nopal-vi/Nopal-viTools) debemos tener descargado el programa [FFmpeg](https://mega.nz/file/b4p01C4b#jXOvdNONX7SJgGLyxRiDEItVAMsglSemp5BR0qr4Kko) y crear una carpeta junto a Nopal-viTools con ella.

**INTERNO**: Descarga [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases) y luego crear una carpeta en tu disco C de tu computadora: (FFmpeg es disponible solo en 64bits)

> C:\ffmpeg\ffmpeg\bin

Ahora ve a `Propiedades del Equipo`, `Configuración Avanzada del sistema` y dentro del apartado `Opciones Avanzadas` vamos a la `Variable de enterno`.

Editado la variable `Patch`, y dentro de ella añadimos nuestra direccion de ffmpeg que ubicamos en nuestro Disco C. Ejemplo:

> ...;C:\ffmpeg\ffmpeg\bin

Para añadir el valor de la variable que nuestro caso es ffmpeg debemos comenzar primero con `;` y luego agregamos la direccion donde esta ubicada ffmpeg

## Tutorial de Nopal-viTools
Una vez hecho el primer paso, es muy simple de utilizar Nopal-viTools pero antes necesitas saber sus caracteristicas:

### Tipo de formato disponible:
- mp4
- avi
- mov
- mwv
### Resolucion de los videos de Nopal-vi: (Algunos disponibles)
- xvids: 256x192
- xvidsi: 256X144 **Recomendado por los usuarios de Nopal-viTools**

Para utilizar Nopal-viTools, primero te pedira que selecciones un lenguaje:

> select a language: \
ES: Spanish \
EN: English \
-> _

Por lo cual, tu seleccionaras el que gustes! Entraras a la ventana principal que te dice lo que se trata de ester programa y seleccionaras la resolucion que quieres añadir a tu video (**no reemplazara el video original, solo que creara uno nuevo**).

### Nombre del Archivo
El nombre del archivo debe ser `nopal_vi` anteriormente era `vid_source` en las versiones anteriores pero debido a que los usuarios se le complicaba guardar muy bien el nombre del archivo introduccido.

### Finalización
Ya que el ffmpeg ha hecho su trabajo, el archivo sera guardado como `nopal_ouput.avi`, puede visualizar el video previo en su reproductor el que guste para rectificar si no ha habido problema con la conversión.

## Tuna-viDS
Crea una carpeta en la raiz de la tarjeta de la consola
> Z:\video\

Donde aqui añadiras todos los videos convertidos de Nopal-viTools, puedes renombrar el nombre del archivo el que gustes o el nombre del archivo original.

# Creditos
[Tuna-viDS](https://github.com/chishm/tuna-vids) <3 \
[FFmpeg](https://ffmpeg.org/) \
[Nopal-viTools](https://github.com/Nopal-vi/Nopal-viTools)
