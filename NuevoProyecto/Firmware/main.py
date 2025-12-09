import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data, Color

# --- CLASE PARA GESTIÓN AUTOMÁTICA DE LUCES ---
class LayerColor:
    def __init__(self, rgb_ext):
        self.rgb = rgb_ext
        self.last_layer_state = -1

    def on_runtime(self, keyboard):
        # Detectamos si la Capa 1 (Azul) está activa
        layer_1_active = 1 in keyboard.active_layers
        
        # Solo enviamos la orden a los LEDs si ha cambiado el estado
        if layer_1_active != self.last_layer_state:
            if layer_1_active:
                # CAPA 1 (AZUL): MODO TRABAJO
                # Brillo 100 para que se note el resplandor indirecto
                self.rgb.set_hsv_fill(170, 255, 100) 
            else:
                # CAPA 0 (VERDE): MODO SPOTIFY
                # Brillo 100 para que se note el resplandor indirecto
                self.rgb.set_hsv_fill(85, 255, 100)
            
            self.last_layer_state = layer_1_active

keyboard = KMKKeyboard()

# --- CARGAMOS MÓDULOS NECESARIOS ---
macros = Macros()
keyboard.modules.append(macros)

layers = Layers()
keyboard.modules.append(layers)

holdtap = HoldTap()
keyboard.modules.append(holdtap)

# --- CONFIGURACIÓN DE PINES FÍSICOS ---
# SW1=D7, SW2=D8, SW3=D9, SW4=D10
PINS = [board.D7, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# --- CONFIGURACIÓN DE LOS LEDS (LUZ INDIRECTA) ---
rgb_ext = Rgb_matrix(
    pixel_pin=board.D4,
    num_pixels=2,
    val_limit=200,     # Límite alto para permitir el resplandor
    val_default=100,   # Brillo inicial (ajustado para luz rebotada)
)
keyboard.extensions.append(rgb_ext)
# Añadimos nuestro gestor de colores personalizado
keyboard.extensions.append(LayerColor(rgb_ext))


# --- TECLAS INTELIGENTES (SW1) ---

# Para la Capa Verde: Tap = Play/Pausa | Hold = Ir a Capa Azul (Toggle)
# Mantiene la capa Azul encendida hasta que vuelvas a pulsar SW1 mantenido
LLAVE_ENTRAR = KC.HT(KC.TG(1), KC.MEDIA_PLAY_PAUSE)

# Para la Capa Azul: Tap = Deshacer (Ctrl+Z) | Hold = Volver a Capa Verde
LLAVE_SALIR = KC.HT(KC.TG(1), KC.LCTRL(KC.Z))


# --- TU MAPA DE TECLAS DEFINITIVO ---
keyboard.keymap = [
    # --- CAPA 0: MÚSICA (Luz Verde) ---
    [
        LLAVE_ENTRAR,          # SW1: Play/Pause (Tap) | Ir a Azul (Hold)
        KC.MEDIA_NEXT_TRACK,   # SW2: Siguiente Canción
        KC.AUDIO_VOL_DOWN,     # SW3: Bajar Volumen
        KC.AUDIO_VOL_UP,       # SW4: Subir Volumen
    ],
    
    # --- CAPA 1: TRABAJO (Luz Azul) ---
    [
        LLAVE_SALIR,           # SW1: Deshacer (Tap) | Volver a Verde (Hold)
        KC.LALT(KC.TAB),       # SW2: Alt + Tab (Multitarea)
        KC.LCTRL(KC.C),        # SW3: Copiar
        KC.LCTRL(KC.V),        # SW4: Pegar
    ]
]

if __name__ == '__main__':
    keyboard.go()