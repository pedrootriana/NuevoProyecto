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
![Render del Hackpad](ruta/a/tu/imagen_render_completo.png)
*(Vista general de cómo queda la carcasa con la PCB y las teclas)*

### 2. Esquema Electrónico (Schematic)
![Esquema en KiCAD](ruta/a/tu/imagen_esquematico.png)
*(Conexiones del XIAO RP2040 a los 4 switches y los LEDs)*

### 3. Diseño de la PCB
![Diseño PCB 2D](ruta/a/tu/imagen_pcb.png)
*(El enrutado de las pistas y colocación de componentes en KiCAD)*

### 4. La Carcasa (Case)
![Carcasa 3D](ruta/a/tu/imagen_carcasa.png)
*(Diseño de la caja impreso en 3D)*

---

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

### Capa 0:
