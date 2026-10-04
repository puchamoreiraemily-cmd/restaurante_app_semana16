# 🍽️ Restaurante App

Sistema de gestión para un restaurante desarrollado en Python utilizando Tkinter.

El proyecto permite administrar usuarios, productos y ventas mediante una interfaz gráfica, manteniendo la información persistida en archivos JSON.

## 📚 Semana 16 - Manejo de eventos en Tkinter

En esta semana se evolucionó el proyecto para incorporar la gestión de usuarios mediante una interfaz gráfica con formulario y tabla `Treeview`.

Se mantuvo la arquitectura modular del proyecto y se agregaron eventos de Tkinter para mejorar la interacción con el usuario.

## 🎯 Objetivo

Implementar el manejo de eventos en Tkinter dentro de un sistema de gestión de restaurante, utilizando:

- `bind()`
- `command=`
- Callbacks
- `Treeview`
- `<<TreeviewSelect>>`
- `<Return>`
- `<Escape>`
- `<<ComboboxSelected>>`

## 🏗️ Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── logo.png
│
├── main.py
└── README.md