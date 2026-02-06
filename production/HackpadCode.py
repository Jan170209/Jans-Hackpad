# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler 

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Encoder 
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define your pins here!
PINS = [board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
    KC.Macro(Press(KC.G), Tap(KC.L), Release(KC.G)), #Line
    KC.Macro(Press(KC.G), Tap(KC.R), Release(KC.G)), #Rectangle
    KC.Macro(Press(KC.G), Tap(KC.C), Release(KC.G)), #Circle
    KC.Macro(Press(KC.G), Tap(KC.A), Release(KC.G)), #Arch
    KC.Macro(Press(KC.G), Tap(KC.N), Release(KC.G)), #Hilfsgeometrie
    KC.Macro(Press(KC.G), Tap(KC.X), Release(KC.G)), #Externe Geometrie
    ]
]

# Encoder Pins
encoder_handler.pins =(
    (board.D2, board.D3)
)

# Encoder Actions
encoder_handler.map = [
    (KC.VOLU, KC.VOLD),
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()