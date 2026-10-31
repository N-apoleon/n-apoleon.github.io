#!/usr/bin/env python3
"""Bettet das App-Icon eines Tools in dessen index.html ein.

Aufruf (aus dem Repo-Hauptordner):
    python3 _werkzeuge/icon_einbetten.py notenrechner

Erwartet: <tool>/icon-1024.png  (quadratisch, 1024 x 1024, ohne Transparenz, ohne abgerundete Ecken)
Erzeugt:  <tool>/apple-touch-icon.png (180 x 180)
Ersetzt:  in <tool>/index.html die href-Werte von
          <link rel="icon" ...> (32 x 32) und <link rel="apple-touch-icon" ...> (180 x 180)
          durch eingebettete data:-URIs, damit die Datei auch allein (ohne Bilddateien) funktioniert.
Benötigt: Pillow  (pip install pillow --break-system-packages)
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image


def data_uri(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def main(tool: str) -> None:
    folder = Path(tool)
    master = Image.open(folder / "icon-1024.png").convert("RGB")
    if master.size != (1024, 1024):
        sys.exit(f"icon-1024.png muss 1024 x 1024 sein, ist aber {master.size}")
    touch = master.resize((180, 180), Image.LANCZOS)
    fav = master.resize((32, 32), Image.LANCZOS)
    touch.save(folder / "apple-touch-icon.png", optimize=True)

    html_path = folder / "index.html"
    html = html_path.read_text(encoding="utf-8")
    html, n1 = re.subn(r'(<link rel="icon"[^>]*href=")[^"]*(")', lambda m: m.group(1) + data_uri(fav) + m.group(2), html, count=1)
    html, n2 = re.subn(r'(<link rel="apple-touch-icon"[^>]*href=")[^"]*(")', lambda m: m.group(1) + data_uri(touch) + m.group(2), html, count=1)
    if not (n1 and n2):
        sys.exit("In index.html fehlen <link rel=\"icon\"> oder <link rel=\"apple-touch-icon\"> (siehe _vorlage/index.html).")
    html_path.write_text(html, encoding="utf-8")
    print(f"Icon in {html_path} eingebettet, {folder/'apple-touch-icon.png'} erzeugt.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Aufruf: python3 _werkzeuge/icon_einbetten.py <tool-ordner>")
    main(sys.argv[1])
