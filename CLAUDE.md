# CLAUDE.md – Tool-Sammlung (Noten-Tools & weitere Web-Apps fürs iPad)

> Diese Datei ist das Gedächtnis des Projekts. Lies sie vollständig, bevor du irgendetwas tust.
> Sie fasst alles zusammen, was bisher entschieden, gebaut und ausprobiert wurde (Stand: 31.10.2026),
> und beschreibt genau, wie du in diesem Repository arbeiten sollst.
> Halte sie aktuell: Jede neue Entscheidung, jedes neue Tool und jede Änderung an den Regeln gehört hier hinein.

---

## 1. Worum es geht

- **Was:** Eine wachsende Sammlung kleiner, eigenständiger Web-Tools (je eine HTML-Datei), die auf dem **iPad** wie echte Apps laufen: Vollbild, eigenes Icon auf dem Home-Bildschirm, offline-tauglich nach dem ersten Laden, Daten bleiben auf dem Gerät.
- **Für wen:** Für die Person, der dieses Repository gehört und die mit dir chattet (im Folgenden „Nutzer“). Der Nutzer beschreibt dir in normaler Sprache, was ein Tool können soll. **Du** baust es und testest es. Er lädt die fertigen Dateien hoch (siehe Abschnitt 5) und muss keinen Code verstehen. Sprich ihn mit „du“ an.
- **Erste Tools:** Zwei Rechner für Klausurbewertung im **Oberstufen-Notenpunktesystem (0–15 Punkte)**:
  1. `notenrechner/` – Klausur-Notenrechner (Aufgaben, frei in Blöcken gewichtbar)
  2. `gesamtnote/` – Gesamtnote aus gewichteten Teilnoten (z. B. mündlich/schriftlich, Inhalt/Sprache)
- **Wie es online kommt:** Über **GitHub Pages**. Jeder Ordner mit einer `index.html` hat eine eigene feste Adresse, die man in Safari öffnet und per „Zum Home-Bildschirm“ als App ablegt.

### Arbeitsweise mit dir (Claude) in einem Satz
Der Nutzer beschreibt → du fragst höchstens kurz nach, wenn etwas wirklich unklar ist → du baust nach der Vorlage und dem Design-System in dieser Datei → du testest → du lieferst die fertigen Dateien mit Hochlade-Anleitung (oder committest und pushst selbst, wenn du Repo-Zugriff hast, siehe Abschnitt 5) → du sagst in einfachen Worten, was neu ist.

---

## 2. Kommunikation mit dem Nutzer

- **Sprache:** Deutsch, freundlich, einfach. Gehe davon aus, dass **keine Programmierkenntnisse** vorhanden sind. Fachbegriffe (Commit, Branch, Pull Request) nur, wenn nötig, und dann kurz erklären.
- **Nicht nachfragen, was du selbst entscheiden kannst** (Farben, Layout, Dateinamen, technische Details). Fragen nur bei echten inhaltlichen Unklarheiten, z. B. Rechenregeln, Rundung, Notenschlüssel. Dann **eine** konkrete Frage mit Vorschlag („Soll ab ,5 aufgerundet werden? Das ist der Standard, den ich sonst nehme.“).
- **Nach jeder Änderung** kurz zurückmelden: was neu ist (2–4 Punkte), die Adresse des Tools, und ob er auf dem iPad etwas tun muss (z. B. App einmal ganz schließen und neu öffnen).
- **Keine langen Erklärungen über das, was du getan hast.** Ergebnis zuerst.
- Gibt er Feedback wie „mach die Eingabe leichter“ oder „schöner“, ist das ein Auftrag zum Umsetzen, nicht zum Nachfragen.

---

## 3. Repository-Struktur

```
/
├── CLAUDE.md                 ← diese Datei (Projektgedächtnis + Regeln)
├── README.md                 ← kurze Info für Menschen auf GitHub
├── .nojekyll                 ← GitHub Pages liefert Dateien unverändert aus (nicht löschen)
├── index.html                ← Übersichtsseite „Meine Tools“ (Liste aller Tools mit Icon)
├── icon-1024.png             ← Icon der Übersichtsseite (Master)
├── apple-touch-icon.png      ← Icon der Übersichtsseite (180 × 180)
├── notenrechner/
│   ├── index.html            ← das Tool (eine einzige, eigenständige Datei)
│   ├── icon-1024.png         ← Icon-Master 1024 × 1024
│   └── apple-touch-icon.png  ← Home-Bildschirm-Icon 180 × 180 (auch in index.html eingebettet)
├── gesamtnote/
│   └── … (gleicher Aufbau)
├── _vorlage/
│   └── index.html            ← Startpunkt für jedes neue Tool (Design-System + Meta-Tags)
└── _werkzeuge/
    ├── icons_zeichnen.py     ← zeichnet alle Icons als 1024er-Master (Pillow)
    └── icon_einbetten.py     ← erzeugt 180er-PNG und bettet Icon + Favicon in index.html ein
```

### Regeln zur Struktur
- **Ein Tool = ein Ordner = eine `index.html`.** Der Dateiname muss genau `index.html` heißen (klein geschrieben), sonst funktioniert die kurze Adresse `…/ordnername/` nicht.
- **Ordnernamen:** klein, ohne Umlaute und Leerzeichen, Bindestriche erlaubt (`vokabeltrainer`, `sitzplan`, `noten-statistik`).
- **Jede `index.html` ist komplett eigenständig:** alles CSS und JavaScript steht in der Datei, Icons sind als `data:`-URI eingebettet. Keine externen Bibliotheken, keine Google Fonts, keine CDNs. Grund: Die Datei soll auch allein funktionieren (z. B. offline in einer Viewer-App, siehe Abschnitt 9) und auf dem iPad schnell und ohne Netz starten.
- Das Design-System (CSS) ist deshalb **in jeder Datei kopiert**. Wenn du es verbesserst, übernimm die Änderung in **alle** Tools und in `_vorlage/index.html`, damit alles gleich aussieht.
- Ordner mit Unterstrich (`_vorlage`, `_werkzeuge`) sind Hilfsmittel, keine Tools. Sie erscheinen nicht in der Übersicht.

---

## 4. Veröffentlichung: GitHub Pages

### Einmalige Einrichtung (falls noch nicht geschehen – prüfe das zuerst)
1. Repository auf GitHub, Inhalt dieses Ordners im Hauptzweig `main`.
2. Auf GitHub: **Settings → Pages → Build and deployment → Source: „Deploy from a branch“ → Branch: `main`, Ordner: `/ (root)` → Save.**
3. Nach 1–2 Minuten ist die Seite erreichbar unter
   `https://<github-benutzername>.github.io/<repo-name>/`
   und jedes Tool unter `https://<github-benutzername>.github.io/<repo-name>/<ordner>/`.
4. Trage die echte Adresse unten in Abschnitt 12 („Projektdaten“) ein, sobald sie bekannt ist.

**Wichtig zu Sichtbarkeit:** Mit einem kostenlosen GitHub-Konto funktioniert GitHub Pages nur, wenn das Repository **öffentlich** ist. Der Code ist dann für jeden lesbar. Die Adresse ist aber nirgends verlinkt. Für private Repositorys mit Pages braucht man ein kostenpflichtiges GitHub-Konto. Das ist unkritisch, **solange niemals personenbezogene Daten ins Repository gelangen** (siehe Abschnitt 8).

### Nach jedem Push
- GitHub Pages braucht nach einem Push ungefähr **1–2 Minuten**, bis die neue Version online ist.
- Auf dem iPad kann die Home-Bildschirm-App kurz noch die alte Version zeigen. Lösung für den Nutzer: App im App-Umschalter ganz wegwischen und neu öffnen. Notfalls die Adresse einmal in Safari neu laden.

### Auf dem iPad als App einrichten (Anleitung für den Nutzer)
1. Adresse des Tools in **Safari** öffnen (nicht in einem anderen Browser).
2. Auf das **Teilen-Symbol** tippen (Quadrat mit Pfeil nach oben).
3. **„Zum Home-Bildschirm“** wählen, Name prüfen, „Hinzufügen“.
4. Ab jetzt das Tool über das neue Icon starten. Dann läuft es im **Vollbild ohne Adressleiste**.
- Jedes Tool einzeln hinzufügen. Die Übersichtsseite kann man zusätzlich hinzufügen.
- Gespeicherte Eingaben einer Home-Bildschirm-App sind **getrennt** von denen in Safari. Wird das Icon gelöscht, sind auch die dort gespeicherten Einstellungen weg.

---

## 5. Arbeitsweise: Wie Änderungen ins Repository kommen

Es gibt zwei Arbeitsmodi. **Stell zu Beginn fest, welcher gilt:** Hast du Zugriff auf das Repository (Dateien im Arbeitsordner, `git` funktioniert)? Dann gilt Modus B. Sonst gilt Modus A.

### Modus A – Chat ohne Repo-Zugriff (aktueller Standard)

Der Nutzer arbeitet mit dem kostenlosen Claude-Abo im normalen Chat. Claude Code mit GitHub-Anbindung gibt es erst ab dem Pro-Abo. Du kannst also **nicht** selbst committen oder pushen. Der Nutzer lädt die Dateien **von Hand** auf GitHub hoch. Deshalb:

- Der Nutzer hängt zu Beginn des Chats diese CLAUDE.md an, oft auch die aktuelle `index.html` des Tools, das geändert werden soll. **Arbeite immer auf der Datei, die er dir gibt.** Rekonstruiere keine Datei aus dem Gedächtnis. Fehlt die aktuelle Datei für eine Änderung, bitte ihn in einem Satz, sie anzuhängen. Dafür öffnet er sie auf GitHub, tippt auf „Raw“ und kopiert den Text, oder er lädt sie herunter.
- **Liefere immer komplette, fertige Dateien**, nie Ausschnitte, Diffs oder „ersetze Zeile X“. Der Nutzer ersetzt den ganzen Dateiinhalt.
  - Kannst du Dateien erzeugen (Datei-Erstellung/Code-Ausführung verfügbar): als Datei zum Herunterladen ausgeben, mit dem exakten Dateinamen (`index.html`).
  - Sonst: den kompletten Inhalt in **einem** Codeblock ausgeben.
