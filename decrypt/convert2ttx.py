from fontTools.ttLib import TTFont

font = TTFont('fontello.woff2')
font.saveXML('fontello.ttx')