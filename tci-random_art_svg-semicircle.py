#!/usr/bin/env python3
"""
TCI Generativ Art Generator 2
Semicircle
Rotate
30.04.2022
"""
import random
import tci_random_art_svg as tci_svg

default_config_file = 'config-semicircle.yaml'
config_file = tci_svg.get_config_file(default_config_file )
config = tci_svg.read_file(config_file)

prefix = "semicircle"
out_filename = tci_svg.output_file(prefix)

forground = tci_svg.read_file(config["general"]["forground_colors"])
background = tci_svg.read_file(config["general"]["background_colors"])

forground_palette, text_froground = tci_svg.get_palette(forground)
background_palette, text_background = tci_svg.get_palette(background)

f = open(f'{out_filename}.svg', "w")

# generate SVG File
data = tci_svg.header(config)
f.write(data) 

# init
rectx = 0
recty = 0
radiusx = 0
radiusy = 0
rect_half = config["grid"]["rectwidth"] / 2

for i in range(config["grid"]["fields_y"]):
    for j in range(config["grid"]["fields_x"]):
        
        # backround
        arguments1 = {"palette": background_palette,
                      "fill" : config["rect"]["background_fill"],
                      "rotate": "no",
                      "transform": "no",
                      "stroke_fill": "no"
                     }

        data = tci_svg.rect2(rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], **arguments1)
        f.write(data)

        # select pattern
        if config["circle"]["semicircle_only"] == "yes":
            ori =  random.randrange(2,10)
        else:    
            ori =  random.randrange(10)
        
        if ori == 0:
            data = tci_svg.circle(config["circle"]["circle_radius"], rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
            f.write(data) 
        elif ori == 1:
            data = tci_svg.circle(config["circle"]["circle_radius"], rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
            f.write(data) 
            data = tci_svg.circle(config["circle"]["circle_radius"] - 20, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
            f.write(data) 
        elif ori == 2:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=90, endangle=270)
            f.write(data) 
        elif ori == 3:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=0, endangle=180)
            f.write(data) 
        elif ori == 4:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=180, endangle=360)
            f.write(data) 
        elif ori == 5:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=270, endangle=450)
            f.write(data) 
        elif ori == 6:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=90, endangle=270)
            f.write(data) 
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half-20, startangle=90, endangle=270)
            f.write(data) 
        elif ori == 7:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=0, endangle=180)
            f.write(data) 
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half-20, startangle=0, endangle=180)
            f.write(data) 
        elif ori == 8:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=180, endangle=360)
            f.write(data) 
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half-20, startangle=180, endangle=360)
            f.write(data) 
        elif ori == 9:
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half, startangle=270, endangle=450)
            f.write(data) 
            data = tci_svg.write_svgarc(forground_palette, xcenter=rectx+rect_half, ycenter=recty+rect_half, r=rect_half-20, startangle=270, endangle=450)
            f.write(data) 
        else:
            print ("ups")
        
        rectx += config["grid"]["rectwidth"]

    rectx = 0
    recty += config["grid"]["rectheight"]
       
 
# Paletten 
if config["note"]["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption(
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
