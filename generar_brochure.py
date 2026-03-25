import os
import webbrowser

archivos = [
    "portada.html",
    "quienes_somos.html",
    "certificados.html",
    "proyectos_destacados.html",
    "servicios.html",
    "contacto.html"
]

html_inicio = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brochure Completo - INTAY CORPORATION</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Oswald:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #040812;      
            --orange-brand: #FF6600; 
            --steel-blue: #1C2D42;   
        }
        body { 
            background-color: #f3f4f6; 
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2rem;
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        .font-title { font-family: 'Oswald', sans-serif; }
        .a4-container {
            width: 794px;
            height: 1123px; /* Reemplaza aspect-ratio para evitar el bug de colapso en PDF */
            background-color: white; /* Por defecto */
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
            page-break-after: always;
        }
        
        /* Portada Específicos */
        .industrial-grid {
            background-color: #040812 !important;
            background-image: 
                linear-gradient(rgba(255, 102, 0, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 102, 0, 0.04) 1px, transparent 1px);
            background-size: 25px 25px;
        }
        .steel-triangle {
            position: absolute; bottom: 0; right: 0; width: 60%; height: 45%;
            background-color: var(--steel-blue); clip-path: polygon(100% 0, 100% 100%, 0 100%); opacity: 0.8; z-index: 1;
        }
        .logo-decoration { position: absolute; border: 2px solid rgba(255, 102, 0, 0.3); border-radius: 50%; }
        .decoration-ring-1 { width: 420px; height: 420px; top: 50%; left: 50%; transform: translate(-50%, -50%); animation: spin 30s linear infinite reverse; }
        .decoration-ring-2 { width: 500px; height: 500px; top: 50%; left: 50%; transform: translate(-50%, -50%); border: 1px solid rgba(255, 102, 0, 0.2); animation: spin 40s linear infinite; }
        .decoration-corner-top-left { width: 120px; height: 120px; border-right: 3px solid var(--orange-brand); border-bottom: 3px solid var(--orange-brand); opacity: 0.4; }
        .decoration-corner-bottom-right { width: 80px; height: 80px; border-left: 3px solid var(--orange-brand); border-top: 3px solid var(--orange-brand); opacity: 0.4; }
        @keyframes spin { from { transform: translate(-50%, -50%) rotate(0deg); } to { transform: translate(-50%, -50%) rotate(360deg); } }

        /* Varios Generales */
        .triangle-orange { width: 0; height: 0; }
        .pattern-bg {
            position: absolute; inset: 0;
            background-image: 
                linear-gradient(rgba(28, 45, 66, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(28, 45, 66, 0.05) 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .label-tag { clip-path: polygon(0 0, 100% 0, 92% 100%, 0 100%); }
        .industrial-grid-orange {
            position: absolute; inset: 0;
            background-image: linear-gradient(rgba(255, 102, 0, 0.01) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 102, 0, 0.01) 1px, transparent 1px);
            background-size: 30px 30px; z-index: 1;
        }
        .octagon { clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%); }

        /* Fix para Contacto */
        .contacto-fix {
            align-items: center !important;
            justify-content: center !important;
            background-color: #0e1e35 !important;
        }

        /* MAGIA PARA PDF EXACTO */
        @page {
            size: 794px 1123px; /* Forzamos tamaño de página exacto en píxeles (A4 a 96DPI) */
            margin: 0;
        }
        @media print {
            html, body { 
                display: block !important; /* FACTOR CRÍTICO: Si el body es flex, el PDF se rompe y los page-breaks se ignoran */
                background: white; 
                padding: 0 !important; 
                margin: 0 !important; 
                width: 100% !important;
                height: auto !important; /* body height auto para que el contenido sea el que empuje */
            }
            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            .a4-container { 
                box-shadow: none !important; 
                page-break-after: always !important;
                page-break-inside: avoid !important;
                margin: 0 !important;
                border: none !important;
                
                /* EL FIX CLAVE: Dimensiones precisas absolutas en píxeles igual que en pantalla */
                width: 794px !important;
                height: 1123px !important;
                min-height: 1123px !important;
                max-height: 1123px !important;
                position: relative !important;
            }
        }
    </style>
</head>
<body>
"""

html_fin = """
</body>
</html>
"""

contenido_cuerpos = ""

for archivo in archivos:
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            html_raw = f.read()
            
            if '<body' in html_raw and '</body>' in html_raw:
                body_start = html_raw.find('>', html_raw.find('<body')) + 1
                body_end = html_raw.find('</body>')
                body_content = html_raw[body_start:body_end].strip()
                
                # REPARACIÓN DE CLASES PERDIDAS AL UNIFICAR
                # Asegurarnos de que las páginas viejas tengan "a4-container" y HEIGHT FIJO para evitar colapsos
                body_content = body_content.replace('class="relative w-full max-w-[794px] aspect-[1/1.414]', 'class="a4-container relative w-full max-w-[794px] h-[1123px]')
                
                # Arreglos específicos por archivo
                if archivo == "contacto.html":
                    body_content = body_content.replace('class="a4-container"', 'class="a4-container contacto-fix"')
                
                contenido_cuerpos += f"<!-- ======= INICIO DE {archivo.upper()} ======= -->\n"
                contenido_cuerpos += body_content + "\n"
                contenido_cuerpos += f"<!-- ======= FIN DE {archivo.upper()} ======= -->\n\n"

html_final = html_inicio + contenido_cuerpos + html_fin

salida = "brochure_completo_para_imprimir.html"
with open(salida, 'w', encoding='utf-8') as f:
    f.write(html_final)

print(f"¡Éxito! Se ha unido todo en HTML: {salida}")
print("Abriendo automáticamente en tu navegador...")

# Abrir automáticamente en el navegador por defecto
webbrowser.open('file://' + os.path.realpath(salida))

print("Una vez abierto, recuerda presionar 'Ctrl + P', poner Márgenes en 'Ninguno' y marcar 'Gráficos de Fondo'.")
