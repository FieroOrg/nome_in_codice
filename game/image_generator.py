from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random
from game.word import WordTable
from game import colorgame


class ImageGenerator():
    """Class description

    """

    def __init__(self):
        self.col_num = 5
        self.space_btw_cards = 30

    def image_spy(self, words):
        """

        :param words: list of Word
        :return: immagine (path??)
        """
        # not colored + hide found one
        with Image.open('../res/images/white_card.png') as img:
            img_w, img_h = img.size
            bg_width = self.col_num * (img_w + self.space_btw_cards) + self.space_btw_cards
            row_num = len(words)//self.col_num
            if len(words)%self.col_num != 0:
                row_num =+ 1
            bg_height = row_num* (img_h + self.space_btw_cards) + self.space_btw_cards
            # Image constructor: mode, size (width, height in pixels), color.
            background = Image.new('RGBA', (bg_width, bg_height), (255, 255, 255, 255))
            font = ImageFont.truetype("arial.ttf", 50)
            for word in words:
                img = Image.open('../res/images/white_card.png', 'r')
                draw = ImageDraw.Draw(img)

                # calculate where to place the word inside the white space of the card
                (word_width, baseline), (offset_x, offset_y) = font.font.getsize(word.name)
                # pixel number in which the white space in the card starts and ends
                start_pixel = 40
                end_pixel = 335
                available_space = end_pixel - start_pixel
                free_space = available_space - word_width
                # W, H: top left position of the word in the white space of the card
                W, H = (40 + (free_space // 2)), 142
                if word.revealed and word.color==colorgame.ColorGame.RED:
                    color = "red"
                elif word.revealed and word.color==colorgame.ColorGame.BLUE:
                    color = "blue"
                elif word.revealed and word.color==colorgame.ColorGame.WHITE:
                    color = "yellow"
                else:
                    color = "black"
                draw.text((W, H), word.name, fill=color, font=font)

                pos = words.index(word)
                offset = (pos%5 * img_w + (pos%5 + 1) * 30, (pos//5) * img_h + ((pos//5) + 1) * 30)  # pixel coordinates
                background.paste(img, offset)
            background.save('../res/images/grid.png')
        # return '/path/to/return'

    def image_master(self, words):
        """

        :param words: list of Word
        :return: immagine (path??)
        """
        # colored + hide found one
        return '/path/to/return'


words_table = WordTable()
words_table.generate_words("tag")
print(words_table.print_status())
# rivelo 10 parole a caso
i = 10
while i > 0:
    words_table.words[random.randint(0, 24)].reveal()
    i -= 1
img_gen = ImageGenerator()
img_gen.image_spy(words_table.words)
# if you need to do comparisons use colorgame.py (create method is_blue etc?)
# before creating a new method check it doesn't exist in word.py
