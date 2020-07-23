# ReportCovid19Itabira

>  This directory have a script that does a report with data from Itabira city.

---

### Overview

The pdf examples of the latest version can be found in folder `examples`.

> Note that besides this informations, you also need two files in `others` directory. Those files are used to generate the graph of confirmed cases over time and 

### Downloads

This section needs to be executed by system.

```bash
# Download tool to generate pdf Report
pip3 -q install reportlab > /dev/null

# Download tools to login and get spreadsheet
pip3 -q install oauth2client > /dev/null
pip3 -q install wheel > /dev/null
pip3 -q install gspread > /dev/null

# Download tools to threat data
pip3 -q install pandas > /dev/null
pip3 -q install numpy > /dev/null

# Download tools to plot
pip3 -q install matplotlib > /dev/null
pip3 -q install seaborn > /dev/null

# Download font that will be used
mkdir fonts
curl https://fonts.google.com/download?family=Montserrat -so font.zip
unzip -qq font.zip -d fonts && rm font.zip

# Download Images
#     IMG (Imgur keeps images if 1 view per six months)
#     https://i.imgur.com/vKgu7bE.png --> WomanBlue
#     https://i.imgur.com/GcsTCOp.png --> Default Itabira's logo
wget http://www.clker.com/cliparts/2/a/Q/D/P/J/woman-orange-hi.png -qO girl.png
wget https://i.imgur.com/OnzjeAY.png -qO boy.png
mkdir img && mv boy.png img/boy.png && mv girl.png img/girl.png
wget https://i.imgur.com/ef1IAWY.jpg -qO img/logo.png
# It's need fontawesome also, so downlod it in site
# https://use.fontawesome.com/releases/v5.13.1/fontawesome-free-5.13.1-desktop.zip
# And then convert into ttf
# https://anyconv.com/otf-to-ttf-converter/

# Create folder to store pdf and logs
mkdir pdfs/
mkdir logs/
```

## Running

```bash
# To run, just execute
python3 coronaplotsv2.py
```
