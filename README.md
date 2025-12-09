# Hackpad RP2040: Teclado Macro Programable

Documentación y archivos de diseño para un macropad con 4 teclas, para el programa Hack Club Blueprint. El proyecto incluye el diseño electrónico (PCB) en KiCad, el diseño mecánico en Fusion 360 y la implementación del firmware en CircuitPython utilizando KMK.

## Especificaciones Técnicas

* **Microcontrolador:** Seeed Studio XIAO RP2040.
* **Interfaz:** USB Tipo-C.
* **Firmware:** KMK (basado en CircuitPython).
* **Entrada:** 4 interruptores mecánicos Cherry MX.
* **Indicadores:** 2 LEDs RGB SK6812 MINI-E.
* **Funcionalidad:** Soporte para múltiples capas mediante Hold-Tap.

## Documentación Visual

### 1. Renderizado Final
<img width="865" height="581" alt="Captura de pantalla 2025-12-09 124717" src="https://github.com/user-attachments/assets/95d33212-a004-4c1d-9045-47bb68e33ea3" />

Vista de la carcasa y componentes.

### 2. Esquema Electrónico
<img width="528" height="416" alt="Captura de pantalla 2025-12-09 124858" src="https://github.com/user-attachments/assets/8a3f6e10-c036-4dac-b63e-53943704cf66" />

Diagrama de conexiones.

### 3. Diseño de PCB
<img width="596" height="749" alt="Captura de pantalla 2025-12-09 124839" src="https://github.com/user-attachments/assets/17221959-ae7e-4cb8-a673-895d737d7c4d" />

Disposición de componentes.

---

## Lista de Materiales (BOM)

Componentes necesarios:

| Cantidad | Componente | Especificaciones |
| :---: | :--- | :--- |
| 1 | Seeed XIAO RP2040 | Microcontrolador principal. |
| 4 | Interruptores Mecánicos | Compatibles con footprint Cherry MX (3-pin/5-pin). |
| 4 | Keycaps | Perfil DSA (1u). |
| 2 | LEDs RGB | SK6812 MINI-E (Montaje en reverso). |
| 1 | Carcasa | Impresión 3D (PLA o PETG). |
| 4 | Tornillos | M3 x 16mm. |
| 4 | Tuercas | M3 Hexagonales. |
| 1 | Cable USB | Tipo C a Tipo A/C. |

---

## Mapa de Teclas y Funcionalidad

El dispositivo funciona con dos capas lógicas.  Utilizando el interruptor **SW1** (Superior Izquierdo), con doble función: pulsar (Tap) para ejecutar comando y mantener (Hold) para cambiar de capa.

### Capa 0: Control Multimedia (Luz Verde)
Configuración predeterminada al iniciar el dispositivo.

| Ubicación | Interruptor | Acción (Pulsación) | Acción (Mantener) |
| :--- | :--- | :--- | :--- |
| **Sup. Izq.** | **SW1** | Reproducir / Pausar | **Activar Capa 1** |
| **Sup. Der.** | **SW2** | Siguiente Pista | - |
| **Inf. Izq.** | **SW3** | Bajar Volumen | - |
| **Inf. Der.** | **SW4** | Subir Volumen | - |

### Capa 1: Productividad (Luz Azul)
Configuración para flujo de trabajo en entorno Windows.

| Ubicación | Interruptor | Acción (Pulsación) | Acción (Mantener) |
| :--- | :--- | :--- | :--- |
| **Sup. Izq.** | **SW1** | Deshacer (Ctrl+Z) | **Retornar a Capa 0** |
| **Sup. Der.** | **SW2** | Cambiar Ventana (Alt+Tab) | - |
| **Inf. Izq.** | **SW3** | Copiar (Ctrl+C) | - |
| **Inf. Der.** | **SW4** | Pegar (Ctrl+V) | - |

---

## Autor
pedrootriana
