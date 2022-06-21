#!/usr/bin/env python3
"""
TCI Random Art Generator 3
Rectangle 
Trinagle
Circle
30.04.2022
"""
import random
import uuid
import tci_random_art_svg as tci_svg

config = tci_svg.read_file('config-rect-tri-cir.yaml')
forground = tci_svg.read_file(config["general"]["forground_colors"])
background = tci_svg.read_file(config["general"]["background_colors"])

# init
rectx = 0
recty = 0

# out_filename = "./output/my_file" 
run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')
out_filename = f'./output/rect-tri-cir_{run_id}'

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
        
        if (config["triangle"]["use_triangle"] == "yes"):
            ori =  random.randrange(0, 2)
                
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
                
        if (config["circle"]["use_circle"] == "yes"):
            
            circle_radius = random.randrange(config["circle"]["random_shrink_randrange"][0], config["circle"]["random_shrink_randrange"][1]) 
            data = tci_svg.circle(circle_radius, rectx, recty, config["grid"]["rectwidth"], config["grid"]["rectheight"], forground_palette)
            f.write(data) 
       
        rectx += config["grid"]["rectwidth"]

    rectx = 0
    recty += config["grid"]["rectheight"]
       

print ("Elements: ", i+1, j+1)
   
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

tci_svg.generate_files(config, out_filename)
