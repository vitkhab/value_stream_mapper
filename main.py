import yaml
from PIL import Image, ImageFont, ImageDraw

filename = "examples/development.yml"
stream = open(filename, "r")
steps = yaml.load(stream)

size = len(steps)*200

im = Image.new('RGB', (size,200), (255,255,255))
dr = ImageDraw.Draw(im)

fnt = ImageFont.truetype('SourceCodePro-Regular.ttf', 20)
attributes_font = ImageFont.truetype('SourceCodePro-Regular.ttf', 14)
start = 50
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
    dr.text((start+10, 100), "VA: {}".format(step["value"]), font=attributes_font, fill=(0,0,0))
    ca = "%C/A: {:.2%}".format(step["accepted"]/step["completed"])
    dr.text((start+10, 120), ca, font=attributes_font, fill=(0,0,0))
    start += 200

im.save("rectangle.png")