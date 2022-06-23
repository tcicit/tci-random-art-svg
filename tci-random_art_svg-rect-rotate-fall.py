#!/usr/bin/env python3
"""
TCI Generativ Art Generator 2
Rectangle
Rotate
30.04.2022
"""
import random
import tci_random_art_svg as tci_svg

default_config_file = 'config-rect-rotate-fall.yaml'
config_file = tci_svg.get_config_file(default_config_file )
config = tci_svg.read_file(config_file)

prefix = "rect-rotate-fall"
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
rotate = 0
center_x = 0
center_y = 0
arguments2 = { "rotate_angle": 0 }

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

        if (i != 0):
            rotate = random.uniform(-3-i/4, 3+i/4) * i

        # forground
        arguments2["fill"]              = config["rect"]["forground_fill"]
        arguments2["palette"]           = forground_palette
        arguments2["stroke_fill"]       = config["rect"]["stroke_fill"]
        arguments2["stroke_palette"]    = forground_palette
        arguments2["stroke_width"]      = config["rect"]["stroke_width"]
        arguments2["transform"]         = config["rect"]["transform_random"]
        arguments2["rotate"]            = config["rect"]["rotate"]
        arguments2["transform_range_0"] = config["rect"]["transform_random_randrange"][0]
        arguments2["transform_range_1"] = config["rect"]["transform_random_randrange"][1]
        arguments2["center_x"]          = center_x
        arguments2["center_y"]          = center_y

                     
        if (config["rect"]["rotate"] == "yes"):
            if (arguments2["rotate_angle"] < 360):
                arguments2["rotate_angle"] += rotate
            else: 
                arguments2["rotate_angle"] = 0

        data = tci_svg.rect2(rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], **arguments2)
        f.write(data)

        rectx += config["grid"]["rectwidth"]

        center_x = rectx + (config["grid"]["rectwidth"] / 2)
        center_y = recty + (config["grid"]["rectheight"] / 2)

    rectx = 0
    recty += config["grid"]["rectheight"]
    center_x = rectx + (config["grid"]["rectwidth"] / 2)
    center_y = recty + (config["grid"]["rectheight"] / 2)

    trans1 = f'transform="rotate({rotate}, {center_x}, {center_y})"'

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

print("Elements: ", i+1, j+1)

tci_svg.generate_files(config, out_filename)
