from PIL import Image

img = Image.open('images/white_card.png', 'r')

img_w, img_h = img.size
# white background
background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
bg_w, bg_h = background.size
background.paste(img)
offset = (img_w + 10, 0)
background.paste(img, offset)
background.save('images/grid.png')