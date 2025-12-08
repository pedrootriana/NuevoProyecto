# Mi Hackpad Personalizado 🎹

Un macropad de 4 teclas diseñado desde cero utilizando KiCAD y Fusion360. Este proyecto está basado en el microcontrolador Seeed XIAO RP2040 y utiliza el firmware KMK (CircuitPython) para ofrecer capas de productividad y control multimedia con indicadores LED RGB reactivos.

## ✨ Características

* **Doble Capa:** Cambio entre modo "Música" y "Productividad" manteniendo pulsada una tecla.
* **Feedback Visual:**
    * 🟢 **Luz Verde:** Modo Spotify/Música.
    * 🔵 **Luz Azul:** Modo Trabajo/Windows.
* **Atajos Inteligentes:** Incluye funciones de Copiar, Pegar, Multitarea (Alt+Tab) y Deshacer.
* **Hardware:** PCB personalizada con interruptores mecánicos Cherry MX y LEDs SK6812 MINI-E.

## 📸 Galería del Proyecto

### 1. El Hackpad (Render Completo)
<img width="1510" height="850" alt="Captura de pantalla 2025-12-09 002536" src="https://github.com/user-attachments/assets/36d314bd-973f-41bf-88ed-70087af8dd02" />


### 2. Esquema Electrónico (Schematic)
<img width="1142" height="783" alt="Captura de pantalla 2025-12-09 002608" src="https://github.com/user-attachments/assets/20814fec-8910-42a6-8f05-bb9b3298d3eb" />


### 3. Diseño de la PCB
<img width="595" height="674" alt="Captura de pantalla 2025-12-09 002658" src="https://github.com/user-attachments/assets/aab09b0c-1121-4396-b997-6dd5a0171b83" />


## 🛠️ Bill of Materials (BOM)

Lista de componentes necesarios para construir este proyecto:

| Cantidad | Componente | Descripción |
| :---: | :--- | :--- |
| 1 | **Seeed XIAO RP2040** | El cerebro del macropad. |
| 4 | **Interruptores (Switches)** | Tipo Cherry MX (3-pin o 5-pin). |
| 4 | **Keycaps** | Perfil DSA recomendado (1u). |
| 2 | **LEDs RGB** | Modelo SK6812 MINI-E (NeoPixel). |
| 1 | **Carcasa 3D** | Impresa en PLA o PETG. |
| 1 | **Cable USB-C** | Para conectar al PC. |

---

## ⌨️ Mapa de Teclas (Keymap)

El teclado funciona con dos capas. El **Botón 1 (Arriba-Izquierda)** actúa como tecla maestra: si lo tocas rápido ejecuta una acción, si lo mantienes pulsado cambia de capa.

### Capa 0: Modo Música 🎵 (LED Verde)
*Activa por defecto.*

| Posición | Tecla | Función |
| :--- | :--- | :--- |
| **Arriba Izq (SW1)** | `Play/Pause` | Tocar para pausar/reproducir. **Mantener para ir a Capa Azul.** |
| **Arriba Der (SW2)** | `Next Track` | Siguiente canción. |
| **Abajo Izq (SW3)** | `Vol -` | Bajar volumen. |
| **Abajo Der (SW4)** | `Vol +` | Subir volumen. |

### Capa 1: Modo Trabajo 💼 (LED Azul)
*Se activa manteniendo SW1 (aprox. 300ms).*

| Posición | Tecla | Función |
| :--- | :--- | :--- |
| **Arriba Izq (SW1)** | `Undo` | Deshacer (`Ctrl + Z`). **Mantener para volver a Capa Verde.** |
| **Arriba Der (SW2)** | `Alt + Tab` | Cambiar de ventana (Multitarea). |
| **Abajo Izq (SW3)** | `Copy` | Copiar (`Ctrl + C`). |
| **Abajo Der (SW4)** | `Paste` | Pegar (`Ctrl + V`). |

---

## 🚀 Instalación del Firmware

Este teclado utiliza **CircuitPython** y **KMK**.

1.  Conecta el XIAO RP2040 al PC manteniendo pulsado el botón "Boot".
2.  Instala CircuitPython arrastrando el archivo `.uf2` correspondiente.
3.  Una vez aparezca la unidad `CIRCUITPY`, copia dentro:
    * La carpeta `kmk` (librería).
    * El archivo `boot.py`.
    * El archivo `main.py` de este repositorio.

---

Diseñado para el programa **Hack Club Blueprint**.