- **Icons:** Das `apple-touch-icon` und das Favicon sind als `data:`-URI in der `index.html` eingebettet. Wenn du Code ausführen kannst, zeichne und bette die Icons mit den Skripten aus `_werkzeuge/` ein und liefere zusätzlich `apple-touch-icon.png` und `icon-1024.png` als Dateien. Kannst du das nicht, übernimm die bestehenden `<link rel="icon">`- und `<link rel="apple-touch-icon">`-Zeilen unverändert. Bei einem neuen Tool: Lass sie vorerst weg und sag dem Nutzer, dass das Icon nachgereicht wird.
- **Am Ende jeder Antwort mit Dateien** steht eine kurze Hochlade-Anleitung, genau für diese Änderung:
  1. Welche Datei(en), in welchen Ordner, z. B. „`notenrechner/index.html` ersetzen“ oder „neuen Ordner `sitzplan` anlegen“.
  2. Bei einer **bestehenden Datei**: auf GitHub die Datei öffnen → Stift-Symbol (Edit) → kompletten Inhalt löschen und neuen einfügen → „Commit changes…“ → als Beschreibung den Commit-Text eintragen, den du vorschlägst → „Commit changes“.
  3. Bei einer **neuen Datei bzw. einem neuen Ordner**: im Repo „Add file“ → „Create new file“ → als Namen `ordner/index.html` eintippen (der Schrägstrich legt den Ordner an) → Inhalt einfügen → „Commit changes“. Für Bilddateien (PNG): in den Ordner wechseln → „Add file“ → „Upload files“.
  4. Wenn sich die Übersicht ändert (neues Tool): auch die neue `/index.html` hochladen.
  5. Hinweis: Nach 1–2 Minuten ist die Änderung online, auf dem iPad die App einmal ganz schließen und neu öffnen.
- Schlage zu jeder Datei einen **Commit-Text** vor (Regeln siehe unten).
- Wenn sich Regeln, Tools oder Entscheidungen ändern, liefere auch die **aktualisierte CLAUDE.md** als komplette Datei mit. Der Nutzer lädt sie ebenfalls hoch, damit das Projektgedächtnis aktuell bleibt.
- Die Prüfschritte aus Abschnitt 10 führst du aus, soweit du Code ausführen kannst. Sonst prüfst du den Code sorgfältig von Hand: Klammern, IDs, Speicher-Schlüssel und Rechenbeispiele.
- Halte Dateien schlank. Im kostenlosen Abo sind Nachrichten begrenzt, unnötig lange Antworten kosten den Nutzer Kontingent. Liefere keine Datei, die sich nicht geändert hat.

### Modus B – Claude Code mit Repo-Zugriff (bei Pro-Abo oder höher)

- **Commit und Push gehören zu jeder abgeschlossenen Änderung dazu.** Der Nutzer möchte, dass du das selbst erledigst.
- **Ziel ist `main`**, denn nur `main` wird von GitHub Pages veröffentlicht.
  - Kannst du direkt nach `main` pushen: tu das.
  - Arbeitest du in einer Umgebung, die automatisch einen eigenen Branch anlegt (z. B. `claude/…`): pushe dorthin, **erstelle einen Pull Request nach `main`** und sag dem Nutzer in einem Satz, dass er ihn auf GitHub mit „Merge pull request“ bestätigen muss, damit die Änderung online geht. Wenn du die Berechtigung hast, den PR selbst zu mergen, und er das gewünscht hat, merge ihn selbst.
- **Commit-Nachrichten auf Deutsch**, kurz und konkret, im Imperativ:
  - `Notenrechner: Aufgaben per Antippen statt Tippen eingeben`
  - `Neues Tool: Sitzplan`
  - `Design: größere Tasten für Notenpunkte in allen Tools`
- Pro Thema ein Commit. Keine halbfertigen Stände pushen.
- **Niemals** einen GitHub-Token (Personal Access Token) im Chat erfragen oder in Dateien schreiben. Der Zugriff läuft über die GitHub-Verbindung von Claude. (Hinweis aus früherer Recherche: Andere KIs brauchen dafür einen Token. Bei dir ist das nicht nötig, und ein Token im Chat wäre ein Sicherheitsrisiko.)
- Vor dem Push: Prüfschritte aus Abschnitt 10 ausführen.

---

## 6. Design-System (Apple-Stil / iOS Human Interface Guidelines)

Ausdrücklicher Wunsch bei der Entstehung: Die Apps sollen **nach Apples Richtlinien** aussehen und sich so bedienen lassen. Alle Tools nutzen dasselbe Design-System. Die Referenz-Umsetzung steht in `_vorlage/index.html` und in den beiden bestehenden Tools.

