# Random Art Generator 2

Diese Scriptsamlung diehnt dazu durch verschieden Algoritmen einfache zufällige SVG Bilder zu erzeigen.
Es können diverse Parameter in den Coonfig-Files beinflusst werden. Die Parameter sind meistens selbst erklärend (Dokumentation muss noch erstellt werden)

Zusätzlich zu den SVG-Files können auch PDF, PNG Dateien erzeugt werden. Bei jedem Durchgang werden auch noch die Parameter gesichert.
Unter dem Verzeichnis sind zwei Files (Forground, Background) mit Farbpaletten, dadurch können zfällig erzeugte Farben erstellt werden.

* tci-random_art_svg-line-star.py   -> erzeugt zufällig verteilte Sterne
* tci-random_art_svg-only-circle.py -> erzeugt zufällig verteilte Keise
* tci-random_art_svg-only-lines.py -> erzeugt zufallig verteilte Linien 
* tci-random_art_svg-rect-rotate-fall.py -> erzeugt ein Bild bei dem es scheint als ob die Rechtecke von oben nach unten fallen.
* tci-random_art_svg-rect-rotate-shrink.py -> erzeugt Rechtecke die auch ineinander geschachtelt sein können
* tci-random_art_svg-rect-tri-cir.py -> erzeugt ein Bild bei dem die Rechtecke diagonal geteilt sind und einen Kreis beinhalten
* tci-random_art_svg-semicircle.py -> erzeugt ein Bild bei dem die Rechtecke mit Halbkeisen gefüllt sind
* tci-random_art_svg-trinagle.py -> erzeugt ein Bild mit verschieden ausgereichteten Dreiecken
* tci-random_art_svg.py -> Modul mit den standart Funktuionen 

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

### Installation cairosvg unter Linux


    Update the package index:

    # sudo apt-get update

    Install cairosvg deb package:

    # sudo apt-get install cairosvg






## Beispiele







Zusätzlich Beispiele unter art-cigolla.ch
