#!/usr/bin/env python3
"""
TCI Art Generator 2
The program creates a random image from geometric elements. 
The output is generated as an SVG file.

Autor: Thomas Cigolla, 16.02.2021
Version: 0.002
---------------------------------------------------------------
Requirements: 
Directory for Output Files (./output)
python 3.19.xxx

----------------------------------------------------------------
Aufteilung des Rechteckes für Dreieck (polygon)
  
  0,0   | 50,0   | 100,0
  ------|--------|--------
  0,50  | 50,50  | 100,50
  ------|--------|--------
  0,100 | 50,100 | 100,100 



"""
import random
import uuid
import tci_random_art_svg as tci_svg

config = tci_svg.read_file('config-trinagle.yaml')
forground = tci_svg.read_file(config["general"]["forground_colors"])
background = tci_svg.read_file(config["general"]["background_colors"])


# init
i = 0
j = 0
rectx = 0
recty = 0

# out_filename = "./output/my_file" 
run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')
out_filename = f'./output/triangle-{run_id}'


forground_palette, text_froground = tci_svg.get_palette(forground)
background_palette, text_background = tci_svg.get_palette(background)

f = open(f'{out_filename}.svg', "w")

# generate SVG File
data = tci_svg.header(config)
f.write(data) 

for i in range(config["grid"]["fields_y"]):
    for j in range(config["grid"]["fields_x"]):

        arguments1 = {"palette": background_palette,
                      "fill" : config["rect"]["background_fill"],
                      "rotate": "no",
                      "transform": "no",
                      "stroke_fill": "no"
                     }
        
        # draw Background    
        data = tci_svg.rect2(rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], **arguments1)
        f.write(data) 
        
        ori =  random.randrange(8)
        
        if ori == 0:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data)  
        elif ori == 1:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette) 
            f.write(data) 
        elif ori == 2:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 3:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 4:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 5:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 6:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 7:
            data = tci_svg.triangle(ori, rectx, recty, forground_palette)
            f.write(data) 

        else:
            print ("Ups")
       
        
        rectx += config["grid"]["rectwidth"]

    rectx = 0
    recty += config["grid"]["rectwidth"]
       
# Paletten 
if config["note"]["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption(f, 
                                    config["grid"]["fields_y"], 
                                    recty,
                                    config["grid"]["rectwidth"], 
                                    config["grid"]["rectheight"], 
                                    forground_palette, 
                                    background_palette, 
                                    text_froground, 
                                    text_background)
    f.write(data) 

data = tci_svg.footer()
f.write(data) 
f.close()

print("Elements: ", i+1, j+1)

tci_svg.generate_files(config, out_filename)
