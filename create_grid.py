from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('images/white_card.png', 'r')
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 50)
text = "carta1"
W, H = 120, 142  # first card position
draw.text((W,H), text, fill="black", font=font)

img_w, img_h = img.size
# white background
background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
bg_w, bg_h = background.size
background.paste(img)
offset = (img_w + 10, 0)
background.paste(img, offset)
background.save('images/grid.png')