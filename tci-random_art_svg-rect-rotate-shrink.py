#!/usr/bin/env python3
"""
TCI Generativ Art Generator 2
Rectangle
Rotate
30.04.2022
"""
import random
import uuid
import tci_random_art_svg as tci_svg

config = tci_svg.read_file('config-rect-rotate-shrink.yaml')
forground = tci_svg.read_file(config["general"]["forground_colors"])
background = tci_svg.read_file(config["general"]["background_colors"])

# out_filename = "./output/my_file" 
run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')
out_filename = f'./output/rect-rotate-{run_id}'

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
         
        arguments1 = {"palette": background_palette,
                      "fill" : config["rect"]["background_fill"],
                      "rotate": "no",
                      "transform": "no",
                      "stroke_fill": "no"
                     }
        
        # draw Background    
        data = tci_svg.rect2(rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], **arguments1)
        f.write(data) 
        
        arguments2 = {"rotate_angle":  0 }
        # inner elements
        for ii in range(config["rect"]["number_inner_object"]):
            x = config["rect"]["shrink_x"] * ii
            y = config["rect"]["shrink_y"] * ii
            xx = x * 2
            yy = y * 2
            center_x = rectx + (config["grid"]["rectwidth"] / 2)
            center_y = recty + (config["grid"]["rectheight"] / 2)
            
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
             
            if config["rect"]["rotate"] == "yes":
                if arguments2["rotate_angel"] < 360:
                    arguments2["rotate_angle"] += config["rect"]["rotate_angle"]
                else: 
                    arguments2["rotate_angle"] = 0
                
            # Draw inner element
            data = tci_svg.rect2(rectx+x, recty+y, config["grid"]["rectwidth"]-xx, config["grid"]["rectheight"]-yy, **arguments2)
            f.write(data)

            if (config["circle"]["use_circle"] == "yes"):
                circle_radius = (config["grid"]["rectwidth"]-xx) / 2
                data = tci_svg.circle(circle_radius, rectx+x, recty+y, config["grid"]["rectwidth"]-xx, config["grid"]["rectheight"]-yy, forground_palette)
                f.write(data) 
        
        rectx += config["grid"]["rectwidth"]

    rectx = 0
    recty += config["grid"]["rectheight"]
       
print ("Elements: ", i+1, j+1)
   
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

tci_svg.generate_files(config, out_filename)

