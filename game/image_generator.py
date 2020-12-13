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

    def __init__(self, master):
        self.col_num = 5
        self.space_btw_cards = 30
        self.font = ImageFont.truetype("arial.ttf", 25)
        self.master = master

    def image_spy(self, words):
        """

        :param words: list of Word objects
        :param master: boolean for distinguish spies from masters
        :return: image path
        """
        background = self.create_bg('../res/images/cards/white_card.png', words)
        if self.master:
            for word in words:
                pos = words.index(word)
                # choose the color of the card
                if word.color == colorgame.ColorGame.RED:
                    path_card = '../res/images/cards/red_card.png'
                elif word.color == colorgame.ColorGame.BLUE:
                    path_card = '../res/images/cards/blue_card.png'
                elif word.color == colorgame.ColorGame.WHITE:
                    path_card = '../res/images/cards/white_card.png'
                else:
                    path_card = '../res/images/cards/black_card.png'
                background = self.add_card_to_bg(background, path_card, word, pos)
        else:
            for word in words:
                pos = words.index(word)
                background = self.add_card_to_bg(background, '../res/images/cards/white_card.png', word, pos)
                # substitute path with correct word property
        background.save('../res/images/grid.png')
        return '../res/images/grid.png'

    """
    This function creates the background of the image
    """
    def create_bg(self, img_path, words):
        with Image.open(img_path) as img:
            img_w, img_h = img.size

        # compute background width
        bg_width = self.col_num * (img_w + self.space_btw_cards) + self.space_btw_cards

        # compute background height
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
        (word_width, word_height), (offset_x, offset_y) = self.font.font.getsize(word.name)
        # coordinates of the white space
        x_left = 18
        x_right = 160
        y_up = 65
        y_down = 98
        # dimension of the white space
        white_space_width = x_right - x_left
        white_space_height = y_down - y_up
        # white space that remains free
        free_space_x = white_space_width - word_width
        free_space_y = white_space_height - 23
        # 23 and not word_height because sometimes it is 18 and sometimes it is 23
        # and then the words are on different planes and they suck
        # (maybe if there is a letter going down the height increases).
        # coordinates of the beginning of the word
        word_x_pos = x_left + (free_space_x // 2)
        word_y_pos = y_up + (free_space_y // 2)

        # choose the color of the text
        if self.master and word.color == colorgame.ColorGame.ASSASSIN:
            font_color = "white"
        else:
            font_color = "black"
        draw.text((word_x_pos, word_y_pos), word.name, fill=font_color, font=self.font)

        # top-left corner coordinates of the card in the background
        card_x = (pos % self.col_num) * img_w + (pos % self.col_num + 1) * self.space_btw_cards
        card_y = (pos // self.col_num) * img_h + ((pos // self.col_num) + 1) * self.space_btw_cards
        offset = (card_x, card_y)
        background.paste(img, offset)
        return background


words_table = WordTable()
words_table.generate_words("tag")
print(words_table.print_status())
# rivelo 10 parole a caso
i = 10
while i > 0:
    words_table.words[random.randint(0, 24)].reveal()
    i -= 1
img_gen = ImageGenerator(True)
img_gen.image_spy(words_table.words)
# if you need to do comparisons use colorgame.py (create method is_blue etc?)
# before creating a new method check it doesn't exist in word.py
