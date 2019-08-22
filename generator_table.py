"""
Codigo generador de tablas en un pdf
"""

import numpy as np
import matplotlib.pyplot as plt
import tabla as tbl
from PIL import Image, ImageDraw, ImageFont
import os
from fpdf import FPDF

height_text = 300 #Tamanio del encabezado
font_size = 75 #Tamanio de fuente del encabezado
encabezado_separador = 3 #tamanio del separador entre el encabezado y las tablas
line_limit = 25 #numero de palabras por linea

"""
INPUT:
La funcion recibe el numero de tablas o paginas de pdf (num_tablas), el encabezado (text)
y la palabra en las tablas (palabra)
OUTPUT:
La funcion nos da un archivo pdf llamado "tablas_imprimir.pdf" que se guarda en la carpeta local
y puede ser impreso
ATENCION: solo se escribiran las primeras 6 letras de la palabra (si la palabra tiene mas de 6 letras, NO se escribirán las demas)
"""
def tables_to_pdf(num_tablas,text,palabra):
    #text = nombre+materia+paralelo
    pdf = FPDF()
    images_gye = []

    for i in range(num_tablas):
        tabla = tbl.tablaLlena()
        images = []
        for j in range(6):
            if j < len(palabra):
                table_to_png(tbl.tablaLetra(palabra[j],tabla))
            else:
                table_to_png(tabla)
            images.append(Image.open("tabla1.png"))
            os.remove("tabla1.png")
        table_gye(images,text,i)
        pdf.add_page()
        pdf.image("tablaGYE"+str(i)+".png",w=190,h=260)
        os.remove("tablaGYE"+str(i)+".png")
    pdf.output("tablas_imprimir.pdf","F")

def table_gye(images,text,num):
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)*2
    max_height = max(heights)*3 + height_text

    img_text = text_to_png(text,max_width,height_text)

    new_im = Image.new('RGB', (max_width, max_height))
    new_im.paste(img_text, (0,0))

    #width, height = im.size
    x_offset = 0
    y_offset = height_text + encabezado_separador
    num_img = 0 #numero de imagenes
    for im in images:
        new_im.paste(im, (x_offset,y_offset))
        num_img += 1
        if num_img == 2:
            num_img = 0
            x_offset = 0
            y_offset += im.size[1]
        else:
            x_offset += im.size[0]
    new_im.save('tablaGYE'+str(num)+'.png')
    new_im.close()

def table_to_png(intersection_matrix):
    min_val, max_val = 0, 5

    #Muestro el eje x en el top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    #Escondo el eje y
    plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = False
    plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False

    #Tamanio de la palabra BINGO
    plt.rc('xtick',labelsize=15)

    fig, ax = plt.subplots()

    for i in range(5):
        for j in range(5):
            c = intersection_matrix[4-j,i]
            if c != "##":
                ax.text(i+0.5, j+0.5, str(c), va='center', ha='center',fontsize=15)
            if i == 2 and j == 2:
                ax.text(i+0.5, j+0.5, 'BINGO', va='center', ha='center',fontsize=15)

    ax.set_xlim(min_val, max_val)
    ax.set_ylim(min_val, max_val)
    ax.minorticks_on()
    ax.tick_params(axis=u'x', which=u'major',length=0);

    #Pongo la palabra BINGO arriba y centrado
    labels = "BINGO"
    arange_labels = np.arange(len(labels))
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(arange_labels, minor=True)
        axis.set(ticks=arange_labels+0.5,ticklabels=labels)

    #Pongo el grid para separar los numeros y dar forma de tabla de bingo
    plt.grid(True,which='minor')

    #Guardo la imagen
    plt.savefig('tabla1.png')
    plt.close()

def text_to_png(text,width,height):
    img_text = Image.new('RGB', (width, height),(255,255,255))
    fnt = ImageFont.truetype('./font/Insanibc.ttf',font_size)
    d = ImageDraw.Draw(img_text)
    d.text((20, 20), text, font=fnt, fill=(0,0,0))
    return img_text
    #img_text.save("Hello.png")
