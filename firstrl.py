import libtcodpy as libtcod

# Actual size of window in characters, not pixels
SCREEN_WIDTH = 80  
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

LIMIT_FPS = 20     # Max FPS

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

class GameObject:
    # This is a generic object: a player, a monster and item etc...
    # It's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Move by given amount.
        self.x += dx
        self.y += dy

    def draw(self):
        # Set the colour and draw the character that represents the object
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self):
        # Erase the character that represents the object.
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        
class Tile:
    # Tile class. For walls and floor. block vision? Passable?
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        # If a tile blocks movement it also blocks sight by default. This can be changed per tile.
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight


def make_map():
    global map
    #fill map with unblocked tiles
    map = [[ Tile(False)
        for y in range(MAP_HEIGHT)]
            for x in range(MAP_WIDTH)]
    # Place two pillars to test map
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[50[22].blocked = True
    map[50][22].block_sight = True


def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # alt + enter toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0)

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0) 


# ------------------
# Initilization
# ------------------

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# initilize the root window and set width, height, title and fullscreen or not
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Neils RL', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
# set FPS limit, only matters if you opt for real time game
libtcod.sys_set_fps(LIMIT_FPS)

# Create GameObject representing the player
player = GameObject(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)

# Create a new NPC
npc = GameObject(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
objects = [npc, player]
# ---------------- 
# main game loop.
# ----------------

while not libtcod.console_is_window_closed():
    # Draw all objects in the list.
    for obj in objects:
        obj.draw()

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    # Erase all objects at their old location
    for obj in objects:
        obj.clear()

    # Handle keys and exit if needed
    exit = handle_keys()
    if exit:
        break
