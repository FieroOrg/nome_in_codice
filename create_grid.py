from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('images/white_card.png', 'r')
draw = ImageDraw.Draw(img)
img_w, img_h = img.size

cards_number = 5
space = 30
bg_width = cards_number * (img_w + space) + space
bg_height = 1700
# Image constructor: mode, size (width, height in pixels), color.
background = Image.new('RGBA', (bg_width, bg_height), (255, 255, 255, 255))

font = ImageFont.truetype("arial.ttf", 50)
word_list = ["carta1", "carta2", "carta3", "carta4", "carta5"]
W, H = 120, 142  # first card position
bg_w, bg_h = background.size

for word in word_list:
    img = Image.open('images/white_card.png', 'r')  # controlla se è da chiudere
    draw = ImageDraw.Draw(img)
    draw.text((W,H), word, fill="black", font=font)
    pos = word_list.index(word)
    offset = (pos * img_w +(pos+1)*30, 30)  # controlla cosa sono: pixel?
    background.paste(img, offset)

background.save('images/grid.png')