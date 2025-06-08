function crearBloc() {
    const nombre = document.getElementById('nombreBloc').value;
    const privado = document.getElementById('privadoBloc').checked;
    fetch('/crear_bloc', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `nombre=${encodeURIComponent(nombre)}&privado=${privado}`
    }).then(res => res.json()).then(data => {
        if (data.success) location.reload();
    });
}

function agregarNota(idBloc) {
    const input = document.getElementById('nuevaNota-' + idBloc);
    const texto = input.value;
    fetch('/agregar_nota', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `texto=${encodeURIComponent(texto)}&bloc_id=${idBloc}`
    }).then(res => res.json()).then(data => {
        if (data.success) location.reload();
    });
}

function borrarBloc(idBloc) {
    if (!confirm("¿Seguro que deseas eliminar este bloc?")) return;
    fetch('/borrar_bloc', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `id=${idBloc}`
    }).then(res => res.json()).then(data => {
        if (data.success) location.reload();
    });
}

function mostrarEdicion(notaId) {
    const li = document.getElementById(`nota-${notaId}`);
    const span = li.querySelector('.texto-nota');
    const autor = li.querySelector('small').innerText;
    const textoOriginal = span.textContent;

    // Crear input y botón
    const input = document.createElement('input');
    input.type = 'text';
    input.value = textoOriginal;

    const guardarBtn = document.createElement('button');
    guardarBtn.innerText = 'Guardar';
    guardarBtn.onclick = () => {
        const nuevoTexto = input.value.trim();
        if (nuevoTexto === "") {
            alert("La nota no puede estar vacía.");
            return;
        }

        fetch(`/editar_nota/${notaId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texto: nuevoTexto })
        }).then(res => res.json())
          .then(data => {
            if (data.status === "success") {
                // Limpiar el contenido del li y reconstruirlo
                li.innerHTML = `
                    <span class="texto-nota">${nuevoTexto}</span>
                    <small>${autor}</small>
                    <small class="editado">(editado)</small>
                    <button onclick="mostrarEdicion(${notaId})" class="btn-editar">Editar</button>
                    <button onclick="eliminarNota(${notaId})" class="btn-eliminar">Eliminar</button>
                `;
            } else {
                alert("Error al editar la nota.");
            }
        });
    };

    // Insertar input y botón en el li
    li.insertBefore(input, span);
    li.insertBefore(guardarBtn, span);
    span.style.display = 'none';
}


function eliminarNota(notaId) {
    fetch(`/eliminar_nota/${notaId}`, {
        method: 'POST'
    }).then(res => {
        if (res.ok) {
            const li = document.getElementById(`nota-${notaId}`);
            li.remove();
        }
    });
}

function guardarEdicionNota(id) {
    const notaLi = document.getElementById(`nota-${id}`);
    const input = notaLi.querySelector('input');
    const nuevoTexto = input.value.trim();

    if (nuevoTexto === "") {
        alert("La nota no puede estar vacía.");
        return;
    }

    fetch(`/editar-nota/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto: nuevoTexto }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            notaLi.innerHTML = `${nuevoTexto} - <small>${data.autor}</small> <span class="editado">(editado)</span>`;
        } else {
            alert(data.error || "Error al editar la nota.");
        }
    });
}

