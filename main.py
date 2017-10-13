import yaml
from PIL import Image, ImageFont, ImageDraw

filename = "examples/development.yml"
stream = open(filename, "r")
steps = yaml.load(stream)

size = len(steps)*200

im = Image.new('RGB', (size,100), (255,255,255))
dr = ImageDraw.Draw(im)

start = 50
for step in steps:
    dr.rectangle(((start,25),(start+100,75)), outline="black")
    start += 200

im.save("rectangle.png")