#!/usr/bin/env python3
"""
TCI Generativ Art Generator 2
Rectangle
Rotate
30.04.2022
"""
import random
import tci_random_art_svg as tci_svg

prefix = "rect-001"


default_config_file = f'config-{prefix}.yaml'
config_file = tci_svg.get_config_file(default_config_file )
config = tci_svg.read_file(config_file)

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
rectheight = config["grid"]["rectheight"]
rectwidth = config["grid"]["rectwidth"]
grid_length_x = config["grid"]["fields_x"] * config["grid"]["rectwidth"] 
grid_length_y = config["grid"]["fields_y"] * config["grid"]["rectheight"] 


while recty < grid_length_y:
    while  rectx < grid_length_x:

        arguments1 = {"palette": forground_palette,
                      "fill" : config["rect"]["background_fill"],
                      "rotate": "no",
                      "transform": "no",
                      "stroke_fill": "no"
                     }
    
        data = tci_svg.rect2(rectx, recty, rectwidth, rectheight, **arguments1)
        f.write(data)


        if (config["rect"]["use_rect_variants"] == "width" ):
            rectx += rectwidth
            rectwidth = config["grid"]["rectwidth"] + random.randrange(config["rect"]["rect_variants_x"][0],config["rect"]["rect_variants_x"][1]) 
        else:
            rectx += config["grid"]["rectwidth"]
         

    if (config["rect"]["use_rect_variants"] == "height" ):
        recty += rectheight
        rectheight = config["grid"]["rectheight"] + random.randrange(config["rect"]["rect_variants_y"][0],config["rect"]["rect_variants_y"][1]) 
    else:
        recty += config["grid"]["rectheight"]

    rectx = 0
  

# ----------------------------------------
# Paletten 
if config["note"]["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption( 
                                    config["grid"]["fields_y"], 
                                    config["grid"]["rectheight"], config["grid"]["rectwidth"], 
                                    config["grid"]["rectheight"], 
                                    forground_palette, 
                                    background_palette, 
                                    text_froground, 
                                    text_background)
    f.write(data) 

data = tci_svg.footer()
f.write(data)
f.close()

print ("generated")
tci_svg.generate_files(config, out_filename)
