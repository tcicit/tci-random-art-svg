#!/usr/bin/env python3
"""
TCI Generativ Art Generator 2
Line Star
"""
import random
import tci_random_art_svg as tci_svg

default_config_file = 'config-line-star.yaml'
config_file = tci_svg.get_config_file(default_config_file )
config = tci_svg.read_file(config_file)

prefix = "line-star"
out_filename = tci_svg.output_file(prefix)

forground = tci_svg.read_file(config["general"]["forground_colors"])
forground_palette, text_froground = tci_svg.get_palette(forground)

# Grid-Dimension berechnen
width = (config["grid"]["rectwidth"] * config["grid"]["fields_x"]) 
height = (config["grid"]["rectwidth"] * config["grid"]["fields_y"])

fill = random.choice(forground[random.choice(list(forground))])

# berechnen wie viele linien gezeichnet werden
degree = config["stars"]["degree"]
number_segments =  int(360 / degree)
print (number_segments)

f = open(f'{out_filename}.svg', "w")

# generate SVG File
data = tci_svg.header(config)
f.write(data) 

if (config["stars"]["number_stars"] <= 1):
 
    data = f'<g>\n'
    f.write(data) 
    
    if (config["stars"]["change_color"] == "yes"):
            fill = random.choice(forground[random.choice(list(forground))])
            
    line_length = random.randint(config["stars"]["line_length_min"], config["stars"]["line_length_max"])
    strok_width = random.randint(config["stars"]["strok_width_min"], config["stars"]["strok_width_max"])

    x1 = width / 2           # Startpunkt festlegen
    y1 = height / 2          # Startpunkt festlegen
    
    for number in range(number_segments): # Stern zeichnen
        data = tci_svg.line(number, x1, y1, degree, line_length, fill, strok_width)
        f.write(data) 
        
    data = f'</g>\n'
    f.write(data)        
else:
    for j in range(config["stars"]["number_stars"]):
        data = f'<g>\n'
        f.write(data) 
        
        if (config["stars"]["change_color"] == "yes"):
                fill = random.choice(forground[random.choice(list(forground))])
                
        line_length = random.randint(config["stars"]["line_length_min"], config["stars"]["line_length_max"])
        strok_width = random.randint(config["stars"]["strok_width_min"], config["stars"]["strok_width_max"])

        x1 = random.randint(0, width)          # Startpunkt festlegen
        y1 = random.randint(0, height)         # Startpunkt festlegen  
        
        for number in range(number_segments): # Stern zeichnen
            data = tci_svg.line(number, x1, y1, degree, line_length, fill, strok_width)
            f.write(data) 
            
        data = f'</g>\n'
        f.write(data)        

# ----------------------------------------
# Paletten 
if config["note"]["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption( 
                                    config["grid"]["fields_y"], 
                                    config["grid"]["rectheight"], config["grid"]["rectwidth"], 
                                    config["grid"]["rectheight"], 
                                    forground_palette, 
                                    text_froground
    )
    
    f.write(data) 

data = tci_svg.footer()
f.write(data) 
f.close()

tci_svg.generate_files(config, out_filename)
