# 📁 Brochure Corporativo — INTAY CORPORATION SAC

> Dossier corporativo digital en formato HTML + CSS (Tailwind), listo para exportar como PDF de calidad profesional en tamaño A4.

---

## 🏭 ¿Qué es este proyecto?

Este repositorio contiene el **brochure/dossier corporativo digital** de **INTAY CORPORATION SAC**, empresa peruana especializada en ingeniería metalmecánica, estructuras metálicas, construcciones industriales y fabricación de equipos, ubicada en Cajabamba, Perú.

El brochure está construido completamente en **HTML + Tailwind CSS**, diseñado para imprimirse o exportarse como PDF en formato A4 (210mm × 297mm), conservando todos los colores, imágenes y diseños gráficos tal cual se ven en pantalla.

---

## 📄 Estructura de Páginas

El brochure contiene **7 páginas A4** (algunas páginas contienen 2 vistas):

| N° | Archivo | Contenido |
|----|---------|-----------|
| 01 | `portada.html` | Portada principal con logo, imagen de obra y slogan |
| 02 | `quienes_somos.html` | Misión, visión, valores e indicadores corporativos |
| 03 | `certificados.html` | Certificaciones de soldadura AWS D1.1 (3G, 4G, 6G) |
| 04-05 | `servicios.html` | Las 4 especialidades de servicio con imágenes reales |
| 06 | `proyectos_destacados.html` | Proyectos ejecutados: obra educativa y Planta ADR–UM Shahuindo |
| 07 | `contacto.html` | Datos de contacto: teléfonos, correo y ubicación |

---

## 📂 Estructura de Carpetas

```
brochure_intay/
│
├── portada.html
├── quienes_somos.html
├── certificados.html
├── servicios.html
├── proyectos_destacados.html
├── contacto.html
│
├── generar_brochure.py          ← Script para unir TODO en un solo HTML
├── brochure_completo_para_imprimir.html  ← Archivo unificado generado automáticamente
│
├── logo.jpeg                    ← Logo oficial de INTAY CORPORATION
│
└── imagenes/
    ├── portada/                 ← Imagen de fondo de portada
    ├── proyectos/               ← Fotos de obras ejecutadas
    │   └── nave/                ← Imágenes de la nave industrial
    └── servicios/               ← Imágenes de cada especialidad de servicio
```

---

## 🚀 ¿Cómo generar el PDF?

### Paso 1 — Instalar Python (si no lo tienes)
Descárgalo desde [https://python.org](https://python.org) e instálalo.

### Paso 2 — Ejecutar el script generador

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python generar_brochure.py
```

Esto realizará automáticamente dos cosas:
1. ✅ Unirá los 6 archivos HTML en uno solo: `brochure_completo_para_imprimir.html`
2. ✅ Abrirá ese archivo automáticamente en tu navegador web

### Paso 3 — Exportar a PDF desde el navegador

Una vez abierto en el navegador (Chrome o Edge recomendado):

1. Presiona **`Ctrl + P`** (Imprimir)
2. En **"Impresora/Destino"** selecciona → **Guardar como PDF**
3. En **"Márgenes"** selecciona → **Ninguno**
4. Activa la casilla → **✅ Gráficos de fondo** (esto asegura que los colores oscuros y fondos aparezcan correctamente)
5. Haz clic en **Guardar**

> ⚠️ **IMPORTANTE:** Sin activar "Gráficos de fondo" los fondos oscuros, naranjas y grillas no se exportarán al PDF.

---

## 🎨 Identidad Visual

| Elemento | Valor |
|----------|-------|
| Color primario | `#040812` — Azul Marino Oscuro |
| Color de acento | `#FF6600` — Naranja Industrial |
| Color secundario | `#1C2D42` — Azul Acero |
| Tipografía títulos | **Oswald** (Google Fonts) |
| Tipografía cuerpo | **Inter** (Google Fonts) |
| Tamaño de hoja | A4 → `794px × 1123px` (96 DPI) |

---

## 📞 Datos de Contacto de INTAY

| Canal | Dato |
|-------|------|
| 📱 WhatsApp / Teléfono | 914 042 943 · 997 607 951 |
| 📧 Correo | intaycorp@gmail.com |
| 📍 Dirección | Jr. Blondel 921, Cajabamba, Perú |

---

## 🛠️ Tecnologías Usadas

- **HTML5** — Estructura semántica de cada página
- **Tailwind CSS** (via CDN) — Estilos utilitarios modernos
- **Google Fonts** — Tipografías Oswald e Inter
- **Python 3** — Script de automatización para unir páginas y generar PDF
- **CSS `@media print` + `@page`** — Control preciso de impresión A4

---

## 📝 Notas de Mantenimiento

- Cada página del brochure es un archivo HTML **independiente** → puedes editar una sin afectar las demás.
- Después de cualquier edición, vuelve a ejecutar `python generar_brochure.py` para regenerar el archivo unificado de impresión.
- Las imágenes usan **rutas relativas** → deben estar siempre dentro de la carpeta `imagenes/` junto a los archivos HTML.

---

*Desarrollado con ❤️ para INTAY CORPORATION SAC — Cajabamba, Perú 🇵🇪*