### Grundprinzipien
- Sieht aus wie eine **iPad-Einstellungen-App**: großer fetter Titel oben, darunter **gruppierte Listen** („inset grouped“) auf hellgrauem Grund, abgerundete weiße Gruppen.
- **Systemschrift** (`-apple-system` / SF Pro), für große Zahlen **SF Rounded** (`ui-rounded`), für Rechenwege **SF Mono** (`ui-monospace`). Keine Webfonts.
- **Hell- und Dunkelmodus** automatisch nach iPad-Einstellung, mit den echten iOS-Systemfarben.
- **Touch first:** Jedes antippbare Element ist **mindestens 44 × 44 pt** groß.
- **Antippen statt Tippen:** Wo es eine überschaubare Auswahl gibt (z. B. Notenpunkte 0–15), werden Tasten angeboten, keine Textfelder. Das war ein ausdrücklicher Wunsch („Eingabe leichter machen“) und hat sich bewährt.
- **Ergebnis immer sichtbar:** Auf dem iPad im Querformat (≥ 880 px Breite) steht rechts eine Ergebnis-Spalte, die beim Scrollen stehen bleibt (`.side`, sticky). Schmaler: Ergebnis unter der Eingabe.
- Beim Antippen in Eingabefelder darf Safari **nicht hineinzoomen**: Eingabefelder haben mindestens 16 px Schriftgröße (ist im Basis-CSS geregelt).
- Inhalte respektieren die **Safe Area** (Statusleiste oben, Home-Balken unten, abgerundete Ecken).
- Wenig Dekoration. Keine Emojis als Gestaltungselement. Farbe nur mit Bedeutung.

### Farben (CSS-Variablen, in jeder Datei unter `:root`)
| Variable | Hell | Dunkel | Verwendung |
|---|---|---|---|
| `--bg` | `#f2f2f7` | `#000000` | Seitenhintergrund (systemGroupedBackground) |
| `--surface` | `#ffffff` | `#1c1c1e` | Gruppen/Zellen |
| `--fill` | `rgba(118,118,128,.12)` | `.24` | Tasten, Eingabefelder |
| `--fg` | `#000` | `#fff` | Text |
| `--muted` | `rgba(60,60,67,.6)` | `rgba(235,235,245,.6)` | Nebentext, Abschnittsüberschriften |
| `--line` | `rgba(60,60,67,.29)` | `rgba(84,84,88,.65)` | Trennlinien (Haarlinie) |
| `--accent` | `#007aff` | `#0a84ff` | Systemblau: Auswahl, Links, Hauptbutton |
| `--red` | `#ff3b30` | `#ff453a` | Löschen, Zurücksetzen |
| `--green` | `#34c759` | `#30d158` | Hinzufügen, gute Noten |
| `--warn` | `#c93400` | `#ff9f0a` | Warnhinweise (z. B. Gewichte ≠ 100 %) |
| `--c1 … --c6` | Blau, Orange, Grün, Pink, Indigo, Teal | jeweils Dunkel-Variante | Farbpunkte zur Unterscheidung von Gruppen/Blöcken |

Farben nie fest in Komponenten schreiben, immer über Variablen. Sonst bricht der Dunkelmodus.

### Bausteine (Klassen)
| Klasse | Bedeutung |
|---|---|
| `.app` | Außenrahmen mit Seitenabständen (Safe Area berücksichtigt) |
| `.nav` + `h1` + `.sub` | Großer Titel (34 pt, fett) + eine Zeile Erklärung |
| `.layout` > `.col` / `.col.side` | Zweispaltig ab 880 px (Inhalt links, Ergebnis rechts) |
| `.sec` > `.sec-h` / `.group` / `.sec-f` | Abschnitt: Überschrift in Großbuchstaben (13 pt grau), Gruppe, Fußnote |
| `.group` > `.cell` | Weiße abgerundete Gruppe mit Zeilen; Trennlinien entstehen automatisch |
| `.cell.sub` | Eingerückte Unterzeile (z. B. Aufgaben in einem Block) |
| `details.setup` | Ausklappbarer Einstellungsbereich (Zeile mit farbigem Symbol-Quadrat `.ico` und Pfeil `.chev`) |
| `input.plain` | Textfeld ohne Rahmen, direkt in der Zeile |
| `.pct` | kleines Zahlenfeld mit `%` dahinter |
| `.del` | roter Minus-Kreis (Zeile löschen) – wie im iOS-Bearbeitungsmodus, immer links |
| `.add` (in `button.linkcell`) | grüner Plus-Kreis + blauer Text „… hinzufügen“ |
| `button.linkcell` / `.linkcell.red` | Zeile als Button (blau) / destruktiv (rot) |
| `.btn-fill` | großer blauer Hauptbutton (50 pt hoch) |
| `.bar` | Verteilungsbalken (z. B. Gewichte) in den Gruppenfarben |
| `.cell.task` + `.task-h` + `.chips` | Eingabe-Karte mit 8-spaltigem Tastenraster; gewählte Taste `aria-pressed="true"` = blau |
| `.hero` / `.badge` / `.hero-t` / `.hero-s` | **Hauptergebnis** ganz oben in der Ergebnisgruppe: großes farbiges Feld mit der gerundeten Gesamtnote in Punkten, daneben „13 Punkte“ und klein „Note 1− · sehr gut“ |
| `.stats` / `.stat` / `.k` / `.big` | Zusatzwerte darunter, kleiner (Gesamtpunkte exakt, Gesamtprozent) |
| `.calc` | Rechenweg in Monospace, horizontal scrollbar |

