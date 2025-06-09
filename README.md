# 📝 Bloc de Notas Comunitario

Este proyecto es una aplicación web de un **Bloc de Notas Comunitario**, desarrollado como parte de la materia **Programación Avanzada**. Permite a los usuarios crear blocs de notas, escribir y editar notas, y gestionar la privacidad del contenido.

## 🚀 Funcionalidades principales

- ✅ Login simple con nombre de usuario
- ✅ Creación de blocs de notas públicos o privados
- ✅ Agregado de notas por usuario
- ✅ Edición y eliminación de notas (solo por el autor o el creador del bloc)
- ✅ El creador del bloc puede eliminar todo el bloc
- ✅ Sistema visual de edición con texto "editado"
- ✅ Estilo moderno y responsivo

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask** (framework web)
- **Peewee** (ORM para SQLite)
- **SQLite** (base de datos liviana)
- **HTML, CSS, JavaScript** (frontend puro, sin frameworks)

## 🧩 Estructura del proyecto

```
📁 proyecto/
├── app.py                # Servidor Flask principal
├── models.py             # Modelos ORM (Usuario, Bloc, Nota)
├── templates/
│   └── index.html        # Vista principal
├── static/
│   ├── style.css         # Estilos del sitio
│   └── script.js         # Funciones JS (agregar, editar, eliminar)
├── database.db           # Base de datos SQLite (autogenerada)
└── README.md             # Este archivo
```

## ⚙️ Cómo ejecutar el proyecto

### 1. Descargar el proyecto

```bash
git clone https://github.com/enzolarrea/tp-peewee.git
cd tp-peewee
```

> O descargá el archivo ZIP desde GitHub y descomprimilo.

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
Si da error instalar:
apt install python3.(version)-venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install flask peewee
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

### 5. Abrir la aplicación en el navegador

Abrí tu navegador y andá a:  
👉 [http://localhost:5000](http://localhost:5000)

¡Listo! Ya podés comenzar a usar el bloc de notas comunitario.

## 👨‍💻 Autores

- **Nombre:** Enzo Larrea, Nicolas Saavedra, Ezequiel Bota
- **Proyecto para:** Programación Avanzada

---

¡Gracias por visitar este proyecto!
