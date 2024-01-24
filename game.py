import displayio
import terminalio
from adafruit_display_text import label
game_group = displayio.Group()
axe = displayio.OnDiskBitmap("axe/axe.bmp")
startingbg = displayio.OnDiskBitmap("axe/STARTINGBG.bmp")
bkgnd = displayio.TileGrid(startingbg, pixel_shader=startingbg.pixel_shader)

FIELD_W =64
FIELD_H = 64

forest_bg = displayio.TileGrid(
    axe,
    pixel_shader=axe.pixel_shader,
    width=FIELD_W,
    height=FIELD_H,
    tile_width=64,
    tile_height=64,
    )
forest_bg.pixel_shader.make_transparent(30)
forest_bg.y = 64

the_axes = []
game_score = 0
game_tick = 0


def game_setup(p1_button:bool,p2_button:bool, coin_button:bool):
    text = "Press start."
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 10
    text_area.y = 10

    game_group.append(bkgnd)
    game_group.append(forest_bg)
    game_group.append(text_area)
    global game_tick
    pass


def game_frame(p1_button:bool,p2_button:bool, coin_button:bool) -> bool:
    return False


def game_over(p1_button:bool, p2_button:bool, coin_button:bool):
    global game_score
    pass