### Bedienmuster
- **Löschen** einer Zeile: roter Minus-Kreis links. Die letzte verbleibende Zeile kann nicht gelöscht werden (Button deaktiviert).
- **Zurücksetzen**: roter Text-Button, erster Tipp ändert die Beschriftung zu „Zum Bestätigen erneut tippen“, zweiter Tipp innerhalb von 3 s setzt zurück. Keine `alert()`/`confirm()`-Dialoge.
- **Neue Zeile hinzufügen** setzt den Cursor direkt in das neue Namensfeld (markiert), damit man sofort umbenennen kann.
- Werte werden **sofort** gespeichert und neu berechnet, es gibt keinen „Speichern“-Button.
- Prozentfelder akzeptieren Komma und Punkt.

### Pflicht-Kopf jeder Tool-Datei (steht so in `_vorlage/index.html`)
```html
<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Tool-Name</title>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Kurzname">   <!-- Name unter dem Home-Icon, max. ~12 Zeichen -->
<meta name="application-name" content="Kurzname">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,…">
<link rel="apple-touch-icon" sizes="180x180" href="data:image/png;base64,…">
<style> … Design-System … </style>
</head>
```
- `apple-mobile-web-app-capable` sorgt für das Vollbild ohne Adressleiste (aus der ursprünglichen Recherche übernommen). `mobile-web-app-capable` ist die neuere Schreibweise, beide bleiben drin.
- Statusleiste: `default` (dunkle Schrift auf hellem Grund bzw. automatisch). Früher war `black-translucent` drin. Das wurde beim Umstieg auf den Apple-Stil ersetzt, weil die Statusleiste sonst über dem Inhalt liegt.
- `viewport-fit=cover` + die Safe-Area-Paddings im CSS sind Pflicht, sonst verschwindet Inhalt unter Statusleiste oder Home-Balken.

---

## 7. Icons (nach Apples Icon-Richtlinien)

- **Kein Text, keine Zahlen, keine Buchstaben** im Icon. Ein einfaches, sofort erkennbares Motiv.
- **Fläche komplett gefüllt**, keine Transparenz, **keine eigenen runden Ecken** (iOS schneidet die Form selbst zu).
- Hintergrund: weicher Verlauf (oben heller, unten dunkler) in **einer iOS-Systemfarbe**. Jedes Tool bekommt eine **eigene** Farbe, damit man es auf dem Home-Bildschirm sofort findet. Bisher vergeben: **Blau** = Notenrechner, **Orange** = Gesamtnote, **Grau** = Übersicht. Für neue Tools z. B. Grün, Indigo, Pink, Teal.
- Motiv in Weiß (gern mit einem Akzent in der Systemfarbe), mittig, etwa 55–65 % der Fläche, dezenter Schatten.
- Immer als **1024 × 1024**-Master zeichnen, nur herunterskalieren.

**Ablauf für ein neues Icon:**
1. In `_werkzeuge/icons_zeichnen.py` eine Funktion für das Tool anlegen (Muster: `notenrechner()`, `gesamtnote()`), in `ICONS` eintragen.
2. `python3 _werkzeuge/icons_zeichnen.py <ordner>` → erzeugt `<ordner>/icon-1024.png`.
3. `python3 _werkzeuge/icon_einbetten.py <ordner>` → erzeugt `apple-touch-icon.png` (180) und bettet Favicon (32) und Home-Icon (180) als `data:`-URI in `<ordner>/index.html` ein.
4. Icon ansehen (Bild öffnen). Prüfen: auch in klein (32 px) noch erkennbar?
- Pillow fehlt? `pip install pillow --break-system-packages`

Bestehende Icons: Notenrechner = weißes Blatt mit drei Aufgabenzeilen, letztes Punktefeld blau mit Häkchen, auf blauem Verlauf. Gesamtnote = weißer Ring, aufgeteilt 40 % (deckend) / 60 % (halbtransparent), auf orangem Verlauf. Übersicht = 2 × 2 weiße Kacheln mit farbigen Quadraten, auf grauem Verlauf.

---

## 8. Daten & Datenschutz

