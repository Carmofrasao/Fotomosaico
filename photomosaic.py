#!/usr/bin/env python3
from PIL import Image
import sys 
import os
from colorthief import ColorThief

if len(sys.argv) < 6:
    print('./photomosaic foto.jpg base_fotos caract.txt <R> <N>')
    exit(1)

if sys.argv[1] == '-h':
    print('./photomosaic foto.jpg base_fotos caract.txt <R> <N>')
    exit(1)

foto = sys.argv[1]
base = sys.argv[2]
caracteristicas = sys.argv[3]
repetidas = int(sys.argv[4])
tam_matriz = int(sys.argv[5])

# Quanto mais imagens no banco, menor pode ser o valore da distancia
distancia = 74

tiles = []

# O arquivo de caracteristicas deve ser gerado com o script caract.py
caract = open(caracteristicas, 'r')
for caracteristica in caract:
    tile = []
    tile.append( caracteristica.split(': ')[0])
    tile.append(tuple(map(int, (caracteristica.split(': ')[1].strip().strip('(').strip(')').split(', ')))))
    tiles.append(tile)

base_fotos = []
foto = Image.open(foto)
for root, dirs, files in os.walk(base):
    for file in files:
        base_fotos.append(Image.open(base+"/"+file))

W = foto.size[0]
R = foto.size[1]
JW = int(W/tam_matriz)
JR = int(R/tam_matriz)

saida = Image.new('RGB', (W, R), (255,255,255))

for r in range(0, R, JR):
    for w in range(0, W, JW):
        foto.crop((w, r, w+JW, r+JR)).save("tmp.jpg")
        
        color_thief = ColorThief("tmp.jpg")
        dominant_color = color_thief.get_color(quality=1)
        
        # Para testar se existem tiles para todas as partes da imagem principal, use a flag!
        # flag = 0
        for tile in tiles:
            if (tile[1][0] >= dominant_color[0] - distancia and tile[1][0] <= dominant_color[0] + distancia) and (tile[1][1] >= dominant_color[1] - distancia and tile[1][1] <= dominant_color[1] + distancia) and (tile[1][2] >= dominant_color[2] - distancia and tile[1][2] <= dominant_color[2] + distancia):
                # flag = 1
                tileOK = tile[0]
                if repetidas == 0:
                    tiles.remove(tile)
                if len(tiles) == 0:
                    print("Acabou as tiles, faz o L")
                    exit(1)
                break
        # if flag == 0:
        #     print("Nenhuma imagem foi encontrada para esse trecho")
        # else: 
        #     print("Imagem encontrada!")
        n_image = int(tileOK.strip('image').strip('.jpg'))
        saida.paste(base_fotos[n_image-1], (w, r))

saida.save("saida.png", "PNG")
saida.show()
