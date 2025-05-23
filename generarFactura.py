import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF
from datetime import datetime
import random
import sys
import os

def resource_path(relative_path):
    """ Obtener ruta absoluta, funciona para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generar_factura():
    
    nombre_cliente = nombre_cliente_entry.get()
    apellidos_cliente = apellidos_cliente_entry.get()
    telefono_cliente = telefono_cliente_entry.get()
    dni_cliente = dni_cliente_entry.get()
    ciudad_cliente = ciudad_cliente_entry.get()
    nombre_servicio = nombre_servicio_entry.get()
    descrpcion_servicio = descripcion_servicio_entry.get()
    total_servicio = total_servicio_entry.get()

    fecha_factura = datetime.now().strftime('%d/%m/%Y')

    identificador_factura = 'F' + str(random.randint(1000000, 9999999))

    pdf = FPDF()
    pdf.add_page()

    logo_path = resource_path('logoCadetUsh.png')
    logo_path_x = resource_path('facturaX.png')
    pdf.image(logo_path, x=160, y=8, w=40)
    

    pdf.set_xy(10, 10)
    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, 'CadetUsh', ln=True)
    pdf.cell(0, 10, 'Guanaco N° 65', ln=True)
    pdf.cell(0, 10, '27-28545197-9', ln=True)
    pdf.cell(0, 10, f'Fecha: {fecha_factura}', ln=True)

    pdf.ln(20)

    pdf.set_font('Arial', size=16)
    pdf.cell(0, 10, 'Factura', ln=True, align='C')

    y_actual = pdf.get_y()
    pdf.image(logo_path_x, x=95, y=y_actual + 2, w=20)

    pdf.set_xy(10, y_actual + 30)  

    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, f'N° de Factura: {identificador_factura}', ln=True, align='C')


    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, '-----------------------------------------', ln=True, align='L')

   
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Datos del Cliente', ln=True, align='L')

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(30, 10, 'Nombre:', border=0, ln=0)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, nombre_cliente, ln=True)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(30, 10, 'Apellido/s:', border=0, ln=0)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, apellidos_cliente, ln=True)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(30, 10, 'Teléfono:', border=0, ln=0)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, telefono_cliente, ln=True)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(30, 10, 'DNI:', border=0, ln=0)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, dni_cliente, ln=True)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(30, 10, 'Ciudad:', border=0, ln=0)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, ciudad_cliente, ln=True)

    # Otro título en negrita
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Detalles del Servicio', ln=True, align='L')

    pdf.cell(0, 10, '-----------------------------------------', ln=True, align='L')

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Nombre del Servicio', border=1)
    pdf.cell(80, 10, 'Descripción del Servicio', border=1)
    pdf.cell(30, 10, 'Total', border=1, ln=True)

    
    pdf.set_font('Arial', '', 12)
    pdf.cell(60, 10, nombre_servicio, border=1)
    pdf.cell(80, 10, descrpcion_servicio, border=1)
    pdf.cell(30, 10, f'${total_servicio}', border=1, ln=True)

    pdf.cell(0, 10, '========================================', ln=True, align='L')

    pdf.set_text_color(0, 0, 255)

    pdf.cell(0, 10, 'Gracias por usar nuestro Servicio !!!', ln=True, align='C')

    pdf.set_text_color(0, 0, 0)

    #ruta para generar un dialogo con el cliente y guardar las facturas en la carpeta que el elija
    pdf_file = f'Factura_{nombre_cliente}_{apellidos_cliente}.pdf'

    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        initialfile=pdf_file,
        filetypes=[("Archivos PDF", "*.pdf")],
        title="Guardar Factura"
    )

    if ruta_archivo:
        pdf.output(ruta_archivo, 'F')
        messagebox.showinfo('Factura Generada', f'Factura guardada en: {ruta_archivo}')
    else:
        messagebox.showwarning('Guardado cancelado', 'No se guardó la factura.')

        









root = tk.Tk()
root.title('Generador de Facturas')

frame = ttk.Frame(root, padding='10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text='Nombre del Cliente').grid(row=0, column=0, sticky=tk.W)
nombre_cliente_entry= ttk.Entry(frame, width=30)
nombre_cliente_entry.grid(row=0, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Apellidos del Cliente').grid(row=1, column=0, sticky=tk.W)
apellidos_cliente_entry= ttk.Entry(frame, width=30)
apellidos_cliente_entry.grid(row=1, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Teléfono del Cliente').grid(row=2, column=0, sticky=tk.W)
telefono_cliente_entry= ttk.Entry(frame, width=30)
telefono_cliente_entry.grid(row=2, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='DNI del Cliente').grid(row=3, column=0, sticky=tk.W)
dni_cliente_entry= ttk.Entry(frame, width=30)
dni_cliente_entry.grid(row=3, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Ciudad del Cliente').grid(row=4, column=0, sticky=tk.W)
ciudad_cliente_entry= ttk.Entry(frame, width=30)
ciudad_cliente_entry.grid(row=4, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Nombre del Servicio').grid(row=5, column=0, sticky=tk.W)
nombre_servicio_entry= ttk.Entry(frame, width=30)
nombre_servicio_entry.grid(row=5, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Descripción del Servicio').grid(row=6, column=0, sticky=tk.W)
descripcion_servicio_entry= ttk.Entry(frame, width=30)
descripcion_servicio_entry.grid(row=6, column=1, sticky=(tk.E,tk.E))

ttk.Label(frame, text='Total ($)').grid(row=7, column=0, sticky=tk.W)
total_servicio_entry= ttk.Entry(frame, width=30)
total_servicio_entry.grid(row=7, column=1, sticky=(tk.E,tk.E))

generar_factura_btn = ttk.Button(frame, text='Generar Factura', command=generar_factura) 
generar_factura_btn.grid(row=8, column=0, columnspan=2)

root.mainloop()