- Tools speichern Einstellungen und Eingaben **nur lokal auf dem Gerät** (`localStorage`). Es wird nichts an einen Server geschickt, es gibt kein Konto, keine Analyse und kein Tracking.
- **Jeder Schlüssel ist eindeutig pro Tool**, Schema `<ordnername>-v<nummer>`. Alle Tools liegen unter derselben Domain und teilen sich den Speicher, deshalb darf sich nichts überschneiden.
  - Ausnahme (historisch): Der Notenrechner nutzt `notenrechner-v2`, die Gesamtnote `gesamtnote-v1`. **Nicht umbenennen**, sonst sind die gespeicherten Einstellungen auf den Geräten weg.
- Ändert sich die Struktur der gespeicherten Daten: alte Daten lesen und umwandeln (Migration). Nur wenn das nicht geht: Versionsnummer erhöhen und dem Nutzer sagen, dass die Einstellungen einmal neu gemacht werden müssen.
- Jeder Zugriff auf `localStorage` steht in `try/catch`. Das Tool muss auch ohne gespeicherte Daten mit sinnvollen Startwerten funktionieren.
- **Niemals echte Schülerdaten** (Namen, Noten mit Namen, Klassenlisten) ins Repository schreiben, auch nicht als Beispiel. Das Repository ist öffentlich (siehe Abschnitt 4). Beispieldaten sind immer neutral („Aufgabe 1“, „Teil A“, „Inhalt“).
- Will der Nutzer Daten sichern oder auf ein anderes Gerät übertragen: Export/Import als Datei bzw. als kopierbarer Text anbieten. Keine Cloud.

---

## 9. Hintergrund: Wie man HTML-Tools aufs iPad bringt (Ergebnis der Recherche)

Diese Abwägung wurde vorab mit einer anderen KI recherchiert. Das Ergebnis:

| Weg | Bewertung |
|---|---|
| HTML-Datei in der **Dateien-App** antippen (Schnellvorschau) | Ungeeignet: Skripte (JavaScript) laufen dort nicht zuverlässig. |
| **Viewer-Apps** wie „HTML Viewer – Sitecase“ oder „Documents“ von Readdle | Funktioniert offline, ohne Internet. Sitecase hat einen Vollbildmodus. Gut als **Notlösung ohne Hochladen**. |
| Code-Editoren mit Live-Vorschau (Koder, Textastic) | Nur nötig, wenn man selbst am Code arbeiten will. Für den Nutzer nicht gedacht. |
| **GitHub Pages + „Zum Home-Bildschirm“** | **Gewählter Weg.** Echtes App-Gefühl (Vollbild, eigenes Icon), Updates kommen automatisch, kostenlos. |
| Netlify Drop / Vercel | Alternative zum schnellen Hochladen, wird hier nicht genutzt. |

Entscheidungen daraus:
- **Ein Repository mit Unterordnern** pro Tool (statt einem Repository pro Tool). Jedes Tool hat seine eigene Adresse und ein eigenes Home-Icon. Eine Übersichtsseite sammelt die Links.
- Dateien heißen `index.html`.
- Icons werden als **Apple Touch Icon (180 × 180 PNG)** hinterlegt. Zusätzlich sind sie in der HTML-Datei eingebettet, damit die Datei auch allein in einer Viewer-App ihr Icon hat.
- Zusammenarbeit mit der KI direkt im Repository: Claude ist mit GitHub verbunden, committet und pusht selbst. Die Token-Variante aus der Recherche wird bewusst **nicht** genutzt.

---

## 10. Neues Tool erstellen – Schritt für Schritt

Wenn der Nutzer ein neues Tool beschreibt:

1. **Verstehen.** Was soll rein, was soll rauskommen? Eine Rückfrage nur bei inhaltlichen Rechen- oder Fachregeln, die du nicht sicher ableiten kannst. Sonst sinnvolle Standards wählen und im Ergebnis kurz nennen.
2. **Ordner anlegen:** `cp -r _vorlage <neuer-ordner>` (Ordnername nach Abschnitt 3).
3. **Kopf anpassen:** `<title>` (2–4 Wörter, ein Name, keine Erklärung), `apple-mobile-web-app-title` und `application-name` (Kurzname ≤ 12 Zeichen).
4. **Bauen** mit den Bausteinen aus Abschnitt 6. Beispielinhalt der Vorlage ersetzen. `KEY` für `localStorage` eindeutig setzen.
   - Das Tool startet mit **realistischen Beispielwerten** (deutlich als Beispiel erkennbar), nie leer.
   - Zahlen im deutschen Format (`toLocaleString("de-DE")`, Komma als Dezimaltrenner).
   - Wenn gerechnet wird: einen **Rechenweg** anzeigen, damit man das Ergebnis nachprüfen kann.
