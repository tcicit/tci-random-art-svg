#!/usr/bin/env python3
"""
TCI Random Art Generator 3
only-circle
30.04.2022
"""
import random
import tci_random_art_svg as tci_svg

default_config_file = 'config-only-circle.yaml'
config_file = tci_svg.get_config_file(default_config_file )
config = tci_svg.read_file(config_file)

prefix = "only-circle"
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
                
        if (config["circle"]["number_inner_object"] <= 1):
            if (config["circle"]["random_radius"] == "yes"):
                circle_radius = random.randrange(config["circle"]["radius_random_randrange"]) 
                data = tci_svg.circle(circle_radius, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
                f.write(data) 
            else:
                circle_radius = config["grid"]["rectwidth"] - 5
                data = tci_svg.circle(circle_radius, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
                f.write(data) 
        else:
            circle_radius = config["circle"]["circle_radius"]
            for ii in range(config["circle"]["number_inner_object"]):
                if (config["circle"]["random_shrink"] == "yes"):
                
                    print (config["circle"]["random_shrink_randrange"])
                    shrink = random.randrange(config["circle"]["random_shrink_randrange"][0], config["circle"]["random_shrink_randrange"][1])
              
                    circle_radius -= shrink 
                    data = tci_svg.circle(circle_radius, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
                    f.write(data)                
                else:
                
                    data = tci_svg.circle(circle_radius, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
                    f.write(data) 
                
                    circle_radius -= config["circle"]["shrink"]
                
                print (circle_radius)
        
        rectx += config["grid"]["rectwidth"]

    rectx = 0
    recty += config["grid"]["rectheight"]
   
# Paletten 
if (config["note"]["show_palette"] == "yes"):
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

print ("Elements: ", i+1, j+1)

tci_svg.generate_files(config, out_filename)
