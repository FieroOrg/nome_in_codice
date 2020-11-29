from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('images/white_card.png', 'r')
draw = ImageDraw.Draw(img)

# white background
background = Image.new('RGBA', (2000, 1500), (255, 255, 255, 255))

font = ImageFont.truetype("arial.ttf", 50)
word_list = ["carta1", "carta2", "carta3", "carta4", "carta5"]
W, H = 120, 142  # first card position
img_w, img_h = img.size
bg_w, bg_h = background.size

for word in word_list:
    img = Image.open('images/white_card.png', 'r')
    draw = ImageDraw.Draw(img)
    draw.text((W,H), word, fill="black", font=font)
    pos = word_list.index(word)
    # offset pdm style
    offset = (pos * img_w + (pos * img_w + 10)//9 +30, 30)
    background.paste(img, offset)

background.save('images/grid.png')