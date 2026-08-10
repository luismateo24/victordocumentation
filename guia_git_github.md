# Guía rápida — Git y GitHub

## Flujo local
```bash
git init                          # Iniciar el repositorio
git add .                         # Preparar archivos
git commit -m "mensaje"           # Guardar una version
git log --oneline                 # Ver el historial de commits
```

## Conectar con GitHub (solo la primera vez)
1. Crear cuenta en github.com
2. New repository → nombre → descripción → público → SIN marcar README → Create
3. Copiar la URL que muestra

```bash
git remote add origin [URL]
git branch -M main
git push -u origin main
```

## Para subir cambios nuevos (después de la primera vez)
```bash
git add .
git commit -m "mensaje describiendo el cambio"
git push
```

## Verificar identidad (si es necesario)
"Tu Nombre" = tu usuario o nombre real de GitHub
"tu-correo" = el correo con el que creaste tu cuenta de GitHub
```bash
git config --global user.name "Usuario GitHub"
git config --global user.email "Correo cuenta GitHub"
```

## Nota importante
`git init` se hace UNA SOLA VEZ, la primera vez que empiezas el proyecto en esa carpeta. Si ya lo hiciste antes, no lo repitas — solo sigue con `add`, `commit`, `push`.

## Al terminar, en PCs del SENA (compartidos)
Borra tu identidad para que el siguiente usuario no quede configurado con tu nombre:
```bash
git config --global --unset user.name
git config --global --unset user.email
```

## Si el PC ya tiene un repo de otro usuario
```bash
git status
```
Si muestra algo raro, muévete a una carpeta nueva antes de `git init`.
