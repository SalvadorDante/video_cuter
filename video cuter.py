from tkinter import filedialog
from moviepy.editor import VideoFileClip
import tkinter as tk

def seleccionar_video():
    archivo_video = filedialog.askopenfilename(filetypes=[("Archivos de video", "*.mp4")])
    entry_video.delete(0, tk.END)
    entry_video.insert(0, archivo_video)

def seleccionar_carpeta():
    carpeta_salida = filedialog.askdirectory()
    entry_carpeta_salida.delete(0, tk.END)
    entry_carpeta_salida.insert(0, carpeta_salida)

def recortar_video():
    nombre_video = entry_video.get()
    duracion_clip = int(entry_duracion.get())
    carpeta_salida = entry_carpeta_salida.get()

    video = VideoFileClip(nombre_video)
    duracion_total = video.duration

    cantidad_clips = int(duracion_total / duracion_clip)
    duracion_ultimo_clip = duracion_total % duracion_clip

    lbl_resultado.config(text=f"Se generarán {cantidad_clips} clips de {duracion_clip} segundos cada uno")

    nombre_salida_base = entry_nombre_salida.get()

    for i in range(cantidad_clips):
        tiempo_inicio = i * duracion_clip
        tiempo_fin = (i + 1) * duracion_clip
        nombre_salida = f"{nombre_salida_base}_{i+1}.mp4"

        clip_recortado = video.subclip(tiempo_inicio, tiempo_fin)
        ruta_salida = f"{carpeta_salida}/{nombre_salida}"
        clip_recortado.write_videofile(ruta_salida, codec="libx264", threads=4, preset="ultrafast")

    if duracion_ultimo_clip > 0:
        tiempo_inicio_ultimo = cantidad_clips * duracion_clip
        tiempo_fin_ultimo = duracion_total
        nombre_ultimo_salida = f"{nombre_salida_base}_{cantidad_clips+1}.mp4"

        clip_ultimo = video.subclip(tiempo_inicio_ultimo, tiempo_fin_ultimo)
        ruta_ultimo_salida = f"{carpeta_salida}/{nombre_ultimo_salida}"
        clip_ultimo.write_videofile(ruta_ultimo_salida, codec="libx264", threads=4, preset="ultrafast")

    video.close()
    lbl_resultado.config(text="Recorte completado")

ventana = tk.Tk()
ventana.title("Video Cutter")

# Etiqueta y campo de entrada para el video
lbl_video = tk.Label(ventana, text="Video:")
lbl_video.grid(row=0, column=0, padx=10, pady=10)
entry_video = tk.Entry(ventana, width=50)
entry_video.grid(row=0, column=1, padx=10, pady=10)
btn_seleccionar = tk.Button(ventana, text="Seleccionar", command=seleccionar_video)
btn_seleccionar.grid(row=0, column=2, padx=10, pady=10)

# Etiqueta y campo de entrada para la duración de cada clip
lbl_duracion = tk.Label(ventana, text="Duración de cada clip (segundos):")
lbl_duracion.grid(row=1, column=0, padx=10, pady=10)
entry_duracion = tk.Entry(ventana, width=10)
entry_duracion.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta y campo de entrada para la carpeta de salida
lbl_carpeta_salida = tk.Label(ventana, text="Carpeta de salida:")
lbl_carpeta_salida.grid(row=2, column=0, padx=10, pady=10)
entry_carpeta_salida = tk.Entry(ventana, width=50)
entry_carpeta_salida.grid(row=2, column=1, padx=10, pady=10)
btn_seleccionar_carpeta = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta)
btn_seleccionar_carpeta.grid(row=2, column=2, padx=10, pady=10)

# Etiqueta y campo de entrada para el nombre del archivo de salida
lbl_nombre_salida = tk.Label(ventana, text="Nombre del archivo de salida:")
lbl_nombre_salida.grid(row=3, column=0, padx=10, pady=10)
entry_nombre_salida = tk.Entry(ventana, width=50)
entry_nombre_salida.grid(row=3, column=1, padx=10, pady=10)

# Botón de recorte
btn_recortar = tk.Button(ventana, text="Recortar", command=recortar_video)
btn_recortar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
lbl_resultado = tk.Label(ventana, text="")
lbl_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