5. **Icon** nach Abschnitt 7 zeichnen und einbetten.
6. **Übersicht ergänzen:** In `/index.html` zwischen `TOOLS-START` und `TOOLS-ENDE` einen Eintrag nach dem Muster der vorhandenen hinzufügen. Bei neuem Themengebiet einen neuen Abschnitt (`.sec`) mit eigener Überschrift anlegen.
7. **CLAUDE.md aktualisieren:** Tool in Abschnitt 11 beschreiben (Zweck, Bedienung, Rechenregeln, Speicher-Schlüssel, Icon-Farbe in Abschnitt 7).
8. **Prüfen** (alles muss bestehen):
   - JavaScript-Syntax: Skript aus der Datei extrahieren und `node --check` ausführen.
   - Im Browser öffnen (Playwright/Chromium ist meist vorhanden): keine Fehler in der Konsole. Je ein Screenshot in **820 × 1180** (iPad hoch), **1180 × 820** (iPad quer) und **390 × 844** (iPhone), jeweils hell und einmal dunkel. Ansehen: nichts abgeschnitten, kein seitliches Scrollen, Texte lesbar.
   - Rechenlogik mit 2–3 Beispielen von Hand nachrechnen.
9. **Veröffentlichen** nach Abschnitt 5: Modus A = komplette Dateien + Hochlade-Anleitung, Modus B = Commit + Push.
10. **Rückmeldung** an den Nutzer: was das Tool kann (kurz), Adresse, Hinweis „Zum Home-Bildschirm hinzufügen“.

Bei **Änderungen an bestehenden Tools** gelten 4, 8, 9, 10 entsprechend. Gespeicherte Daten auf den Geräten müssen erhalten bleiben (Abschnitt 8).

---

## 11. Die bestehenden Tools im Detail

### Gemeinsame Notenlogik (Oberstufe, Notenpunkte)

| Punkte | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | 1+ | 1 | 1− | 2+ | 2 | 2− | 3+ | 3 | 3− | 4+ | 4 | 4− | 5+ | 5 | 5− | 6 |
| Wort | sehr gut | | | gut | | | befriedigend | | | ausreichend | | | mangelhaft | | | ungenügend |

- Eingabe pro Aufgabe/Teilnote: **0–15 Notenpunkte**, per Antippen (Raster mit 16 Tasten, 8 pro Reihe). Die 0 ist bewusst dabei.
- **Gesamtpunkte (exakt)** = gewichtete Summe, angezeigt mit 2 Nachkommastellen „x,xx / 15“.
- **Gesamtnote** = Gesamtpunkte **kaufmännisch gerundet auf ganze Notenpunkte (ab ,5 aufrunden)**, maximal 15.
- **Wichtigste Information = gerundete Gesamtnote in Punkten.** Ausdrücklicher Wunsch: Nach der Eingabe muss man zuerst sehen „14 Punkte“ (bei exakt 14,3). Deshalb steht sie ganz oben im Ergebnis als großes farbiges Feld mit der Punktzahl. Schulnote (z. B. „1“), Wort, exakte Punkte und Prozent sind Zusatzinfos und werden kleiner darunter angezeigt. Diese Rangfolge in allen Noten-Tools beibehalten.
- **Gesamtprozent** = exakte Gesamtpunkte / 15 × 100, eine Nachkommastelle.
- Farbe des Notenfelds: ≥ 10 Punkte grün, 7–9 blau, 4–6 orange, < 4 rot.
- Ergeben die eingestellten Gewichte nicht 100 %, wird **anteilig hochgerechnet** (normalisiert). Es erscheint ein Warnhinweis, und im Rechenweg steht „(Gewichte auf 100 % hochgerechnet)“.
- Gewichte mit 0 % oder Blöcke ohne Aufgaben zählen nicht.

### 11.1 `notenrechner/` – Klausur-Notenrechner
- **Zweck:** Eine Klausur besteht aus Aufgaben. Aufgaben werden in **Blöcken** zusammengefasst, jeder Block hat ein Gewicht in % der Gesamtnote.
- **Rechenregel:** Blockpunkte = **Durchschnitt** der Aufgabenpunkte im Block. Gesamtpunkte = Σ (Blockpunkte × Blockgewicht).
  - Beispiel Standard: Teil A (40 %) = Aufgabe 1 + 2, Teil B (60 %) = Aufgabe 3. A1 = 10, A2 = 11, A3 = 12 → Teil A Ø 10,5 × 0,4 = 4,20; Teil B 12 × 0,6 = 7,20; Summe 11,40 → **11 Punkte (2)**, 76,0 %.
- **Einrichtung** (ausklappbar, „Klausur einrichten“): Blöcke anlegen, umbenennen, gewichten, löschen. Aufgaben pro Block hinzufügen, umbenennen, löschen. Verteilungsbalken. Buttons „Block hinzufügen“, „Gewichte gleich verteilen“, „Auf Standard zurücksetzen“. Ein neuer Block bekommt automatisch das noch fehlende Gewicht bis 100 %.
- **Eingabe:** pro Block eine Gruppe, pro Aufgabe ein Tastenraster 0–15, daneben „Gewicht je Aufgabe in %“ und die gewählte Note.
- **Speicher:** `localStorage["notenrechner-v2"]` = `{ blocks: [ { id, name, w, tasks: [ { id, name, v } ] } ] }`
- **Icon:** blau, Blatt mit Häkchen. Kurzname „Notenrechner“.

