# Random Art Generator 2

Diese Scriptsammlung dient dazu, durch verschieden Algorithmen einfache und zufällige SVG Bilder zu erzeigen. Es können diverse Parameter in den Config-Files beeinflusst werden. Die Parameter sind meistens selbst erklärend (Dokumentation muss noch erstellt werden)

Zusätzlich zu den SVG-Files können auch PDF, PNG Dateien erzeugt werden. Bei jedem Durchgang die verwendeten Parameter gesichert in einem eigenen File gesichert. Unter dem Verzeichnis sind zwei Files (Forground, Background) mit Farbpaletten, dadurch können zufällige erzeugte Farben erstellt werden. Die erzeugten Files werden unter dem Directory ./output abgelegt.

Zum Starten des Scriptes können folgende Parameter verwendet werden:

    -d / --default (benützt das im Script definierte Konfigurations-File)
    -c / --config <<FILENAME>> (mit diesem Parameter kann ein individuellse Konfigruations-File angegeben werden)

-----------------------------

This collection of scripts is used to create simple and random SVG images using different algorithms. Various parameters in the config files can be influenced. The parameters are mostly self-explanatory (documentation is still to be created).

In addition to SVG files, PDF, PNG files can be created. At each run the used parameters are saved in a separate file. Under the directory are two files (Forground, Background) with color palettes, so random generated colors can be created. The created files are stored in the directory ./output.

The following parameters can be used to start the script:

    -d / --default (uses the configuration file defined in the script)
    -c / --config <<FILENAME>> (with this parameter an individual configuration file can be specified)

-------------------------------

* tci-random_art_svg-line-star.py   -> erzeugt zufällig verteilte Sterne
* tci-random_art_svg-only-circle.py -> erzeugt zufällig verteilte Keise
* tci-random_art_svg-only-lines.py -> erzeugt zufallig verteilte Linien 
* tci-random_art_svg-rect-rotate-fall.py -> erzeugt ein Bild bei dem es scheint als ob die Rechtecke von oben nach unten fallen.
* tci-random_art_svg-rect-rotate-shrink.py -> erzeugt Rechtecke die auch ineinander geschachtelt sein können
* tci-random_art_svg-rect-tri-cir.py -> erzeugt ein Bild bei dem die Rechtecke diagonal geteilt sind und einen Kreis beinhalten
* tci-random_art_svg-semicircle.py -> erzeugt ein Bild bei dem die Rechtecke mit Halbkeisen gefüllt sind
* tci-random_art_svg-trinagle.py -> erzeugt ein Bild mit verschieden ausgereichteten Dreiecken
* tci-random_art_svg.py -> Modul mit den standart Funktuionen 
* tci-random_art_svg_rect-0001.py -> Verschieden grosse Rechtecke 


## Verwendete Python Module

uuid
random
numpy
json
yaml
math
cairosvg
pathlib
datetime

### Installation cairosvg unter Linux (Mint, Ubuntu)


    Update the package index:

    # sudo apt-get update

    Install cairosvg deb package:

    # sudo apt-get install cairosvg

## Beispiele  / Example


<<<<<<< HEAD
![Example 1](https://github.com/tcicit/tci-random-art-svg/blob/main/exam/semicircle-3098445a-f168-11ec-9f67-5195a8bc9375.png)
=======
![Example 1](https://github.com/tcicit/tci-random-art-svg/blob/main/examples/semicircle-3098445a-f168-11ec-9f67-5195a8bc9375.png)
>>>>>>> 52cfa666549c09631351ecc57b1e99fd3ce37a2b

![Example 2](https://github.com/tcicit/tci-random-art-svg/blob/main/examples/rect-rotate-1ce9c9cc-f151-11ec-9f67-5195a8bc9375.png)

![Example 3](https://github.com/tcicit/tci-random-art-svg/blob/main/examples/rect-rotate-29d7ccc4-f151-11ec-9f67-5195a8bc9375.png)

![Example 4](https://github.com/tcicit/tci-random-art-svg/blob/main/examples/only-circle_127538d4-f168-11ec-9f67-5195a8bc9375.png)


Zusätzlich Beispiele unter https://art-cigolla.ch
