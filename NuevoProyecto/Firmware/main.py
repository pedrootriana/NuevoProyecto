import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data, Color

# --- GESTIÓN DE COLORES AUTOMÁTICA ---
class LayerColor:
    def __init__(self, rgb_ext):
        self.rgb = rgb_ext
        self.last_layer_state = -1

    def on_runtime(self, keyboard):
        # Detectamos si la Capa 1 (Azul) está activa
        layer_1_active = 1 in keyboard.active_layers
        
        # Solo cambiamos el color si ha habido un cambio de capa
        if layer_1_active != self.last_layer_state:
            if layer_1_active:
                # CAPA 1 (AZUL): MODO TRABAJO
                self.rgb.set_hsv_fill(170, 255, 15) # Brillo 15 (Suave)
            else:
                # CAPA 0 (VERDE): MODO SPOTIFY
                self.rgb.set_hsv_fill(85, 255, 15)  # Brillo 15 (Suave)
            
            self.last_layer_state = layer_1_active

keyboard = KMKKeyboard()

# --- MÓDULOS NECESARIOS ---
macros = Macros()
keyboard.modules.append(macros)

layers = Layers()
keyboard.modules.append(layers)

holdtap = HoldTap()
keyboard.modules.append(holdtap)

# --- PINES DE TU PCB ---
# SW1=D7, SW2=D8, SW3=D9, SW4=D10
PINS = [board.D7, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# --- CONFIGURACIÓN DE LEDS (MODO INDICADOR) ---
rgb_ext = Rgb_matrix(
    pixel_pin=board.D4,
    num_pixels=2,
    val_limit=20,      # Límite máximo de brillo (aprox 8%)
    val_default=15,    # Brillo por defecto al encender
)
keyboard.extensions.append(rgb_ext)
# Añadimos el gestor de colores a las extensiones
keyboard.extensions.append(LayerColor(rgb_ext))

# --- TECLAS INTELIGENTES (SW1) ---

# Para la Capa Verde: Tap = Play/Pausa | Hold = Ir a Capa Azul (Toggle)
LLAVE_ENTRAR = KC.HT(KC.TG(1), KC.MEDIA_PLAY_PAUSE)

# Para la Capa Azul: Tap = Deshacer (Ctrl+Z) | Hold = Volver a Capa Verde (Toggle)
LLAVE_SALIR = KC.HT(KC.TG(1), KC.LCTRL(KC.Z))


# --- TU MAPA DE TECLAS DEFINITIVO ---
keyboard.keymap = [
    # --- CAPA 0: MÚSICA (Verde Suave) ---
    [
        LLAVE_ENTRAR,          # SW1
        KC.MEDIA_NEXT_TRACK,   # SW2
        KC.AUDIO_VOL_DOWN,     # SW3
        KC.AUDIO_VOL_UP,       # SW4
    ],
    
    # --- CAPA 1: TRABAJO (Azul Suave) ---
    [
        LLAVE_SALIR,           # SW1: Deshacer / Salir
        KC.LALT(KC.TAB),       # SW2: Alt + Tab (Multitarea)
        KC.LCTRL(KC.C),        # SW3: Copiar
        KC.LCTRL(KC.V),        # SW4: Pegar
    ]
]

if __name__ == '__main__':
    keyboard.go()