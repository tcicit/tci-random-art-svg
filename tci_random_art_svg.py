"""
Modul for TCI Generativ Art Generator 2
Autor: Thomas Cigolla
Date: 16.06.2022
Version: 0.1
"""
import random
import numpy as np
import json
import yaml
import math
import cairosvg
import pathlib
from datetime import datetime


def read_file(file_name):
  
    ext = pathlib.Path(file_name).suffix[1:]

    with open(file_name, 'r') as file:
        if (ext == "yaml"):
            data = yaml.safe_load(file)
        elif (ext == "json"):
            data = json.load(file)
        else:
            print("ups no valide file")
    file.close()
    return(data)


def get_palette(colors):
    palette = random.choice(list(colors))
    data = colors[palette]
    text = palette

    return data, text


def header(config):
    rectwidth = config["grid"]["rectwidth"]
    fields_x = config["grid"]["fields_x"]
    fields_y = config["grid"]["fields_y"]

    if config["grid"]["background_color_fill"]:
        bg_fill = config["grid"]["background_color_fill"]

    if (config["general"]["date"] == "yes"):
        now = datetime.today().isoformat()


    if config["note"]["show_palette"] == "yes":
        h = rectwidth*fields_y + 500
        w = rectwidth*fields_y + 500
    else:
        h = rectwidth*fields_y
        w = rectwidth*fields_y

    data = f"""<svg xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1" 
            baseProfile="full"
            width="{rectwidth*fields_x}" height="{h}"
            viewBox="0 0 {rectwidth*fields_x} {w}">
            <title>{config["general"]["titel"]}</title>
            <desc>{config["general"]["describtion"]}</desc>
            <autor>{config["general"]["autor"]}</autor>
            <date>{now}</date>
            <license>{config["general"]["license"]}</license>\n

            <rect x="0" y="0" width="{w}" height="{h}" fill="{bg_fill}" />\n
            """

    return(data)


def footer():
    data = "</svg>"
    return(data)


def line(number, x1, y1, degree, line_length, color_palette, strok_width):

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    angel = number * degree

    x2 = round((line_length * math.cos(math.radians(angel))), 2)
    y2 = round((line_length * math.sin(math.radians(angel))), 2)

    x2 = x2 + x1
    y2 = y2 + y1

    data = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke:{fill};stroke-width:{strok_width};stroke-linecap:round"/>\n'
    return(data)


def rect(rectx, recty, rectwidth, rectheight, color_palette, trans):

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    data = f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{fill}" {trans}/>\n'
    return(data)


def rect2(rectx, recty, rectwidth, rectheight, **kwargs):
    ''' 
    generates svg rectangle object
    '''
    parameters = ""

    # Background and Forground Fill
    if ((kwargs["fill"]) == "palette"):
        parameters += f'fill="{random.choice(kwargs["palette"])}" '
    elif (type(kwargs["palette"]) == str and kwargs["palette"] != "no" ):
        parameters += f'fill="{kwargs["palette"]}" '
    else:    
        parameters += f'fill="none" '

    # Stroke Fill and width
    if ((kwargs["stroke_fill"]) == "palette"):
        parameters += f'stroke="{random.choice(kwargs["stroke_palette"])}" '
        parameters += f'stroke-width="{kwargs["stroke_width"]}" '
    elif (type(kwargs["stroke_fill"]) == str) and (kwargs["stroke_fill"] != "no"):
        parameters += f'stroke= {kwargs["stroke_palette"]} '
        parameters += f'stroke-width=" {kwargs["stroke_width"]}" '
    else:    
        parameters += f'stroke="none" '

    if (kwargs["transform"] == "yes"):
        rotate = random.randrange(kwargs["transform_range_0"], kwargs["transform_range_1"])
        parameters += f'transform="rotate({rotate}, {kwargs["center_x"]}, {kwargs["center_y"]})" '
    
    if (kwargs["rotate"] == "yes"):
        parameters += f'transform="rotate({kwargs["rotate_angle"]}, {kwargs["center_x"]}, {kwargs["center_y"]})" '
 
    parameters = parameters[:-1]
    data = f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" {parameters} />\n'
    return(data)

def circle(circle_r, rectx, recty, rectwidth, rectheight, color_palette):
    cx = rectx + rectwidth / 2
    cy = recty + rectheight / 2

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    data = f'<circle cx="{cx}" cy="{cy}" r="{circle_r}" fill="{fill}"/>\n'
    return(data)


