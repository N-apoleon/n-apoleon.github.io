#!/usr/bin/env python3
"""Zeichnet die App-Icons (1024 x 1024 Master) nach Apples Icon-Richtlinien.

Aufruf (aus dem Repo-Hauptordner):
    python3 _werkzeuge/icons_zeichnen.py            # alle Icons neu zeichnen
    python3 _werkzeuge/icons_zeichnen.py notenrechner

Danach für jedes geänderte Tool:  python3 _werkzeuge/icon_einbetten.py <tool>
(Das Start-Icon der Übersichtsseite liegt unter ./icon-1024.png und wird mit
 `python3 _werkzeuge/icon_einbetten.py .` eingebettet.)

Regeln (siehe CLAUDE.md, Abschnitt Icons):
- ein einfaches, sofort erkennbares Motiv, KEIN Text, keine Zahlen, keine Buchstaben
- Fläche komplett gefüllt (kein Rand, keine Transparenz, KEINE eigenen runden Ecken – iOS maskiert selbst)
- weicher Verlauf von oben (heller) nach unten (dunkler) in einer iOS-Systemfarbe
- Motiv in Weiß, wichtigste Form etwa 55–65 % der Fläche, mittig
- immer in 1024 zeichnen, nur herunterskalieren
Neue Tools: eine neue Funktion nach dem Muster unten anlegen und in ICONS eintragen.
Benötigt: Pillow
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

S = 1024

# iOS-Systemfarben als Verläufe (oben, unten) – pro Tool eine andere Farbe wählen
VERLAEUFE = {
    "blau":   ((64, 156, 255), (0, 88, 214)),
    "orange": ((255, 184, 64), (255, 128, 0)),
    "gruen":  ((76, 217, 100), (36, 160, 70)),
    "indigo": ((125, 122, 255), (72, 66, 200)),
    "pink":   ((255, 95, 130), (225, 30, 80)),
    "teal":   ((90, 200, 230), (20, 140, 180)),
    "grau":   ((142, 142, 147), (90, 90, 96)),
}


def verlauf(name):
    top, bot = VERLAEUFE[name]
    im = Image.new("RGB", (S, S))
    d = ImageDraw.Draw(im)
    for y in range(S):
        t = y / (S - 1)
        d.line([(0, y), (S, y)], fill=tuple(round(top[i] * (1 - t) + bot[i] * t) for i in range(3)))
    return im


def schatten(im, box, radius, off=18, blur=28, alpha=70):
    sh = Image.new("L", (S, S), 0)
    ImageDraw.Draw(sh).rounded_rectangle([box[0], box[1] + off, box[2], box[3] + off], radius=radius, fill=alpha)
    im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))


def notenrechner():
    """Blatt mit drei Aufgabenzeilen, das letzte Punktefeld ist ausgewählt (Häkchen)."""
    im = verlauf("blau")
    sheet = (262, 190, 762, 834)
    schatten(im, sheet, 72)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(sheet, radius=72, fill=(255, 255, 255))
    for i in range(3):
        y = 300 + i * 175
        d.rounded_rectangle((330, y + 18, 330 + [200, 240, 170][i], y + 58), radius=20, fill=(214, 222, 234))
        d.rounded_rectangle((330, y + 82, 330 + [130, 160, 110][i], y + 104), radius=11, fill=(233, 238, 245))
        d.rounded_rectangle((566, y, 694, y + 120), radius=34, fill=(0, 122, 255) if i == 2 else (224, 236, 255))
    pts = [(598, y + 62), (622, y + 86), (664, y + 38)]
    d.line(pts, fill=(255, 255, 255), width=20, joint="curve")
    for cx, cy in pts:
        d.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=(255, 255, 255))
    return im


def gesamtnote():
    """Ring, aufgeteilt in 40 % (weiß) und 60 % (halbtransparent weiß) – steht für gewichtete Teilnoten."""
    im = verlauf("orange").convert("RGBA")
    ring = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    r = ImageDraw.Draw(ring)
    box, w, gap = (212, 212, 812, 812), 150, 7
    r.arc(box, start=-90 + gap, end=-90 + 144 - gap, fill=(255, 255, 255, 255), width=w)
    r.arc(box, start=-90 + 144 + gap, end=270 - gap, fill=(255, 255, 255, 140), width=w)
    sh = ring.split()[3].point(lambda a: min(a, 90)).filter(ImageFilter.GaussianBlur(24))
    im.paste((150, 60, 0, 255), (0, 18), sh)
    im.alpha_composite(ring)
    return im.convert("RGB")


def start():
    """Übersichtsseite: 2 x 2 abgerundete Kacheln (App-Raster)."""
    im = verlauf("grau")
    d = ImageDraw.Draw(im)
    farben = [(0, 122, 255), (255, 149, 0), (52, 199, 89), (88, 86, 214)]
    k, gap = 250, 64
    x0 = (S - (2 * k + gap)) // 2
    for i, c in enumerate(farben):
        x = x0 + (i % 2) * (k + gap)
        y = x0 + (i // 2) * (k + gap)
        schatten(im, (x, y, x + k, y + k), 64, off=12, blur=18, alpha=60)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((x, y, x + k, y + k), radius=64, fill=(255, 255, 255))
        d.rounded_rectangle((x + 70, y + 70, x + k - 70, y + k - 70), radius=30, fill=c)
    return im


ICONS = {"notenrechner": notenrechner, "gesamtnote": gesamtnote, ".": start}

if __name__ == "__main__":
    ziele = sys.argv[1:] or list(ICONS)
    for name in ziele:
        ICONS[name]().save(Path(name) / "icon-1024.png", optimize=True)
        print(f"{name}/icon-1024.png gezeichnet")
