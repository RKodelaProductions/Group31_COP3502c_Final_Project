# Shared settings for the whole Sudoku project.
# Agreed on by the team - do not change without telling everyone.

WIDTH = 540            # 9 cells x 60 px
CELL_SIZE = 60
BOARD_SIZE = 540       # board is the top 540 x 540 square
BUTTON_AREA = 90       # strip under the board for Reset / Restart / Exit
HEIGHT = BOARD_SIZE + BUTTON_AREA   # 630

THIN_LINE = 1
THICK_LINE = 4

BG_COLOR = (255, 255, 245)
LINE_COLOR = (0, 0, 0)
GIVEN_COLOR = (0, 0, 0)          # numbers the generator placed
USER_COLOR = (30, 80, 200)       # numbers the player entered
SKETCH_COLOR = (128, 128, 128)
SELECT_COLOR = (220, 0, 0)       # red outline on the selected cell
BUTTON_COLOR = (230, 140, 40)
BUTTON_TEXT_COLOR = (255, 255, 255)

VALUE_FONT_SIZE = 40
SKETCH_FONT_SIZE = 22
BUTTON_FONT_SIZE = 30
TITLE_FONT_SIZE = 60

REMOVED_CELLS = {"easy": 30, "medium": 40, "hard": 50}