def write_svgarc(color_palette, xcenter, ycenter, r, startangle, endangle):

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    if startangle > endangle:
        raise ValueError("startangle must be smaller than endangle")

    if endangle - startangle < 360:
        large_arc_flag = 0
        radiansconversion = np.pi/180.
        xstartpoint = xcenter + r*np.cos(startangle*radiansconversion)
        ystartpoint = ycenter - r*np.sin(startangle*radiansconversion)
        xendpoint = xcenter + r*np.cos(endangle*radiansconversion)
        yendpoint = ycenter - r*np.sin(endangle*radiansconversion)

        # If we want to plot angles larger than 180 degrees we need this
        if endangle - startangle > 180:
            large_arc_flag = 1

        p = f'<path d="M {xstartpoint} {ystartpoint} A {r} {r} 0 {large_arc_flag} 0 {xendpoint} {yendpoint} L {xcenter} {ycenter} Z"/>\n'
        data = f'<g stroke="none" fill="{fill}" >' + p + '</g>\n'

    else:
        data = f'<circle cx="{xcenter}" cy="{ycenter}" r="{r}" fill="{fill}"/>\n'

    return(data)


def print_titel(texty, text_title, text_palette):
    data = f'<text x="0" y="{texty}" style="font: bold 30px sans-serif;">{text_title} ({text_palette})</text>\n'
    return(data)


def print_palette(recty, rectwidth, rectheight, color_palette, rectx):

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    for i in range(len(color_palette)):
        if i == 0:
            data = f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{color_palette[i]}"/>\n'
        else:
            data += f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{color_palette[i]}"/>\n'

        data += f'<text x="{rectx+ 20}" y="{recty+120}" style="font: 12px sans-serif;">{color_palette[i]}</text>\n'
        rectx += rectwidth

    return(data)


def show_palette_desciption(fields_y, recty, rectwidth, rectheight, forground_palette, background_palette, text_froground, text_background):
    text_title = "Forground Palette"
    texty = rectheight * fields_y + 120
    data = print_titel(texty, text_title, text_froground)
    data += "\n"

    recty = rectheight * fields_y + 150
    data += print_palette(recty, rectwidth, rectheight,
                          forground_palette, rectx=0)
    data += "\n"

    text_title = "Background Palette"
    texty = rectheight * fields_y + 320
    data += print_titel(texty, text_title, text_background)
    data += "\n"

    recty = rectheight * fields_y + 350
    data += print_palette(recty, rectwidth, rectheight,
                          background_palette, rectx=0)

    return(data)




def triangle(triangle_type, rectx, recty, color_palette):
    """        
    Aufteilung des Rechteckes für Dreieck (polygon)
    
    0,0   | 50,0   | 100,0
    ------|--------|--------
    0,50  | 50,50  | 100,50
    ------|--------|--------
    0,100 | 50,100 | 100,100 
    """

    if (type(color_palette) == list):
        fill = random.choice(color_palette)
    else:
        fill = color_palette

    if (triangle_type == 0):
        data = f'<polygon points="0,0 100,0 0,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 1):
        data = f'<polygon points="100,0 100,100 0,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 2):
        data = f'<polygon points="0,0 100,0 100,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 3):
        data = f'<polygon points="0,0 100,100 0,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 4):
        data = f'<polygon points="0,0 100,50 0,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 5):
        data = f'<polygon points="0,50 100,0 100,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 6):
        data = f'<polygon points="0,100 50,0 100,100" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    elif (triangle_type == 7):
        data = f'<polygon points="0,0 50,100 100,0" fill="{fill}" transform="translate({rectx},{recty})"/>\n'
    else:
        print("missing Trinagle Type")

    return(data)


def generate_files(config, out_filename):
    if config["general"]["make_png"] == "yes":
        cairosvg.svg2png(
            url=f'{out_filename}.svg', write_to=f'{out_filename}.png')

    if config["general"]["make_pdf"] == "yes":
        cairosvg.svg2pdf(
            file_obj=open(f'{out_filename}.svg', "rb"), write_to=f'{out_filename}.pdf')

    # Save Parameter
    stream = open(f'{out_filename}.yaml', 'w')
    yaml.dump(config, stream, indent=4)    # Write a YAML representation of data to 'document.yaml'.
    stream.close()
     