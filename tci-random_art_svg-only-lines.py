
"""
TCI Generativ Art Generator 2
Rectangle
Autor: Thomas Cigolla
Date: 16.06.2022
Version: 0.1
"""

import random
import uuid
import tci_random_art_svg as tci_svg

config = tci_svg.read_file('config-only-lines.yaml')
forground = tci_svg.read_file(config["general"]["forground_colors"])
background = tci_svg.read_file(config["general"]["background_colors"])

#out_filename = "./output/my_file" 
run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')
out_filename = f'./output/only-lines-{run_id}'

forground_palette, text_froground = tci_svg.get_palette(forground)

# Grid-Dimension berechnen
width = (config["grid"]["rectwidth"] * config["grid"]["fields_x"]) 
height = (config["grid"]["rectwidth"] * config["grid"]["fields_y"])

fill = random.choice(forground[random.choice(list(forground))])

f = open(f'{out_filename}.svg', "w")

# generate SVG File
data = tci_svg.header(config)
f.write(data) 

for i in range(config["line"]["number_lines"]): # Linie zeichnen

    if (config["line"]["change_color"] == "yes"):
        fill = random.choice(forground[random.choice(list(forground))])
        
    line_length = random.randint(config["line"]["line_length_min"], config["line"]["line_length_max"])
    strok_width = random.randint(config["line"]["strok_width_min"], config["line"]["strok_width_max"])

    x1 = random.randint(0-line_length, width)          # Startpunkt festlegen
    y1 = random.randint(0-line_length, height)         # Startpunkt festlegen  

    degree = random.randint(config["line"]["degree_min"], config["line"]["degree_max"])
    number = 1    
    
    data = tci_svg.line(number, x1, y1, degree, line_length, fill, strok_width)
    f.write(data) 

# ----------------------------------------
# Paletten 
if config["note"]["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption( 
                                    config["grid"]["fields_y"], 
                                    config["grid"]["rectheight"], config["grid"]["rectwidth"], 
                                    config["grid"]["rectheight"], 
                                    forground_palette, 
                                    text_froground)
    f.write(data) 

data = tci_svg.footer()
f.write(data) 
f.close()

print (i+1)
tci_svg.generate_files(config, out_filename)

