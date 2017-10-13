import yaml
from PIL import Image, ImageFont, ImageDraw
import argparse

parser = argparse.ArgumentParser(description='Draws Value Stream Map.')
parser.add_argument('input', type=str, help='Input file path')
parser.add_argument('output', type=str, help='Output file path')
args = parser.parse_args()

stream = open(args.input, "r")
steps = yaml.load(stream)

size = len(steps)*200

im = Image.new('RGB', (size,200), (255,255,255))
dr = ImageDraw.Draw(im)

fnt = ImageFont.truetype('SourceCodePro-Regular.ttf', 20)
attributes_font = ImageFont.truetype('SourceCodePro-Regular.ttf', 14)
start = 50
value = 0
lead = 0
ca = 1
for i, step in enumerate(steps):
    if i != len(steps) - 1:
        arrow = (
            (start+100, 40),
            (start+150, 40),
            (start+150, 25),
            (start+200, 50),
            (start+150, 75),
            (start+150, 60),
            (start+100, 60),
            (start+100, 40)
        )
        dr.polygon(arrow, outline="black")
    dr.rectangle(((start,25),(start+100,75)), outline="black")
    dr.text((start+10, 35), step["name"], font=fnt, fill=(0,0,0))
    dr.text((start+10, 80), "LT: {}".format(step["lead"]), font=attributes_font, fill=(0,0,0))
    lead += step["lead"]
    dr.text((start+10, 100), "VA: {}".format(step["value"]), font=attributes_font, fill=(0,0,0))
    value += step["value"]
    ca_text = "%C/A: {:.2%}".format(step["accepted"]/step["completed"])
    dr.text((start+10, 120), ca_text, font=attributes_font, fill=(0,0,0))
    ca *= step["accepted"]/step["completed"]
    start += 200


dr.text((10, 140), "LT: {}".format(lead), font=attributes_font, fill=(0,0,0))
dr.text((10, 160), "VA: {}".format(value), font=attributes_font, fill=(0,0,0))
dr.text((10, 180), "%C/A: {:.2%}".format(ca), font=attributes_font, fill=(0,0,0))

im.save(args.output)