### 11.2 `gesamtnote/` – Gesamtnote ausrechnen
- **Zweck:** Gesamtnote aus zwei oder mehr **Teilnoten** mit eigenem Gewicht (z. B. mündlich/schriftlich oder Inhalt/Sprache). Reihenfolge und Namen frei.
- **Rechenregel:** Gesamtpunkte = Σ (Teilnote × Gewicht).
  - Beispiel Standard: Inhalt 40 % = 10, Sprache 60 % = 12 → 4,00 + 7,20 = 11,20 → **11 Punkte (2)**, 74,7 %.
- **Einrichtung** („Gewichtung“, beim Start aufgeklappt): Teilnoten hinzufügen, umbenennen, gewichten, löschen. Verteilungsbalken, „Gleich verteilen“, „Auf Standard zurücksetzen“.
- **Speicher:** `localStorage["gesamtnote-v1"]` = `{ items: [ { id, name, w, v } ] }`
- **Icon:** orange, Ring 40/60. Kurzname „Gesamtnote“.

### Entstehungsgeschichte (wichtig, um Wünsche richtig einzuordnen)
1. Erste Version: 3 Aufgaben à 15 **Rohpunkte**, A1 + A2 = 40 %, A3 = 60 %, Ausgabe Prozent + Punkte, Note nach **IHK-Schlüssel**. → Verworfen. Gewünscht ist das **Gymnasium-Notenpunktesystem 0–15**.
2. Umstellung auf Notenpunkte. Eingabe per **Antippen** statt Zahlenfeld („Eingabe ein bisschen leichter“) → kam sehr gut an, bleibt so.
3. Notenrechner wurde **parametrierbar**: ausklappbarer Bereich mit Blöcken, Gewichten, beliebig vielen Aufgaben (für andere Klausuren).
4. Zweites Tool **Gesamtnote** für Teilnoten (mündlich/schriftlich, Inhalt 40 % / Sprache 60 %).
5. iPad-Optimierung: Vollbild-Meta-Tags, eingebettete Icons.
6. Komplette Umgestaltung **nach Apples Richtlinien** (iOS-Look, Systemschrift, gruppierte Listen, Icons ohne Text).
7. Umzug in dieses GitHub-Repository mit Übersichtsseite, Vorlage und Icon-Werkzeugen.
8. Ergebnisbereich umgebaut: Die gerundete Gesamtnote in Punkten ist jetzt das große Hauptergebnis. Vorher stand im farbigen Feld die Schulnote, und die Punkte standen klein darunter. Das war nicht gewünscht.

### Offene Punkte / mögliche nächste Schritte
- Echte GitHub-Adresse in Abschnitt 12 eintragen, sobald Pages eingerichtet ist.
- Rundungsregel bestätigen lassen. Manche Schulen bzw. Fachkonferenzen runden anders, z. B. werden Teilnoten schon vorher gerundet oder es wird immer abgerundet. Aktuell gilt: Nur das Endergebnis wird gerundet, ab ,5 auf.
- Mögliche Wünsche, die naheliegen (nicht ungefragt bauen, aber vorschlagen, wenn es passt): Rohpunkte je Aufgabe mit Umrechnung in Notenpunkte über einen Prozent-Schlüssel, mehrere gespeicherte Klausur-Vorlagen, Klassen-Durchlauf (mehrere Schüler nacheinander ohne Namen, z. B. „Nr. 1, 2, 3“) mit Notenspiegel, Export als Text.

---

## 12. Projektdaten (bitte ausfüllen/aktualisieren)

- GitHub-Benutzername: _noch eintragen_
- Repository-Name: _noch eintragen_ (Vorschlag: `tools`)
- Basis-Adresse: `https://<benutzername>.github.io/<repo>/`
- Tools:
  - Klausur-Notenrechner → `…/notenrechner/`
  - Gesamtnote → `…/gesamtnote/`

---

## 13. Kurzcheckliste für jede Sitzung

- [ ] CLAUDE.md gelesen, Projektdaten (Abschnitt 12) bekannt?
- [ ] Arbeitsmodus festgestellt (Abschnitt 5: A = Chat ohne Repo-Zugriff, B = Claude Code)?
- [ ] Ist GitHub Pages schon eingerichtet? Wenn nicht: den Nutzer Schritt für Schritt durch Abschnitt 4 führen.
- [ ] Änderung nach Design-System und Regeln umgesetzt?
- [ ] Gespeicherte Daten auf den Geräten bleiben erhalten?
- [ ] Prüfschritte (Abschnitt 10, Punkt 8) bestanden?
- [ ] Übersicht `/index.html` und diese CLAUDE.md aktualisiert?
- [ ] Modus A: komplette Dateien + Hochlade-Anleitung + Commit-Text geliefert? Modus B: committet, gepusht (bzw. PR erstellt)?
- [ ] Dem Nutzer die Adresse genannt?
