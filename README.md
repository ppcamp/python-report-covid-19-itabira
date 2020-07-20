# ReportCovid19Itabira

>  This directory have a script that does a report with data from Itabira city.

---

### Overview

The pdf examples of the latest version can be found in folder `examples`.

### Worksheet structure

Worksheet columns:

| Important | Column Name                                          | Values                                                                         |
|:---------:|:----------------------------------------------------:|:------------------------------------------------------------------------------:|
|           | Carimbo de data/hora                                 | *                                                                              |
|           | Nome:                                                | *                                                                              |
| ★         | Sexo:                                                | F\|M                                                                           |
|           | Data de Nascimento:                                  | *                                                                              |
| ★         | Idade:                                               | AGES list                                                                      |
|           | É profissional da saúde?                             | *                                                                              |
|           | É profissional da segurança pública?                 | *                                                                              |
|           | Contato:                                             | *                                                                              |
|           | Endereço:                                            | *                                                                              |
| ★         | Bairro:                                              | *                                                                              |
|           | CEP:                                                 | *                                                                              |
|           | PSF de referência:                                   | *                                                                              |
|           | Data da notificação:                                 | *                                                                              |
|           | Nome da Unidade de Notificação:                      | *                                                                              |
|           | Há uma data dos sintomas?                            | *                                                                              |
|           | Início dos sintomas:                                 | *                                                                              |
|           | Data de previsão de coleta:                          | *                                                                              |
|           | Sintomas:                                            | *                                                                              |
|           | Outros sintomas:                                     | *                                                                              |
|           | Data do recebimento:                                 | *                                                                              |
|           | Início do isolamento:                                | *                                                                              |
| ★         | Fatores de risco:                                    | DISEASES list                                                                  |
|           | Outros fatores de risco:                             | *                                                                              |
|           | Vínculo epidemiológico:                              | *                                                                              |
|           | Houve coleta?                                        | *                                                                              |
|           | Data da coleta:                                      | *                                                                              |
|           | Método:                                              | *                                                                              |
|           | Resultado primeiro teste:                            | *                                                                              |
|           | Data do Resultado:                                   | *                                                                              |
|           | Laboratório:                                         | *                                                                              |
|           | Houve coleta para retestagem 1?                      | *                                                                              |
|           | Data da nova coleta 1:                               | *                                                                              |
|           | Método na restestagem 1:                             | *                                                                              |
|           | Resultado Retestagem 1:                              | *                                                                              |
|           | Data do Resultado da restestagem 1:                  | *                                                                              |
|           | Laboratório da Retestagem 1:                         | *                                                                              |
|           | Houve coleta para retestagem 2?                      | *                                                                              |
|           | Data da nova coleta 2:                               | *                                                                              |
|           | Método na restestagem 2:                             | *                                                                              |
|           | Resultado Retestagem 2:                              | *                                                                              |
|           | Data do Resultado da restestagem 2:                  | *                                                                              |
|           | Laboratório da Retestagem 2:                         | *                                                                              |
|           | Houve coleta para retestagem 3?                      | *                                                                              |
|           | Data da nova coleta 3:                               | *                                                                              |
|           | Método na restestagem 3:                             | *                                                                              |
|           | Resultado Retestagem 3:                              | *                                                                              |
|           | Data do Resultado da restestagem 3:                  | *                                                                              |
|           | Laboratório da Retestagem 3:                         | *                                                                              |
|           | Houve coleta para retestagem 4?                      | *                                                                              |
|           | Data da nova coleta 4:                               | *                                                                              |
|           | Método na restestagem 4:                             | *                                                                              |
|           | Resultado Retestagem 4:                              | *                                                                              |
|           | Data do Resultado da restestagem 4:                  | *                                                                              |
|           | Laboratório da Retestagem 4:                         | *                                                                              |
| ★         | Selecione a situação:                                | CONFIRMADO\|OBITO EM INVESTIGAÇÃO \|SUSPEITO\|BAIXA PROBABILIDADE\| DESCARTADO |
|           | Data da Situação Atual:                              | *                                                                              |
|           | Observação:                                          | *                                                                              |
|           | Código E-SUS VE:                                     | *                                                                              |
| ★         | Escolha a situação do caso confirmado:               | INTERNADO\|ISOLAMENTO DOMICILIAR\| RECUPERADO\|ÓBITO                           |
|           | Data da situação do caso confirmado:                 | *                                                                              |
| ★         | Escolha a situação do caso descartado:               | OBITO\|*                                                                       |
|           | Data da situação do caso descartado:                 | *                                                                              |
| ★         | Está monitorado pela central de vigilância da saúde? | INTERNADO\|NÃO\|SIM                                                            |
|           | Data de previsão de término:                         | *                                                                              |
| ★         | Houve internação?                                    | NÃO\|SIM                                                                       |
| ★         | Hospital                                             | HNSD\|HMCC\|*                                                                  |
| ★         | Leito:                                               | CTI\|UTI\|ENFERMARIA\|*                                                        |
|           | Observação da internação:                            | *                                                                              |
|           | Data da internação:                                  | *                                                                              |
|           | Data da alta:                                        | *                                                                              |
|           | Qual o outro teste realizado?                        | *                                                                              |
|           | Data da coleta do outro teste:                       | *                                                                              |
|           | Laboratório do outro teste:                          | *                                                                              |
|           | Resultado:                                           | *                                                                              |
|           | Data do Resultado do outro teste:                    | *                                                                              |
|           | Latitude                                             | *                                                                              |
|           | Longitude                                            | *                                                                              |
| ★         | Semana epidemiológica                                | *                                                                              |

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
