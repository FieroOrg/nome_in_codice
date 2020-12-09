from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random
from game.word import WordTable
from game import colorgame


class ImageGenerator:
    """
    A class to create an image from a list of Word objects
    """

    def __init__(self):
        self.col_num = 5
        self.space_btw_cards = 30
        self.font = ImageFont.truetype("arial.ttf", 50)

    def image_spy(self, words):
        """

        :param words: list of Word objects
        :return: image path
        """
        background = self.create_bg('../res/images/white_card.png', words)
        for word in words:
            pos = words.index(word)
            background = self.add_card_to_bg(background, '../res/images/white_card.png', word, pos)
        background.save('../res/images/grid.png')
        return '../res/images/grid.png'

    """
    This function creates the background of the image
    """
    def create_bg(self, img_path, words):
        with Image.open(img_path) as img:
            img_w, img_h = img.size

        bg_width = self.col_num * (img_w + self.space_btw_cards) + self.space_btw_cards

        row_num = len(words) // self.col_num
        if len(words) % self.col_num != 0:
            row_num = + 1
        bg_height = row_num * (img_h + self.space_btw_cards) + self.space_btw_cards

        # Image constructor: mode, size (width, height in pixels), color.
        background = Image.new('RGBA', (bg_width, bg_height), (255, 255, 255, 255))
        return background

    """
    This function add a card to the background
    """
    def add_card_to_bg(self, background, img_path, word, pos):
        """

        :param background: the background on which to add the card
        :param img_path: the path of the card to add
        :param word: the word to add
        :param pos: the position of the word in the list
        :return: the background with the new card
        """
        with Image.open(img_path) as img:
            img_w, img_h = img.size
            draw = ImageDraw.Draw(img)
        # calculate where to place the word inside the white space of the card
        (word_width, baseline), (offset_x, offset_y) = self.font.font.getsize(word.name)
        # pixel number in which the white space in the card starts and ends
        start_pixel = 40
        end_pixel = 335
        available_space = end_pixel - start_pixel
        free_space = available_space - word_width
        # x, y: top-left position of the word in the card white space according to the word's length
        x, y = (40 + (free_space // 2)), 142

        # choose the color of the card
        if word.revealed and word.color == colorgame.ColorGame.RED:
            color = "red"
        elif word.revealed and word.color == colorgame.ColorGame.BLUE:
            color = "blue"
        elif word.revealed and word.color == colorgame.ColorGame.WHITE:
            color = "gold"
        else:
            color = "black"

        draw.text((x, y), word.name, fill=color, font=self.font)

        # pixel coordinates in the background of the card top-left corner
        card_x = (pos % self.col_num) * img_w + (pos % self.col_num + 1) * self.space_btw_cards
        card_y = (pos // self.col_num) * img_h + ((pos // self.col_num) + 1) * self.space_btw_cards
        offset = (card_x, card_y)
        background.paste(img, offset)
        return background

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
